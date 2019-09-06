#!/usr/bin/env python3.6
from passwordLocker import User, Credentials # Importing user and credentials classes

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

def display_credentials():
    """
    display_credentials method to display user's credentials.
    """
    return Credentials.display_credentials()
#The end!

def delete_credential(credentials):
    """
    delete_credential method to delete a credential from credentials list

    """
    credentials.delete_credentials()
#The end!

def find_credential(platform):
    """
    find_credential method to find credentials by the platform name and return the credentials that belong to that platform
    """
    return Credentials.find_credentials(platform)
#The end!

def check_credentials(platform):
    """
    check_credentials method to check if credentials already existed inside that platform and return true or false

    """
    return Credentials.credential_exists(platform)
#The end!

def new_Password():
    '''
    new_password method to generate a new password
    '''
    auto_password = Credentials.new_password()
    return auto_password
#The end!

def copy_credentials(platform):
    """
    copy_credentials class to be able to copy credentials to the clipboard
    """
    return Credentials.copy_credentials(platform)
#The end!

def passwordLocker():
    print("Welcome to Password Locker...\n Please enter one of the following code to proceed.\n CA ---  Create New Account  \n SI ---  Sign In Your Account  \n")
    
    short_code = input("").lower().strip() 
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
    elif short_code == "si":
        pass
    else:
        print("Please enter a valid code to continue")


if __name__ == '__main__':
    passwordLocker()

#The End of PASSWORD LOCKER!