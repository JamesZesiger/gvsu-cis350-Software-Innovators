import User_Profile
import unittest
from datetime import date

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
        self.assertEqual(user.expenses,{date.today():{"gas":51.75}})
        user.add_expenses("loan",256.88)
        self.assertEqual(user.expenses,{date.today():{"gas":51.75,"loan":256.88}})
        user.remove_expenses(date.today(),("gas"))
        self.assertEqual(user.expenses,{date.today():{"loan":256.88}})
        user.remove_expenses(date.today())
        self.assertEqual(user.expenses,{})

    def test_experience(self):
        user = User_Profile.User("James", "zesigeja@mail.gvsu.edu", "password")
        user.experience = 1000
        self.assertEqual(user.experience, 1000)
        user.add_experience(50)
        self.assertEqual(user.experience, 1050)
        user.remove_experience(75)
        self.assertEqual(user.experience, 975)

if __name__ == '__main__':
    unittest.main()
