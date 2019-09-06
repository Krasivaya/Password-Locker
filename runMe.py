#!/usr/bin/env python3.6
from passwordLocker import User, Credentials #Importing user and credentials classes

def create_user(username,password):
    '''
    create_user method to create a new user
    '''
    new_user = User(username,password)
    return new_user
#The end!

def save_user(user):
    '''
    save_user method to save a user
    '''
    user.save_user()
#The end!

def display_user():
    """
    display_user method to display an existing user
    """
    return User.display_user()
#The end!
def signin_user(username,password):
    """
    signin_user method to check a user and then sign in they exist
    """
    check_user = Credentials.user_check_me(username,password)
    return check_user
#The End!

def create_credential(platform,email,password):
    """
    create_credential method to create new credentials
    """
    new_credential = Credentials(platform,email,password)
    return new_credential
#The end!

def save_credentials(credentials):
    """
    save_credentials method to save credentials in credentials_list
    """
    credentials. save_credentials()
#The end!