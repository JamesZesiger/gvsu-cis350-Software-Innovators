from database import *
from User_Profile import User

"""
first call register_user or login_user from database to set User object
get info by calling User_Profile, call update_user_data(user) to sync back with the database
"""

test_email = "johndoe@example.com"
test_password = "securepassword"
test_username = "johndoe"

# Register a new user
print("=== Registering User ===")
register_user(test_email, test_password, test_username)

# Login and create User object
print("\n=== Logging In User ===")
user = login_user(test_email, test_password)
if user:
    print(f"Logged in as: {user.username}")

# Add expenses and sync with database
print("\n=== Adding Expenses ===")
# add using User_Profile class
user.add_expenses("Coffee", 5.50)
user.add_expenses("Lunch", 12.30)
# Sync with database
update_user_data(user)  

# Retrieve expenses from database
print("\n=== Retrieving Expenses ===")
get_all_expenses(user)
print("Current Expenses:", user.expenses)

# Add income and sync with database
print("\n=== Adding Income ===")
user.add_income("Freelancing", 1500.00)
update_user_data(user)  # Sync with database

# Retrieve income from database
print("\n=== Retrieving Income ===")
get_all_income(user)
print("Current Income:", user.income)

# Update user experience points and sync
print("\n=== Updating Experience Points ===")
user.add_experience(100)
update_user_data(user)  # Sync with database
