#!/usr/bin/env python3.8
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



if __name__ == '__main__':
    main()