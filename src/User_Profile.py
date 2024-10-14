class User:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__expenses = {}
        self.__experience = 0

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, new_expenses):
        self.__expenses = new_expenses

    def add_expenses(self, date, expense):
        self.__expenses[date] = expense

    def remove_expenses(self, date):
        del self.__expenses[date]

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, new_experience):
        self.__experience = new_experience

    def add_experience(self, experience):
        self.__experience += experience

    def remove_expenses(self, experience):
        self.__experience -= experience