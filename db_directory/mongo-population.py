import os
from pymongo import MongoClient
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


connection_string = os.getenv("MONGO_CS")

try:
    # Connect to MongoDB Atlas
    client = MongoClient(connection_string, tlsAllowInvalidCertificates=True)
    db = client["formative_db"]  # must match exact db name with out mongo db name in the cloud
    collection = db["restaurant_customers"]

    df = pd.read_csv("restaurant_customer_satisfaction.csv")

    # Gender mapping
    gender_map = {"Male": 0, "Female": 1}

    # document preparation
    documents = []
    for _, row in df.iterrows():
        document = {
            "customer": {
                "customer_id": str(row["CustomerID"]),
                "age": row["Age"],
                "gender": gender_map[row["Gender"]],
                "income": float(row["Income"])
            },
            "visit": {
                "visit_frequency": row["VisitFrequency"],
                "average_spend": float(row["AverageSpend"]),
                "preferred_cuisine": row["PreferredCuisine"],
                "time_of_visit": row["TimeOfVisit"],
                "group_size": row["GroupSize"],
                "dining_occasion": row["DiningOccasion"],
                "meal_type": row["MealType"],
                "online_reservation": bool(row["OnlineReservation"]),
                "delivery_order": bool(row["DeliveryOrder"]),
                "loyalty_program_member": bool(row["LoyaltyProgramMember"]),
                "wait_time": float(row["WaitTime"]),
                "ratings": {
                    "service": row["ServiceRating"],
                    "food": row["FoodRating"],
                    "ambiance": row["AmbianceRating"]
                }
            },
            "satisfaction": bool(row["HighSatisfaction"]),
            "recorded_at": datetime.utcnow()
        }
        documents.append(document)

    # Insert all documents
    collection.insert_many(documents)
    print("MongoDB database populated successfully!")

except Exception as e:
    print(f"Error connecting to MongoDB or inserting data: {e}")

finally:
    # Close connection
    client.close()
    print("MongoDB connection closed.")
