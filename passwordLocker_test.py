import unittest # Importing unittest module
from passwordLocker import User # Importing user class from passwordLocker module
from passwordLocker import Credentials #Importing credentials class from passwordLocker module

class TestUser(unittest.TestCase):
    '''
    TestUser class to define test cases for the user class behaviours
    '''
    def setUp(self):
        '''
        setUp method to run before each test cases
        '''
        self.new_user = User('Carine','hideme') # Create user object
    #The end!
    
    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'Carine')
        self.assertEqual(self.new_user.password,'hideme')
    #The End!
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    #The end!
#The End with TestUser class

class TestCredentials(unittest.TestCase):
    '''
    TestCredentials class to define test cases for the credentials class behaviours
    '''

if __name__ == '__main__':
    unittest.main()