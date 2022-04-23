from user import User
class Credentials:
    '''
    Class that generates new instances of user credentials
    '''
    credentials_list = [] #Empty credentials list
    
    def __init__(self,accountname,login_pass):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            accountname: Acount name 
            login key: Account password
        '''
        self.accountname = accountname
        self.login_pass = login_pass


    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credential_list
        '''
        Credentials.credentials_list.append(self)


    def delete_credentials(self):
        '''
        delete user method deletes user objects from users list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in an account_name and returns a credential that matches that name.

        Args:
            number: Account number to search for
        Returns :
            Name of account that matches the number.
        '''

        for credentials in cls.credentials_list:
            if credentials.accountname == name:
                return credentials


    #Returns the credentials list
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list





