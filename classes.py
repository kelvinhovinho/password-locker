import string
import random
import pyperclip

class User:
    """
    Class that generrates new instances of users
    """
    users_list = []

    def __init__(self,first_name,last_name,phone_number,email,username,password):
        """
        method to define properties for each user object
        """
        # Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    def save_user(self):
        '''
        Function to save a newly created user instance
        '''
        User.users_list.append(self)

    def delete_user(self):
        '''
        Function to delete user information
        '''
        User.users_list.remove(self)    

class Credentials:
    """
    Class that generrates new instances of users credentials
    """
    credential_list = []
    user_crediatials_list = []

    @classmethod
    def check_user(cls, username, password):
        '''
        Method that checks if the name and password entered match entries in the user_list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.username == username and user.password == password):
                current_user = user.username
                return current_user

    def __init__(self, user_name, site_name, password):
        '''
        Method to define the properties for each user object will hold.
        '''
        

        # instance variables
        self.user_name = user_name
        self.site_name = site_name
        self.password = password


    def save_credentials(self):
        '''
        Function to save user credentials
        '''

        Credentials.credential_list.append(self)

    def delete_credentials(self):
        '''
        Function to delete user credentials
        '''
        Credentials.credential_list.remove(self)

        
    @classmethod
    def rand_pass(cls,size): 
      
        # Takes random choices from 
        # ascii_letters and digits 
      
        generate_pass = ''.join([random.choice( string.ascii_letters + string.digits) for n in range(size)]) 
                          
        return generate_pass 

    @classmethod    
    def display_credentials(cls,user_name):
        '''
        Class method to display the list of credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credential_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        A method to search for credentials associated with a given account type.
        '''
        for credential in cls.credential_list:
            if credential.site_name == site_name:

                return credential
    
    @classmethod
    def copy_credentials(cls, site_name):
        '''
        Class method that copies a credential's info after the credential's account site is entered
        '''
        found_credential = cls.find_by_site_name(site_name)
        return pyperclip.copy(found_credential.password)


