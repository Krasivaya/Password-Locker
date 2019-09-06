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