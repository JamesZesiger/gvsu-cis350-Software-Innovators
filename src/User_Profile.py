from datetime import date

class LengthError(Exception):
    def __init__(self, *message):
        self.message = message
        super().__init__(self.message)

class User:
    def __init__(self, username: str, email: str, password: str):
        if type(username) != str or type(email) != str or type(password) != str: raise TypeError
        if len(password) < 8: raise LengthError("Password must be at least 8 characters")
        if len(username) < 3: raise LengthError("Username must be at least 3 characters")
        if '@' not in email or '.' not in email: raise TypeError("Invalid email")
        self.__username = str(username)
        self.__email = str(email)
        self.__password = str(password)
        self.__expenses = {}
        self.__experience = 0

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username:str):
        if len(new_username) < 3: raise LengthError("Username must be at least 3 characters")
        self.__username = new_username

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email: str):
        if '@' not in new_email or '.' not in new_email: raise TypeError("Invalid email")
        self.__email = str(new_email)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password: str):
        if len(new_password) < 8: raise LengthError("Password must be at least 8 characters")
        self.__password = str(new_password)

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, new_expenses: dict):
        self.__expenses = new_expenses

    def add_expenses(self, expense:float):
        if type(expense)!= float: raise TypeError
        self.__expenses[date.today()] = expense

    def remove_expenses(self, date):
        del self.__expenses[date]

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, new_experience: int):
        self.__experience = new_experience

    def add_experience(self, experience: int):
        self.__experience += experience

    def remove_experience(self, experience: int):
        self.__experience -= experience