import User_Profile
import unittest
from datetime import date, timedelta

class Test_User_Profile(unittest.TestCase):
    def test_create_user_good(self):
        self.assertTrue(User_Profile.User("James","zesigeja@mail.gvsu.edu","password"))

    def test_create_user_bad_username(self):
        self.assertRaises(User_Profile.LengthError,lambda:User_Profile.User("Ja","zesigeja@mail.gvsu.edu","password"))
        self.assertRaises(TypeError,lambda:User_Profile.User(12345678,"zesigeja@mailgvsuedu","password"))

    def test_create_user_bad_email(self):
        self.assertRaises(TypeError, lambda: User_Profile.User("James", "zesigejamail.gvsu.edu", "password"))
        self.assertRaises(TypeError,lambda:User_Profile.User("James","zesigeja@mailgvsuedu","password"))
        self.assertRaises(TypeError,lambda:User_Profile.User("James",123456789,"password"))


    def test_create_user_bad_password(self):
        self.assertRaises(User_Profile.LengthError,lambda:User_Profile.User("James","zesigeja@mail.gvsu.edu","bad"))
        self.assertRaises(TypeError,lambda:User_Profile.User("James","zesigeja@mail.gvsu.edu",123456789))

    def test_get_and_set_username(self):
        user = User_Profile.User("James","zesigeja@mail.gvsu.edu","password")
        self.assertEqual(user.username,"James")
        user.username = "Connor"
        self.assertEqual(user.username, "Connor")

    def test_get_and_set_password(self):
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        self.assertEqual(user.password, "password")
        user.password = "password1"
        self.assertEqual(user.password, "password1")

    def test_get_and_set_email(self):
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        self.assertEqual(user.email, "zesigeja@mail.gvsu.edu")
        user.email = "speidelp@mail.gvsu.edu"
        self.assertEqual(user.email, "speidelp@mail.gvsu.edu")

    def test_expense(self):
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        user.add_expenses("gas",51.75)
        self.assertEqual(user.expenses,{date.today().strftime("%m/%d/%y"):{"gas":51.75}})
        user.add_expenses("loan",256.88)
        self.assertEqual(user.expenses,{date.today().strftime("%m/%d/%y"):{"gas":51.75,"loan":256.88}})
        user.remove_expenses(date.today().strftime("%m/%d/%y"),("gas"))
        self.assertEqual(user.expenses,{date.today().strftime("%m/%d/%y"):{"loan":256.88}})
        user.remove_expenses(date.today().strftime("%m/%d/%y"))
        self.assertEqual(user.expenses,{})

    def test_sum_expense(self):
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        m = date.today() - timedelta(days = date.today().isoweekday())
        t = m + timedelta(days = 1)
        w = t + timedelta(days = 1)
        th = w + timedelta(days = 1)
        f = th + timedelta(days = 1)
        sa = f + timedelta(days = 1)
        su = sa + timedelta(days = 1)
        user.expenses = {m.strftime("%m/%d/%y"):{"gift":100.00,"netflix":25.75},
                       t.strftime("%m/%d/%y"):{"groceries":150.70},
                       w.strftime("%m/%d/%y"):{"fast food":75.13,"tax":2.03},
                       th.strftime("%m/%d/%y"):{"rent":201.20},
                       f.strftime("%m/%d/%y"):{"amazon":10.80},
                       sa.strftime("%m/%d/%y"):{"amazon":3.00},
                       su.strftime("%m/%d/%y"):{"spotify":5.00}}
        total = user.sum_of_current_expenses()
        self.assertEqual(total, 573.61,"expenses sum, full week")
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        total = user.sum_of_current_expenses()
        self.assertEqual(total, 0, "expenses sum: empty dict")

    def test_experience(self):
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        user.experience = 1000
        self.assertEqual(user.experience, 1000)
        user.add_experience(50)
        self.assertEqual(user.experience, 1050)
        user.remove_experience(75)
        self.assertEqual(user.experience, 975)

    def test_income(self):
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        user.income = {date.today().strftime("%m/%d/%y"):{"work":250.00,"sales":25.25}}
        self.assertEqual(user.income,{date.today().strftime("%m/%d/%y"):{"work":250.00,"sales":25.25}})
        user.add_income("tax return",143.27)
        self.assertEqual(user.income,{date.today().strftime("%m/%d/%y"):{"work":250.00,"sales":25.25,"tax return":143.27}})
        user.remove_income("11/13/24","work")
        self.assertEqual(user.income,{date.today().strftime("%m/%d/%y"):{"sales":25.25,"tax return":143.27}})
        user.remove_income("11/13/24")
        self.assertEqual(user.income,{})

    def test_sum_income(self):
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        m = date.today() - timedelta(days = date.today().isoweekday())
        t = m + timedelta(days = 1)
        w = t + timedelta(days = 1)
        th = w + timedelta(days = 1)
        f = th + timedelta(days = 1)
        sa = f + timedelta(days = 1)
        su = sa + timedelta(days = 1)
        user.income = {m.strftime("%m/%d/%y"):{"Pay":100.00,"sales":25.75},
                       t.strftime("%m/%d/%y"):{"Pay":150.70},
                       w.strftime("%m/%d/%y"):{"Pay":75.13,"sales":2.03},
                       th.strftime("%m/%d/%y"):{"Pay":201.20},
                       f.strftime("%m/%d/%y"):{"Pay":10.80},
                       sa.strftime("%m/%d/%y"):{"sales":3.00},
                       su.strftime("%m/%d/%y"):{"sales":5.00}}
        total = user.sum_of_current_income()
        self.assertEqual(total, 573.61,"income sum, full week")
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        total = user.sum_of_current_income()
        self.assertEqual(total, 0, "income sum: empty dict")



if __name__ == '__main__':
    unittest.main()
