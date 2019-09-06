#!/usr/bin/env python3.6
from passwordLocker import User, Credentials #Importing user and credentials classes

def create_user(username,password):
    '''
    create_user method to create a new user
    '''
    new_user = User(username,password)
    return new_user