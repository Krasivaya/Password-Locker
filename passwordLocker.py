class User:
    '''
    User class that generate new instances of users
    '''
    user_list = []
    # Empty object to hold user list

    def __init__(self,username,password):
        '''
        __init__ Method to define user properties (what to except from the user)
        '''
        self.username = username
        self.password = password
    #The end!

