
import random

class Credentials:
    """
    Class that generates new instances of credentials

    Args:
       unittest.TestCase class helping in creating test class
    """
    credentials_list = []

    def __init__(self,account,login, password,user ):

        """
         __init__ method that helps us define properties for our objects

        Args:
            account: New user account for creating new passlock account
            login: New account login
            password: New sccount password

    
        """

        self.account = account
        self.login = login
        self.password = password
        self.user = user

    def save_credential(self):
        '''
        save_credential method to save credential contact
        '''
        Credentials.credentials_list.append(self)

    @classmethod
    def get_random_password(cls):
         """
        delete_credentials method returns the credentials
         """
         chars = '1234567890qwertyuioplkjhgfdsazxcvbnm[]*./?<>()%$#@!^'
         password = ''.join(random.choice(chars) for i in range(8))
       
    
         return password

        #  print("First Random Password is ", get_random_password())

    @classmethod
    def display_credentials(cls):
     """
    display_credentials method returns the credentials
    """
     return cls.credentials_list

    # @classmethod
    # def delete_credentials(cls):
    #   """
    #     delete_credentials method returns the credentials
    #   """
    #   return cls.credentials_list

    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in an acc name and returns an acc that matches that name.

        Args:
            account: account name to search for
        Returns :
            credentials of account that matches the account name
        '''

        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials 