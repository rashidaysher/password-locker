import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
       Test class that defines test cases for the contact class behaviours.

        Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Rashid", "rashid3590!") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Rashid")
        self.assertEqual(self.new_user.password,"rashid3590!")

    def test_signup_user(self): 
        '''
        test_signup_user test case to test if the object is initialized properly
        '''   

if __name__ =='__main__':
    unittest.main()
