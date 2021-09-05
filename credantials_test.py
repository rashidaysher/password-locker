import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
     '''
       Test class that defines test cases for the contact class behaviours.

        Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     def setUp(self):
      """
      set up method to run before ech test case
      """
      self.new_account = Credentials("Instagram", "Aysher", "boss123")

     def tearDown(self):
       '''
        tearDown method that does clean up after each test case has run.
       '''
     Credentials.credentials_list = []

     def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account,"Instagram")
        self.assertEqual(self.new_account.login,"Aysher")
        self.assertEqual(self.new_account.password,"boss123")
        

     def test_save_multiple_accounts(self):
        '''
            test_save_multiple_accounts to check if we can save multiple contact
            objects to our contact_list
        '''
        self.new_account.save_credential()
        test_account = Credentials("Test", "user", "29037218")
        test_account.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)

     def test_save_credentials(self):  
        '''
        test_save_credentials method saves credential objects into credential_list
        ''' 
        self.new_account.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

     def test_gen_password(self): 
        '''
        test_save_credentials method saves credential objects into credential_list
        ''' 
        self.assertEqual(len(Credentials.get_random_password()),8)

     def test_delete_account(self):  
        '''
        delete_account method deletes a saved account from the credential_list
        ''' 
        self.new_account.save_credential()
        test_account = Credentials("Test", "user", "29037218")
        test_account.save_credential()
        self.new_account.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)



