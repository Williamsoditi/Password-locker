import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Instagram" , "Mambas25") # create a new credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.accountname,"Instagram")
        self.assertEqual(self.new_credentials.login_pass,"Mambas25")


if __name__ == '__main__':
    unittest.main()