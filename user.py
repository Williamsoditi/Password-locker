class User:
    '''
    Class that generates new instances of users
    '''
    user_list = [] #Empty user list

    def __init__(self,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
        Username: User name
        Password: Account password
        '''
        self.username = username
        self.password = password
