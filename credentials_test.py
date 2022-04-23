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


    #test to save credentials
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
        the contact list
        '''
        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.credentials_list),1)

    #Tear down method - Works awesome
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    #Test to save multiple credentials
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credential objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Facebook","outta") # New instance of credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

    #Test to delete credentials
    def test_delete_credentials(self):
            '''
            test_delete_credentials to test deletion of credentials
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Gmail","2022MyYear") # new credentials added
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting credentials
            self.assertEqual(len(Credentials.credentials_list),1)

    #Test to figure out credentials by name
    def test_find_credentials_by_name(self):
        '''
        test to check if we can find Credentials by accountname and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","cliqueMambas21") # new credentials
        test_credentials.save_credentials()

        found_credential= Credentials.find_by_name("Facebook")

        self.assertEqual(test_credentials.accountname,found_credential.accountname)
    
    #Test to display all credentials
    def test_display_all_credentials(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()