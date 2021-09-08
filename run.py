#!/usr/bin/env python3.8
from credentials import Credentials
from user import User
from termcolor import colored
# import pyperclip

def create_account(account, login, password, user):
    '''
    Function to create a new account
    '''
    new_credential = Credentials(account, login, password, user)
    return new_credential

def newuser(uname, pword):
    '''
    Function to create a new user
    '''  
    new_user = User(uname, pword) 
    new_user.signup_user()

def save_account(credentials):
    '''
    Function to save  a new account
    '''  
    credentials.save_credential()

def generate_password():
    '''
    Function to generate a new random password
    ''' 
    return Credentials.get_random_password()

def display_credentials():
    '''
    Function to display new credential details
    ''' 
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a credential

    """
    credentials.delete_credentials()


def find_account(account):
    '''
    Function to find account
    '''  
    return Credentials.find_by_account(account) 


def main():
    print("Kindly register with us to enjoy our service")
    print(colored("Please input username", "yellow"))
    username = input()
    print (colored(f"Hello {username}. Thank you for choosing passlock. input","green"), colored("password to continue:", "yellow"))
    print('\n')
    password = input()
    print(colored('\n', 'yellow'))
    print(colored("YOU HAVE SUCCESSFULLY REGISTERED TO PASS-LOCK", "green"))
    print ("*"*100, )

    newuser(username,password)

    while True:
        print ('\n')
        print (colored ("Use the words: \n create- create a new account, \n display - display every account, \n find - find account, \n dele - delete accounts, \n exit - exit passlock", "blue"))

        chosen_word = input().lower()

        if chosen_word == 'create':
            print(colored("Add a new account", "yellow"))
            print("_"*8)

            print(colored("Enter account name or application name:", "yellow") )
            account = input()

            print(colored("Input the username or login", "yellow"))
            login = input()

            while True:
                print("Generate password? (y/n)",)
                answer= input().lower()

                if answer == "y":
                    password = generate_password()

                    print(colored(f"Your new password is {password}", "green"))
                    print("your account credentials has been successfully created and saved")
                    break
                elif answer == "n":
                    print("\n")
                    print("Choose a password::")
                    password = input()
                    print("*"*70)

                    break
                else:
                    print("\n")
                    print("Password required. Try again.")
                    print (f"Hello {username}, your account has been created successfully")
                    print("*"*70)


            save_account(create_account(account, login, password, username))  
        elif chosen_word == "display":
            print (colored("Input user name", "yellow"))
            uname = input() 
            print (colored("Input password", "yellow"))
            pword = input()  


            for user in User.user_list:
                if user.username == uname:
                    if user.password == pword:
                       if display_credentials():
                        print(colored("Below are the list of all your accounts", "green"))
                        print ("\n")

                        for account in display_credentials():
                           print("*"*50)
                           print(colored(f"Acconut: {account.account}", "red"))
                           print(colored(f"Login: {account.login}", "red"))
                           print(colored(f"Passsword: {account.password}","red"))
                    else:
                      print("\n")
                      print("You seem to have no saved accounts yet")
                      print("\n") 


        elif chosen_word == 'find':
            print("\n")  
            print("Input account name")
            accname = input()

            if find_account(accname):
                    found_account = find_account(accname) 
                    print("_"*8)
                    print(f"Acconut {found_account.account}")
                    print(f"Login {found_account.login}")
                    print(f"Password {found_account.password}")


        elif chosen_word == "dele":
            print("Enter the account name of the Credentials you want to delete")
            accname = input().lower()
            if find_account(accname):
                found_account = find_account(accname)
                print("_"*50)
                found_account.delete_credentials()
                print('\n')
                print(colored(f"Your stored credentials for : {found_account.account} has been deleted successfully!!!", "green"))
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")  


            # ~         

        elif chosen_word == "exit":
            print("\n")
            print(colored("Come again and Thank you for choosing passlock.", "green"))
            break
        else:
            print("\n")
            print("Invalit. PLease try again")
            print("\n")

if __name__ == '__main__':
    main()                    









