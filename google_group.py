# -*- coding: utf-8 -*-
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def group_users():
    
    """
    Gets users from google group given by its name,authorizes with oauth2
       
    Returns
    -------
    List of users emails, if response was successful, None in the other case
    """
    # oauth2 authorization
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.group']
    #needs already user-authorized token kept in token.json file
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    mail_list = []
    with build('admin', 'directory_v1', credentials=creds) as service:
        response = service.members().list(groupKey='ps@miem.hse.ru').execute()
        if response and 'members' in response:
            for item in response['members']:
                mail_list.append(item['email'])
            return mail_list
    return None
    
def form_list(project_users, group_users):
    """
    Creating the list of users which are in the google group but not in taiga project yet   

    Returns
    -------
    List of users to add to project
    """
    users_to_add = []
    for user in group_users:
        if not (check_if_exists(user,project_users)):
            users_to_add.append(user)
    return users_to_add

def check_if_exists(user,users_list):
    """
    Checking whether a user is in the list of users or not
    
    Returns
    -------
    True if user is in the list, false if not
    """
    for member in users_list:
        if (user == member):
            return True
    return False