class Credentials:
    '''
    Class that generates new instances of user credentials
    '''
    def __init__(self,accountname,login_pass):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            accountname: Acount name 
            login key: Account password
        '''
        self.accountname = accountname
        self.login_key = login_pass