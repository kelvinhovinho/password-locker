import string
import random
import pyperclips
class User:
    '''
    classs that generate new interface of user 
    ''' 

    user_list=[]

    def _init_(self,user_name,password):
        self,user_name=user_name
        self,password=password
    
    def save_user(self):
    '''
    save_user method saves new user objects to the user_list
    ''' 
    User.user_list.append(self)

    def delete_user(self):
        '''
        function to delete user information
        '''

class credentials:
    '''
    class to create an account password and save the information
    '''
    credentials_list=[]
    user_credentials_list=[]
    @classmethod
    def check_user(cls,user_name,password)
