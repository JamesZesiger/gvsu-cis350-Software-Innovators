from datetime import datetime, timedelta

class LengthError(Exception):
    """
    custom exception that raises when input does not match the minimum length
    """
    def __init__(self, *message):
        """
        constructor that sets an error message
        Parameters:
            message: message that is returned when LengthError is raised
        """
        self.message = message
        super().__init__(self.message)

class User:
    """
    Class that contains methods to initialize, set, and retrieve all information for a user

    Attributes: 
        - __username(str): name of user
        - __email(str): valid email for user
        - __password(str): password for user account, minimum of 8 characters
        - __expenses(dict): dictionary of expenses, key: date, item: expense log
        - __experience(int): value representing total experience earned
    """
    
    def __init__(self, username: str, email: str, password: str):
        """
        constructor for user profile
        Parameters: 
            - username: name of user
            - email: email of user
            - password: password of user account
        Raises:
            - TypeError
            - LengthError:
        """
        if type(username) != str or type(email) != str or type(password) != str: raise TypeError    # raises TypeError if parameters are nor str type
        if len(password) < 8: raise LengthError("Password must be at least 8 characters")           # raises LengthError if password does not meet minimum num of chars
        if len(username) < 3: raise LengthError("Username must be at least 3 characters")           # raises LengthError if username does not meet minimum num of chars
        if '@' not in email or '.' not in email: raise TypeError("Invalid email")                   # raises TypeError if email does not contain an '@' or '.'
        self.__username = str(username)
        self.__email = str(email)
        self.__password = str(password)
        self.__expenses = {}
        self.__experience = 0
        self.__income = {}

    @property
    def username(self):
        """
        Getter for __username
        Returns: __username
        """
        return self.__username

    @username.setter
    def username(self, new_username:str):
        """
        Setter for __username
        Parameters:
            - new_username: new name for user
        Raises: 
            - LengthError
        """
        if len(new_username) < 3: raise LengthError("Username must be at least 3 characters")       # raises LenghtError if new_username is < 3 chars
        self.__username = new_username

    @property
    def email(self):
        """
        Getter for __email
        Returns: __email
        """
        return self.__email

    @email.setter
    def email(self, new_email: str):
        """
        Setter for __email
        Parameters:
            - new_email: new user email
        Raises:
            - TypeError
        
        """
        if '@' not in new_email or '.' not in new_email: raise TypeError("Invalid email")           # raises TypeError if new_email does not contain an '@' or '.'
        self.__email = str(new_email)

    @property
    def password(self):
        """
        Getter for __password
        Returns: __password
        """
        return self.__password

    @password.setter
    def password(self, new_password: str):
        """
        Setter for __password
        Parameters:
            - new_password: new password for user
        Raises:
            - LengthError
        """
        if len(new_password) < 8: raise LengthError("Password must be at least 8 characters")        # raises LengthError if new_password does not meet minimum num of chars
        self.__password = str(new_password)

    @property
    def expenses(self):
        """
        Getter for __expenses
        Returns: __expenses
        """
        return self.__expenses

    @expenses.setter
    def expenses(self, new_expenses: dict):
        """
        Setter for __expenses
        Parameters:
            - new_expenses
        """
        self.__expenses = new_expenses

    def add_expenses(self, tag: str, expense:float):
        """
        method that adds expense entry
        Parameters:
            - expense: new expense entry
        Raises:
            - TypeError
        """
        if type(expense)!= float: raise TypeError            # raises TypeError if expense is not a float
        if datetime.now().strftime("%m/%d/%y %H:%M:%S") not in self.__expenses: self.__expenses[datetime.now().strftime("%m/%d/%y %H:%M:%S")] = {}
        self.__expenses[datetime.now().strftime("%m/%d/%y %H:%M:%S")][tag] = expense              # adds expense to __expenses with todays date as key
        self.add_experience(100)
        
    def remove_expenses(self, date, tag = None):
        """
        method that removes an entry from a specified date
        Parameters:
            - date: date to remove entry from
        """
        if not tag: 
            del self.__expenses[date]
        else: 
            del self.__expenses[date][tag]

    def sum_of_current_expenses(self):
        """
        method that calculates total expenses of current week (sunday - saturday)
        Returns:
            - total
        """
        day_pointer = datetime.now() - timedelta(days=6)

        for _ in range(7):
            formatted_date = day_pointer.strftime("%m/%d/%y")

            # Sum all expenses that match the current date
            day_expenses = sum(
                amount
                for key, expenses in self.__expenses.items()
                if key.startswith(formatted_date)  # Match keys that start with the date
                for amount in expenses.values()  # Sum all amounts for the date
            )        

            day_pointer += timedelta(days=1)                                                  # returns total rounded to nearest hundreth 
        return day_expenses                                                         # returns total rounded to nearest hundreth 


    @property
    def experience(self):
        """
        Getter for __experience
        Returns: __experience
        """
        return self.__experience

    @experience.setter
    def experience(self, new_experience: int):
        """
        Setter for __experience
        Parameters:
            - new_experience: new experience for user
        """
        self.__experience = new_experience

    def add_experience(self, experience: int):
        """
        method that adds specified amount of experience to user
        Parameters:
            - experience: int value to add to user experience
        """
        self.__experience += experience

    def remove_experience(self, experience: int):
        """
        method that removes specified amount of experience to user
        Parameters:
            - experience: int value to remove from user experience
        """
        self.__experience -= experience


    @property
    def income(self):
        """
        Getter for __income
        Returns: __income
        """
        return self.__income

    @income.setter
    def income(self, new_income: dict):
        """
        Setter for __income
        Parameters:
            - new_income
        """
        self.__income = new_income

    def add_income(self, tag: str, income:float):
        """
        method that adds income entry
        Parameters:
            - tag: label for income 
            - income: new income amount 
        Raises:
            - TypeError
        """
        if type(income)!= float: raise TypeError            # raises TypeError if expense is not a float
        if datetime.now().strftime("%m/%d/%y %H:%M:%S") not in self.__income: self.__income[datetime.now().strftime("%m/%d/%y %H:%M:%S")] = {}
        self.__income[datetime.now().strftime("%m/%d/%y %H:%M:%S")][tag] = income           # adds expense to __expenses with todays date as key
        self.add_experience(100)
    def remove_income(self, date, tag = None):
        """
        method that removes an entry from a specified date
        Parameters:
            - date: date to remove entry from
            - tag (optional): label to remove 
        """
        if not tag:                         # if tag not provided delete full entry at date
            del self.__income[date]
        else:                               # if tag provided delete entry at tag
            del self.__income[date][tag]
            
    def sum_of_current_income(self):
        """
        method that calculates total income of current week (sunday - saturday)
        Returns:
            - total
        """

        day_pointer = datetime.now() - timedelta(days=6)

        for _ in range(7):
            formatted_date = day_pointer.strftime("%m/%d/%y")

            # Sum all expenses that match the current date
            day_income = sum(
                amount
                for key, income in self.__income.items()
                if key.startswith(formatted_date)  # Match keys that start with the date
                for amount in income.values()  # Sum all amounts for the date
            )        

            day_pointer += timedelta(days=1)                                                  # returns total rounded to nearest hundreth 
        return day_income
