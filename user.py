class User:
    """
    Class that generates new instances of user.
    """
user_list = []

def __init__(self,username, password):

    """
    __init__ method that helps us define properties for our objects

     Args:
     username: New user username
     password: New user password
     """
    self.username = username
    self.password = password

    def signup_user(self):

         """
         Function to signup users
         """
         User.user_list.append(self)
