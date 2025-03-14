# DATABSE DESIGN FORMATIVE (PEER GROUP 2)

## Task 1: Database Design and Schema
Contributor: Glen Miracle
Responsibilties:
The following are the main things I was responsible for:
- Database Creation
- Entity Relation Diagram
- Database Schema design
- Seeding Scripts
- Creating Mongodb clusters and db's
- deploying databases

## Task 2:  APIs
Contributor: Jordan Nguepi
-created api for all CRUD operations on the 3 data models
---
`Data Models`
Customer, Visit, Satisfaction

 api address:
`https://db-design-formative.onrender.com/api/'  

available endpoint: 
---
`api/customers/`
methods: LIST, CREATE, UPDATE, DELETE
---
`api/visits/`
methods: LIST, CREATE, UPDATE, DELETE
---
`api/satisfactions/`
methods: LIST, CREATE, UPDATE, DELETE

![Alt text](api_directory/Screenshot%20from%202025-03-13%2018-22-45.png)

---
## **Task 3 - Fetching Data & Predicting Customer Satisfaction**  
**Contributor:** Peter Johnson  

### **Responsibilities**  
In this project, I handled Task 3, which involved:  
- Fetching the latest customer data from the API  
- Preprocessing the data (categorical encoding, feature scaling)  
- Loading and using a trained neural network model to predict customer satisfaction  

### **Key Steps Implemented**  
1. **API Integration**  
   - Connected to the Django API to retrieve the most recent customer entry  
   - Extracted the last entry 

2. **Data Preprocessing**  
   - Standardized numerical features with Feature Scaling  

3. **Model Deployment**  
   - Trained and used a neural network model (Best Model From Intro To ML)  
   - Loaded `trained_customer_satisfaction_model.keras` for predictions  

4. **Database Logging**  
   - Logged predictions into the PostgreSQL database  

### **Technologies Used**  
- Python  
- TensorFlow/Keras  
- Django REST Framework  
- PostgreSQL  
- Scikit-Learn  

### **Repository Structure**  
- `db_directory/`→ Database Schema and tables
- `api_directory/` → Django API  
- `ml-directory/` → ML model & and predictions
- `Task_3_PETER_JOHNSON.ipynb` → Task 3 implementation  
- `trained_customer_satisfaction_model.keras` → Trained model  



