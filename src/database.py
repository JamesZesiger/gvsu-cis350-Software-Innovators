from pymongo import MongoClient

# MongoDB connection string (replace with your own if needed)
client = MongoClient("mongodb+srv://budgetUser:securePassword123@balancebuddy.r463f.mongodb.net/?retryWrites=true&w=majority&appName=BalanceBuddy")
db = client["BalanceBuddy"]
users_collection = db["users"]

# Function to register a new user
def register_user(username, password):
    # Check if username already exists
    if users_collection.find_one({"username": username}):
        print("Username already exists. Choose a different username.")
        return
    
    # Insert new user into the database
    user = {"username": username, "password": password}
    users_collection.insert_one(user)
    print("User registered successfully!")

# Function to login a user
def login_user(username, password):
    # Look for a user with matching username and password
    user = users_collection.find_one({"username": username, "password": password})
    if user:
        print("Login successful!")
    else:
        print("Invalid credentials.")

# Test the functions
# Register a test user
#register_user("testuser", "testpassword123")

# Attempt to login with the same credentials
login_user("testuser", "testpassword123")

# Attempt to login with incorrect credentials
login_user("testuser", "wrongpassword")
