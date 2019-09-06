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
    def setUp(self):
        '''
        setUp method to run before each test cases
        '''
        self.new_credential = Credentials('Email','semwagacarine@gmail.com','hideme')
    #The end!

    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.platform,'Email')
        self.assertEqual(self.new_credential.email,'semwagacarine@gmail.com')
        self.assertEqual(self.new_credential.password,'hideme')
    #The end!

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    #The end!

    def tearDown(self):
        '''
        tearDown method to clean up after each test has run
        '''
        Credentials.credentials_list = []
    #The end!

    def test_save_multiple_credentials(self):
        '''
        test_save_many_credentials test case to test if we can save multiple credentials at a time
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Email','semwagacarine@gmail.com','hideme')
        test_credential.save_credentials()

        self.assertEqual(len(Credentials.credentials_list),2)
    #The end!

    def test_delete_credentials(self):
        '''
        test_delete_credentials test case to test if we can remove a credential
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Email','semwagacarine@gmail.com','hideme')
        test_credential.save_credentials()
        
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    #The end!

if __name__ == '__main__':
    unittest.main()