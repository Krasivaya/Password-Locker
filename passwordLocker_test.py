import unittest # Importing unittest module
from passwordLocker import User # Importing user class from passwordLocker module

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
    