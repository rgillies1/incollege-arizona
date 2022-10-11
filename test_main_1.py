#import pytest
import main
from tud_test_base import get_display_output, set_keyboard_input
import os

def clearUserList():
  os.remove("userList.txt")
  f = open("userList.txt", "x")
  f.close()
  
def test_main_exit():
  set_keyboard_input(["Exit"])
  main.main()

  output = get_display_output()
  assert output == [
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup",
    "\nLogin | Signup: "
                   ]

def test_mass_signup():#Attempts to signup 6 accounts, only 5 work
  clearUserList()
  set_keyboard_input(["Signup","Dominos", "Dominos@2", "Dominos@2" , "Signup","Popeyes", "Popeyes@2", "Popeyes@2", "Signup", "Pizzahut", "Pizzahut@2", "Pizzahut@2", "Signup", "Starbucks", "Starbucks@2", "Starbucks@2", "Signup", "Dunkins", "Dunkins@2", "Dunkins@2","Signup","Exit"])
  main.main()
  expectedOut = ["Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup",
    "\nLogin | Signup: ",
     "Enter a username: ",
    "\nBefore entering a password, make sure it is between 8 and 12 characters long. Must include at least one capital letter, at least one digit, and at least one special chracter('$', '@', '#', '!', '%', '^', '&', '*')!\n",
    "Enter a password: ",
    "Confirm the password: ",
    "You have successfully signed up to InCollege!"]*5
  expectedOut+=["Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup",
    "\nLogin | Signup: ",
    "ERROR: All permitted accounts have been created, please come back later",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup",
    "\nLogin | Signup: "]
  #print(expectedOut)
  output = get_display_output()
  assert output == expectedOut


#Test login functions, successful login and unsuccessful ones(One incorrect username and one incorrect password)

def test_main_login():#
  set_keyboard_input(["Login","Dominos","Dominos2","Domnos","Dominos2","Dominos","Dominos@2","4","Exit"])
  main.main()
  output = get_display_output()
  expectedOut = ["Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup",
    "\nLogin | Signup: ","Enter in the username: ","Enter in the password: ","Incorrect username / password, please try again.","Enter in the username: ","Enter in the password: ","Incorrect username / password, please try again.","Enter in the username: ","Enter in the password: ","You have successfully logged in.\n","1. Search for a job \n2. Find someone you know \n3. Learn a new skill","\nPlease select a option from the list above: ","Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup",
    "\nLogin | Signup: "]
  assert output == expectedOut
   
  # test function for checkPassword
  #check if it contains a digit/special charecters/atleast 8 charecters
def test_checkPassword():
  clearUserList()
  set_keyboard_input(["Signup","Dominos", "dom", "dom" ,"dom","Dominos2@1234","Dominos2@1234", "Dominos","Dominos2@","Dominos2@","Exit"])
  expectedOut = ["Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup",
    "\nLogin | Signup: ",
     "Enter a username: ",
    "\nBefore entering a password, make sure it is between 8 and 12 characters long. Must include at least one capital letter, at least one digit, and at least one special chracter('$', '@', '#', '!', '%', '^', '&', '*')!\n",
    "Enter a password: ",
    "Confirm the password: ",
  "Password must have at least 8 characters.",
  "Password must contain a digit.",
  "Password must contain one upper.",
  "Password must contain a special character.",
  "ERROR: Please ensure that the password follows all the requirements!",
   "Enter a username: ",
    "\nBefore entering a password, make sure it is between 8 and 12 characters long. Must include at least one capital letter, at least one digit, and at least one special chracter('$', '@', '#', '!', '%', '^', '&', '*')!\n",
    "Enter a password: ",
    "Confirm the password: ",
    "Password must be less than 12 characters.",
    "ERROR: Please ensure that the password follows all the requirements!",
   "Enter a username: ",
    "\nBefore entering a password, make sure it is between 8 and 12 characters long. Must include at least one capital letter, at least one digit, and at least one special chracter('$', '@', '#', '!', '%', '^', '&', '*')!\n",
    "Enter a password: ",
    "Confirm the password: ",
    "You have successfully signed up to InCollege!","Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup",
    "\nLogin | Signup: "]
  main.main()
  output = get_display_output()
  assert output == expectedOut

#checks if the landing page and the new skills function is working correctly
def test_landingPage_newSkill():
  set_keyboard_input(["Login","Dominos", "Dominos2@", "1", "3", "1", "6", "4", "Exit"])
  expectedOut = ["Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup",
    "\nLogin | Signup: ",
    "Enter in the username: ", "Enter in the password: ", "You have successfully logged in.\n", "1. Search for a job \n2. Find someone you know \n3. Learn a new skill", "\nPlease select a option from the list above: ",  "\nThis feature is under construction!", "1. Search for a job \n2. Find someone you know \n3. Learn a new skill", "\nPlease select a option from the list above: ", "1. Study Habits \n2. Creative Thinking \n3. Critical Thinking \n4. Work/School Life Balance \n5. Scheduling \n6. return back to landing page", "Please select a skill you would like to learn: ","This feature is under construction", "1. Study Habits \n2. Creative Thinking \n3. Critical Thinking \n4. Work/School Life Balance \n5. Scheduling \n6. return back to landing page", "Please select a skill you would like to learn: ", "1. Search for a job \n2. Find someone you know \n3. Learn a new skill", "\nPlease select a option from the list above: ", "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup", "\nLogin | Signup: "]
  main.main()
  output = get_display_output()
  assert output == expectedOut
  
  
  
