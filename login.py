import os
from database import authLogin,authUser
def login():#Login screen
    global logged_in
    global loggedin_user
    global currentUserSettings
    if os.path.exists("cookie"):#If cookie exists, like from logging in from ImportantLinks
        if(authUser()[0]):
            print("Already logged in, please continue")
            return True
    currentUserSettings = dict()
    username = input("Enter in the username: ")
    pwd = input("Enter in the password: ")
    if (authLogin(username, pwd)>0):#AuthLogin has three returns:(-1,0,1)
        print("You have successfully logged in.\n")
        return True#Login successful
    else:
        print("Incorrect username / password, please try again.")
        exit = input("Would you like to exit (y/n): ")
        if(exit!="y"):#Allows you to exit login
            login()
    return False