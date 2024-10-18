# Use Case: Log Expense

**Actors:**
- User (initiator)

**Description:**
1. The user navigates to the "Log Expense" page from the dashboard.
2. The user inputs details about their expense, such as the amount, category, and date.
3. The system saves the expense entry into the user's profile and updates their budget status accordingly.
4. The system displays a confirmation that the expense is successfully logged.

**Pre-Conditions:**
- The user must be logged in (Requirement 1.1).
- The user must have an existing profile or create one before logging an expense (Requirement 1.2).

**Post-Conditions:**
- The user's budget is updated with the new expense entry.
- The system saves the expense information to the database (Requirement 5.1).
- The user earns experience points (EXP) for logging an expense (Requirement 4.1).

**Cross Reference:**
- Functional Requirements: 2.2 (Log Expense), 4.1 (Reward System), 5.1 (Database)
