# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:20:04 2021

@author: Admin
"""
from google_group import group_users, form_list, check_if_exists
from taiga_project import project_users, all_taiga_users

group_users = group_users()
project_users = project_users()
taiga_users = all_taiga_users()

if(group_users and project_users):
    users_to_add = form_list(project_users, group_users)
    
    for user in users_to_add:
        if not(check_if_exists(user, taiga_users)):
            print('kuku')
            #if user is not in taiga, register him first
            #add to project school
        else:
            print('exists')
            #user exists in taiga, add him to project school