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


