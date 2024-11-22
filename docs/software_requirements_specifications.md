# Overview
The purpose of this document is to list set functional and non-functional requirements for a budgeting application. The desktop application BalanceBuddy balances expenses, income, savings, and more. BalanceBuddy is targeted mainly at college students struggling to maintain their finances. BalanceBuddy features a gamified tracking system designed to maintain an active user base.
# Functional Requirements
1. User Profile
    1. Users shall be able to sign in to the existing profile
    2. Users shall be able to create a new profile
    3. User profile shall be able to update user name, password, and email
    4. User profiles shall store data related to the user locally
    5. User profile shall communicate and update information in the database 
2. Budget tracker
    1. Users shall be able to log their income
    2. Income tracker shall contain log date, name of income source, and an amount
    3. Income tacker shall calculate total income in the past week
    4. Users shall be able to log their expenses
    5. Expense tracker shall contain log date, name of expense source, and an amount
    6. Expense tacker shall calculate total expenditure in the past week
3. GUI
    1. The application shall use an intuitive easy to navigate UI
    2. The application shall use a unified color palette for all sections
    3. GUI shall have a dedicated page for each function 
4. Reward System
    1. Users shall receive EXP for using different features in the application daily
    2. The amount of EXP a user has shall determine the level of user
5. Database
    1. User information shall be stored on a database
    2. The database shall propagate the user profile for quick local access
# Non-Functional Requirements
1. Alerts
    1. Admins shall be able to post new events for all users
    2. Users Shall be able to receive notifications to log their daily income/expenses 
2. Online functions
    1. A leaderboard shall display global or friend rankings
    2. The leaderboard shall only display non-sensitive information such as level, EXP, or consecutive days using the app
    3. Users shall be able to send and receive friend requests 
3. Visual tracking
    1. Income tracker shall display recent or total income on a graph
    2. Expense tracker shall display recent or total expenses on a 
4. Security
    1. Password shall be hidden during log-in
    2. Data stored in the database shall be encrypted 
6. Functionality
    1. BalanceBuddy shall run on MacOS and Windows 11
    2. BalanceBuddy shall remember the logged-in user on startup
    3. BalanceBuddy shall have a quick-access menu that contains a link to all pages in the application 
