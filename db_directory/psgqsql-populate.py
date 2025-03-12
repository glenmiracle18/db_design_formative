import os
from dotenv import load_dotenv  # Import load_dotenv to load .env file
import psycopg2
import pandas as pd
from psycopg2 import Error
import logging
from psycopg2.extras import execute_values


load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Connection string for Neon PostgreSQL
connection_string = os.getenv("POSTGRES_CS")  # from dotenv

try:
    # Connect to the database with a timeout
    conn = psycopg2.connect(connection_string, connect_timeout=10)
    conn.autocommit = False  # Manual commit for batch operations
    cursor = conn.cursor()
    logging.info("Connected to PostgreSQL database successfully.")

    # Load CSV data
    df = pd.read_csv("restaurant_customer_satisfaction.csv")
    logging.info(f"Loaded CSV with {len(df)} rows.")

    # Gender mapping
    gender_map = {"Male": 0, "Female": 1}

    # Batch insert into Customers operation
    customer_data = [
        (str(row["CustomerID"]), row["Age"], gender_map[row["Gender"]], row["Income"])
        for _, row in df.iterrows()
    ]
    execute_values(cursor, """
        INSERT INTO Customers (customer_id, age, gender, income)
        VALUES %s
        ON CONFLICT (customer_id) DO NOTHING;
    """, customer_data)
    logging.info("Inserted data into Customers table.")

    # Batch insert into Visits
    visit_data = [
        (str(row["CustomerID"]), row["VisitFrequency"], row["AverageSpend"], row["PreferredCuisine"],
         row["TimeOfVisit"], row["GroupSize"], row["DiningOccasion"], row["MealType"],
         bool(row["OnlineReservation"]), bool(row["DeliveryOrder"]), bool(row["LoyaltyProgramMember"]),
         row["WaitTime"], row["ServiceRating"], row["FoodRating"], row["AmbianceRating"])
        for _, row in df.iterrows()
    ]
    execute_values(cursor, """
        INSERT INTO Visits (customer_id, visit_frequency, average_spend, preferred_cuisine, 
                           time_of_visit, group_size, dining_occasion, meal_type, 
                           online_reservation, delivery_order, loyalty_program_member, 
                           wait_time, service_rating, food_rating, ambiance_rating)
        VALUES %s
        RETURNING visit_id;
    """, visit_data)
    visit_ids = cursor.fetchall()  # Fetch all visit_ids
    logging.info(f"Inserted {len(visit_ids)} rows into Visits table (expected {len(df)}).")

    # Check if visit_ids matches CSV row count
    if len(visit_ids) != len(df):
        logging.warning(f"Mismatch: {len(visit_ids)} visit_ids returned, but {len(df)} rows in CSV.")

    # Batch insert into Satisfaction, only for successfully inserted visits
    satisfaction_data = [
        (str(row["CustomerID"]), visit_ids[i][0], bool(row["HighSatisfaction"]))
        for i, (_, row) in enumerate(df.iterrows())
        if i < len(visit_ids)  # Ensure we don't exceed visit_ids length
    ]
    execute_values(cursor, """
        INSERT INTO Satisfaction (customer_id, visit_id, satisfaction)
        VALUES %s;
    """, satisfaction_data)
    logging.info(f"Inserted {len(satisfaction_data)} rows into Satisfaction table.")

    # Commit all changes
    conn.commit()
    logging.info("PostgreSQL database populated successfully!")

except Error as e:
    logging.error(f"Error connecting to PostgreSQL or executing query: {e}")
    if conn:
        conn.rollback()

except Exception as e:
    logging.error(f"Unexpected error: {e}")
    if conn:
        conn.rollback()

finally:
    # Close connection
    if 'conn' in locals() and conn:
        cursor.close()
        conn.close()
        logging.info("PostgreSQL connection closed.")
