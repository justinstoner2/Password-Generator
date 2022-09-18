import random
import os

from fileaccesslib import *

password_dict = {}



active = True
while active==True:
    print("Menu")
    print("1: create new password")
    print("2: change password")
    print("3: delete password")
    print("4: view all passwords")
    print("5: Quit")
    menu_selection = input("Enter number 1 - 5: ")
    if menu_selection == '1':
        newPassword()
    if menu_selection == '2':
        change_password()
    if menu_selection =='3':
        delete_password()
    if menu_selection =='4':
        print_passwords()
    if menu_selection =='5':
        break
    else:
        pass

