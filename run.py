#!/usr/bin/env python3
from credentials import Credentials
from user import User
from termcolor import colored

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

def find_account(account):
    '''
    Function to find account
    '''  
    return Credentials.find_by_account(account) 

def main():
    print("Kindly register with us to enjoy our service")
    print(colored("Please input username", "yellow"))
    username = input()
    print (f"Hello {username}. Thank you for choosing passlock. input"), print (colored("password to continue:", "yellow"))
    print('\n')
    password = input()
    print(colored('\n', 'yellow'))
    print(colored("YOU HAVE SUCCESSFULLY REGISTERED TO PASS-LOCK", "green"))
    print ("*"*70, )

    newuser(username,password)

    while True:
        print ('\n')
        print (colored ("Use the words: create - create a new account, display - display every account, find - find account, exit - exit passlock", "blue"))

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
            print ("Input user name")
            uname = input() 
            print ("Input password")
            pword = input()  


            for user in User.user_list:
                if user.username == uname:
                    if user.password == pword:
                       if display_credentials():
                        print("Below are the list of all your accounts")
                        print ("\n")

                        for account in display_credentials():
                           print("i"*8)
                           print(f"Acconut: {account.account}")
                           print(f"Login: {account.login}")
                           print(f"Passsword: {account.password}")
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

        elif chosen_word == "exist":
            print("\n")
            print("Thank you for choosing passlock.")
            break
        else:
            print("\n")
            print("Invalit. PLease try again")
            print("\n")

if __name__ == '__main__':
    main()                    









