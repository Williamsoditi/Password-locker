class User:
    '''
    Class that generates new instances of users
    '''

    def __init__(self,password, username):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
        Username: User name
        Password: Account password
        '''
        
        self.password = password
        self.username = username