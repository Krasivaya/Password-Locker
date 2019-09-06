class User:
    '''
    User class that generate new object of users
    '''
    user_list = []
    # Empty object to hold new user

    def __init__(self,username,password):
        '''
        __init__ Method to define user properties (what to except from the user)
        '''
        self.username = username
        self.password = password
    #The end!

    def save_user(self):
        '''
        save_user method to save a new user to user_list 
        '''
        User.user_list.append(self)
    #The end!

    @classmethod
    def display_user(cls):
        '''
        display_user method to display user_list
        '''
        return cls.user_list
    #The end!

    def delete_user(self):
        '''
        delete_user method to delete a user stored in user_list
        '''
        User.user_list.remove(self)
    #The End!
#The End of User Class!
class Credentials:
    '''
    Credentials class to create new objects of Credentials
    '''
    credentials_list = []
    # Empty object to hold new credentials

    def __init__(self,platform,email,password):
        '''
        __init__ Method to define credentials properties
        '''
        self.platform = platform
        self.email = email
        self.password = password
    #The End!

    def save_credentials(self):
        '''
        save_credentials class to save and store new credentials into credentials_list
        '''
        Credentials.credentials_list.append(self)
    #The end!
    
    def delete_credentials(self):
        '''
        delete_credentials class to remove credential ffrom credentials_list
        '''
        Credentials.credentials_list.remove(self)
    #The end!

    @classmethod
    def find_credentials(cls, platform):
        '''
        find_credentials class to find credentials and display their information
        '''
        for crede in cls.credentials_list:
            if crede.platform == platform:
                return crede
    #The end!

    @classmethod
    def credential_exists(cls, platform):
        '''
        credential_exists class to check if credentials already exists
        '''
        for crede in cls.credentials_list:
            if crede.platform == platform:
                return True
        return False



