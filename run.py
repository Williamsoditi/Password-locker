#!/usr/bin/env python3.8
from email.policy import default
import random, string, pyperclip
from user import User
from credentials import Credentials

def create_credentials(accountname,login_pass):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(accountname,login_pass)
    return new_credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def generate_loginkey():
    '''
    Function that generates a loginkey
    '''
    phrase = phrase = string.digits + string.ascii_lowercase + string.ascii_uppercase
    while True:
        try:
            length = int(input('Please enter a correct length of loginkey!'))
            loginkey = random.sample(phrase, length)

        except ValueError:
            print("This is not a valid number, Please input a valid number!")
            continue
        else:
            loginkey = ("".join(loginkey))
            return loginkey

def del_credentials(credentials):
    '''
    Function to delete credentials if not needed
    '''
    credentials.delete_credentials()

def find_credentials(accountname):
    '''
    Function that finds credentials by accountname and returns the specified credential
    '''
    return Credentials.find_by_name(accountname)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print('Welcome to PASSWORD-LOCKER !')
    print('Please select an option to continue')
    print('/n')
    while True:
        print("lg => to Login to your account")
        print("sg => to Sign-up and create an account.")
        short_form = input().lower()
        print('\n')
        if short_form == 'sg':
            
                            print("Enter UserName")
                            username = input()

                            print ("Enter Password")
                            password = input()
                            
                            print ("Confirm Password")
                            confirm_password = input()

                            while confirm_password != password:
                                print("Error! Passwords don't match! Kindly try again")
                                print("Enter a Password")
                                password = input()
                                print("Confirm Password")
                                confirm_password = input()
                            else :
                                print(f" Hello {username}!. Welcome to Password-Locker. Your account was created successfully!")
                                print('\n')
                                print("Please login to continue")
                                print("Enter Username")
                                entered_username = input()
                                print("Enter Password")
                                entered_password = input()
                            
                            while entered_username != username or entered_password != password:
                                print("Error! Invalid username or password. Please enter correct details")

                                print("Enter your Username")
                                entered_username = input()
                                print("Enter your Password")
                                entered_password = input()

                            else:
                                print(f"Welcome to your account @{username}")
                                while True:
                                    print("Please choose an option to continue")
                                    print("cc => to create new credentials")
                                    print("dc => to display credentials")
                                    print("cp => to copy credential details to clipboard")
                                    print("del => to delete account credentials")
                                    print("ex => to exit the application")
                                    short_form = input().lower()
                                    if short_form == 'cc':
                                        print("Enter account name")
                                        acc_name = input()

                                        while True:
                                            print("Use the codes to choose an option")
                                            print("el => to enter login key")
                                            print("gl => for a system generated key")
                                            print("ex => to exit the prompt")
                                            l_key = input().lower()
                                            print("\n")
                                            if l_key == 'el':
                                                print("Enter login key")
                                                log_key = input()
                                            elif l_key == 'gl':
                                                log_key = generate_loginkey()
                                                break
                                            elif l_key == 'ex':
                                                break
                                            else:
                                                print("Please check your input!")

                                        save_credentials(create_credentials(acc_name,log_key))
                                        print(f"Credentials for {acc_name} have been created and its login key is {log_key}")

                                    elif short_form == 'dc':
                                        if display_credentials():
                                            print("Find a list of your credentials below")
                                            print("\n")
                                            for credentials in display_credentials():
                                                print(f"{credentials.accountname} - {credentials.login_key}")
                                        else:
                                            print(":( You dont have any saved credentials yet!")

                                    elif short_form == 'cp':
                                        print("Enter account name whose credentials you want to copy!")
                                        accountname = input()
                                        account = find_credentials(accountname)
                                        pyperclip.copy(account.accountname)

                                    elif short_form == 'del':
                                        print("Enter account name you wish to delete")
                                        accountname = input()
                                        account = find_credentials(accountname)
                                        del_credentials(account)

                                    elif short_form == 'ex':
                                        print("Are you sure you want to EXIT !")
                                        print("y/n?")
                                        answer = input().upper()
                                        if answer == 'y':
                                            print("Your details will be autosaved for the next login!")
                                            break
                                        elif answer == 'n':
                                            print("Please choose an option to continue:'cc' to create new credentials,'del' to delete account credentials,'dc' to display credentials,'cp' to copy credential details to clipboard, 'ex' to exit the application")
                                            short_form = input().lower()
                                        else:
                                            print("Could not find that argument. Please choose the selected choices!")

        #Login section
        elif short_form == "lg":
            print("Enter your username")
            default_username = input()
            print("Enter your password")
            default_password = input()

            while default_password != "Mambas25" or default_username != "Williams":
                print("Error ! Wrong details,please countercheck")


    


if __name__ == '__main__':
    main()