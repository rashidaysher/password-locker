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
      self.new_account = Credentials("Instagram", "smart", "boss123", "Rashid")

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
      self.assertEqual(self.new_account.login,"smart")
      self.assertEqual(self.new_account.password,"boss123")
      self.assertEqual(self.new_account.user,"Rashid")

    def test_save_credential(self):  
      '''
        test_save_credentials method saves credential objects into credential_list
      ''' 
      self.new_account.save_credential()
      self.assertEqual(len(Credentials.credentials_list),3)    
        

    def test_save_multiple_credential(self):
      '''
            test_save_multiple_accounts to check if we can save multiple contact
            objects to our contact_list
      '''
      self.new_account.save_credential()
      test_account = Credentials("Test", "user", "29037218", "Rashid")
      test_account.save_credential()
      self.assertEqual(len(Credentials.credentials_list),5)

    

    def test_get_random_password(self): 
      '''
        test_save_credentials method saves credential objects into credential_list
      ''' 
      self.assertEqual(len(Credentials.get_random_password()),8)

    #  def test_delete_account(self):  
    #     '''
    #     delete_account method deletes a saved account from the credential_list
    #     ''' 
    #     self.new_account.save_credential()
    #     test_account = Credentials("Test", "user", "29037218")
    #     test_account.save_credential()
    #     self.new_account.delete_credentials()
    #     self.assertEqual(len(Credentials.credentials_list),2)

      
    def test_display_all_credential(self): 
      '''
        methos that returns a list of all credentials saved
      ''' 
      self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
      

    def test_find_account(self):
      '''
        delete_account method deletes a saved account from the credential_list
      ''' 
      self.new_account.save_credential()
      test_account = Credentials("Test", "user", "29037218", "Rashid")   
      test_account.save_credential()
      found_account = Credentials.find_by_account("Test")

      self.assertEqual(found_account.login,test_account.login)

if __name__ == '__main__':
        unittest.main()    





