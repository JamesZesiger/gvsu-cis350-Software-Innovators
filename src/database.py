from pymongo import MongoClient
from datetime import datetime
from User_Profile import User

# MongoDB connection string
client = MongoClient("mongodb+srv://budgetUser:securePassword123@balancebuddy.r463f.mongodb.net/?retryWrites=true&w=majority&appName=BalanceBuddy")
db = client["BalanceBuddy"]
users_collection = db["users"]

# Function to register a new user
def register_user(email, password, user_name):
    """
    Registers a new user in the database.
    """
    if users_collection.find_one({"email": email}):
        print("Email already exists. Choose a different email.")
        return None

    user_data = {
        "email": email,
        "password": password,
        "user_name": user_name,
        "experience_points": 0,
        "expenses": [],
        "income": []
    }
    users_collection.insert_one(user_data)
    print("User registered successfully!")
    return user_data

# Function to login a user and initialize the User object
def login_user(email, password):
    """
    Logs in a user by checking the database. If valid, returns a populated User object.
    """
    user_data = users_collection.find_one({"email": email, "password": password})
    if user_data:
        print("Login successful!")

        # Create a User object and populate it using setters
        user = User(
            username=user_data["user_name"],
            email=user_data["email"],
            password=user_data["password"]
        )
        user.experience = user_data.get("experience_points", 0)
        user.expenses = {expense["date"]: {expense["description"]: expense["amount"]} for expense in user_data.get("expenses", [])}
        user.income = {income["date"]: {income["description"]: income["amount"]} for income in user_data.get("income", [])}

        return user
    else:
        print("Invalid credentials.")
        return None

# Function to update user data in the database
def update_user_data(user):
    """
    Syncs the User object data back to the database.
    """
    user_data = {
        "user_name": user.username,
        "email": user.email,
        "password": user.password,
        "experience_points": user.experience,
        "expenses": [{"description": desc, "amount": amt, "date": date} 
                     for date, daily_expenses in user.expenses.items() 
                     for desc, amt in daily_expenses.items()],
        "income": [{"description": desc, "amount": amt, "date": date} 
                   for date, daily_income in user.income.items() 
                   for desc, amt in daily_income.items()]
    }
    users_collection.update_one(
        {"email": user.email},
        {"$set": user_data}
    )
    print("User data updated successfully!")

# Function to update User Object from database
def get_all_expenses(user):
    """
    Retrieves all expenses for a user from the database and updates the User object.
    """
    user_data = users_collection.find_one({"email": user.email})
    if user_data:
        expenses = user_data.get("expenses", [])
        user.expenses = {expense["date"]: {expense["description"]: expense["amount"]} for expense in expenses}
        print(f"Updated expenses for user '{user.username}' from database.")
    else:
        print("User not found.")

# Function to update User Object from database
def get_all_income(user):
    """
    Retrieves all income for a user from the database and updates the User object.
    """
    user_data = users_collection.find_one({"email": user.email})
    if user_data:
        income = user_data.get("income", [])
        user.income = {income_entry["date"]: {income_entry["description"]: income_entry["amount"]} for income_entry in income}
        print(f"Updated income for user '{user.username}' from database.")
    else:
        print("User not found.")









"""
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection string
client = MongoClient("mongodb+srv://budgetUser:securePassword123@balancebuddy.r463f.mongodb.net/?retryWrites=true&w=majority&appName=BalanceBuddy")
db = client["BalanceBuddy"]
users_collection = db["users"]

# Function to register a new user
def register_user(email, password, user_name, occupation):
    if users_collection.find_one({"email": email}):
        print("Email already exists. Choose a different email.")
        return
    
    user = {
        "email": email,
        "password": password,
        "user_name": user_name,
        "occupation": occupation,
        "experience_points": 0,
        "expenses": []
    }
    users_collection.insert_one(user)
    print("User registered successfully!")

# Function to login a user
def login_user(email, password):
    user = users_collection.find_one({"email": email, "password": password})
    if user:
        print("Login successful!")
        return user
    else:
        print("Invalid credentials.")
        return None

# Function to add an expense with a date
def add_expense(user, description, amount, date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    expense = {
        "description": description,
        "amount": amount,
        "date": date
    }
    users_collection.update_one(
        {"_id": user["_id"]},
        {"$push": {"expenses": expense}}
    )
    print(f"Expense '{description}' on {date} added successfully!")

# Function to delete an expense by description and date
def delete_expense(user, description, date):
    users_collection.update_one(
        {"_id": user["_id"]},
        {"$pull": {"expenses": {"description": description, "date": date}}}
    )
    print(f"Expense '{description}' on {date} deleted successfully!")

# Function to set experience points for a user
def set_experience_points(user, points):
    users_collection.update_one(
        {"_id": user["_id"]},
        {"$set": {"experience_points": points}}
    )
    print(f"Experience points set to {points} for user '{user['user_name']}'.")

# Function to get experience points for a user
def get_experience_points(user):
    updated_user = users_collection.find_one({"_id": user["_id"]})
    if updated_user:
        return updated_user.get("experience_points", 0)
    else:
        print("User not found.")
        return None

# Function to get all expenses for a user
def get_all_expenses(user):
    updated_user = users_collection.find_one({"_id": user["_id"]})
    if updated_user:
        expenses = updated_user.get("expenses", [])
        if expenses:
            print(f"Expenses for {user['user_name']}:")
            for expense in expenses:
                print(f"- {expense['description']}: ${expense['amount']} on {expense['date']}")
        else:
            print("No expenses found.")
    else:
        print("User not found.")

# Example usage
register_user("testuser@example.com", "testpassword123", "Test User", "Software Engineer")

user = login_user("testuser@example.com", "testpassword123")

if user:
    add_expense(user, "Coffee", 3.50, "2024-11-07")
    #add_expense(user, "Lunch", 10.60, "2024-11-06")
    get_all_expenses(user)
    delete_expense(user, "Coffee", "2024-11-07")
    set_experience_points(user, 100)
    print(f"Experience Points: {get_experience_points(user)}")
"""
