# -*- coding: utf-8 -*-
from taiga import TaigaAPI

api = TaigaAPI(host='https://track.miem.hse.ru/')
api.auth(username='username',password='password')

def project_users():
    """
    Gets list of project users from taiga api, authorization token is provided    
    
    Returns
    -------
    List of users emails
    """    
    project_school = api.projects.get_by_slug('ps')    
    users_list = []
    for member in project_school.members:
        users_list.append(member.username + '@miem.hse.ru')
        
    #replaces some users usernames as they are different in taiga than in google groups 
    for user in range(len(users_list)):
        if (users_list[user] == 'DenisPalukha@miem.hse.ru'):
            users_list[user] = 'dvpalukha@miem.hse.ru'
        if (users_list[user] == 'Affid@miem.hse.ru'):
            users_list[user] = 'aafyodorov@miem.hse.ru'
            
    return users_list

def all_taiga_users():
    users = api.users.list()
    usernames = []
    for item in users:
        usernames.append(item.username + "@miem.hse.ru")
    
    for user in range(len(usernames)):
        if (usernames[user] == 'DenisPalukha@miem.hse.ru'):
            usernames[user] = 'dvpalukha@miem.hse.ru'
        if (usernames[user] == 'Affid@miem.hse.ru'):
            usernames[user] = 'aafyodorov@miem.hse.ru'
        if (usernames[user] == 'Beganov@miem.hse.ru'):
            usernames[user] = 'dvbeganov@miem.hse.ru'
        if (usernames[user] == 'DanilaPavlenko@miem.hse.ru'):
            usernames[user] = 'dnpavlenko@miem.hse.ru'
        if (usernames[user] == 'DariaY@miem.hse.ru'):
            usernames[user] = 'dayazovskaya@miem.hse.ru'
        if (usernames[user] == 'hseguest@miem.hse.ru'):
            usernames[user] = 'tdrykova@miem.hse.ru'
        if (usernames[user] == 'Irina.Bessonova@miem.hse.ru'):
            usernames[user] = 'iabessonova@miem.hse.ru'
        if (usernames[user] == 'Kamedvedev@miem.hse.ru'):
            usernames[user] = 'kamedvedev@miem.hse.ru'
        if (usernames[user] == 'kirfr@miem.hse.ru'):
            usernames[user] = 'kdfrolov@miem.hse.ru'
        if (usernames[user] == 'KirillMatanov@miem.hse.ru'):
            usernames[user] = 'kamatanov@miem.hse.ru'
        if (usernames[user] == 'SadLuntic@miem.hse.ru'):
            usernames[user] = 'mdkolodin@miem.hse.ru'
        if (usernames[user] == 'William@miem.hse.ru'):
            usernames[user] = 'vssargsyan@miem.hse.ru'
        if (usernames[user] == 'Nemnav@miem.hse.ru'):
            usernames[user] = 'vanemna@miem.hse.ru'
            
    return usernames