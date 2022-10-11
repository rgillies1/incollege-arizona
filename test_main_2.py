#import pytest

import main
from tud_test_base import get_display_output, set_keyboard_input
import os

def clearFile(fileName):
  os.remove(fileName)
  f = open(fileName, "x")
  f.close()
  
def test_main_and_video_then_exit():#Display the new login space
  set_keyboard_input(["Video","Exit"])
  main.main()
  
  output = get_display_output()
  assert output == [
    "*************************************************************",
    "*  \"InCollege has helped me throughout my whole journey -   *",
    "*  whether it be developing skills, making connections,     *",
    "*  or even landing my first job, InCollege has been there   *",
    "*  to support me every step of the way with its simple yet  *",
    "*  engaging design.\"                                        *",
    "*                                                           *",
    "*                     - Quandale Dingle                     *",
    "*************************************************************",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video: ",
    "Video is now playing...\n",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video","\nLogin | Signup | Video: ",
                   ]

def test_mass_signup_updated():#Attempts to signup 6 accounts, only 5 work, names now included
  clearFile("userList.txt")
  set_keyboard_input(["Signup","Dominos", "Dominos@2", "Dominos@2","Mohammed","Haque", "Signup","Popeyes", "Popeyes@2", "Popeyes@2", "David", "Hamilton","Signup", "Pizzahut", "Pizzahut@2", "Pizzahut@2", "John", "Ha", "Signup", "Starbucks", "Starbucks@2", "Starbucks@2", "Arthur","Gusmao De Almeida","Signup", "Dunkins", "Dunkins@2", "Dunkins@2","Raymond","Gillies","Signup","Exit"])
  main.main()
  expectedOut = ["*************************************************************",
    "*  \"InCollege has helped me throughout my whole journey -   *",
    "*  whether it be developing skills, making connections,     *",
    "*  or even landing my first job, InCollege has been there   *",
    "*  to support me every step of the way with its simple yet  *",
    "*  engaging design.\"                                        *",
    "*                                                           *",
    "*                     - Quandale Dingle                     *",
    "*************************************************************"]
  expectedOut+=["Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video: ",
     "Enter a username: ",
    "\nBefore entering a password, make sure it is between 8 and 12 characters long. Must include at least one capital letter, at least one digit, and at least one special chracter('$', '@', '#', '!', '%', '^', '&', '*')!\n",
    "Enter a password: ",
    "Confirm the password: ",
    "Enter your first name: ",
    "Enter your last name: ",
    "You have successfully signed up to InCollege!"]*5
  expectedOut+=["Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video: ",
    "ERROR: All permitted accounts have been created, please come back later",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video: "]
  #expectedOut)
  output = get_display_output()
  assert output == expectedOut



def test_connect_users():#Test the connect uses function and inviting option
  set_keyboard_input(["Login","Dominos","Dominos@2","2","David","Hamilton","y","Walter","White","n","y","Bob","f","y","Exit"])
  main.main()
  output = get_display_output()
  expectedOut = ["*************************************************************",
    "*  \"InCollege has helped me throughout my whole journey -   *",
    "*  whether it be developing skills, making connections,     *",
    "*  or even landing my first job, InCollege has been there   *",
    "*  to support me every step of the way with its simple yet  *",
    "*  engaging design.\"                                        *",
    "*                                                           *",
    "*                     - Quandale Dingle                     *",
    "*************************************************************",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video: ","Enter in the username: ","Enter in the password: ","You have successfully logged in.\n","Mohammed Haque","1. Search for a job/internship \n2. Find someone you know \n3. Learn a new skill","\nPlease select a option from the list above: ","\nFind Someone You Know","Enter a first and last name and we'll let you know if they're on InCollege!", "Enter their first name: ","Enter their last name: ", "They are a part of the InCollege system!", "Would you like to search for another person? (y/n): ","Enter their first name: ","Enter their last name: ","Contact found but they are not yet part of the InCollege system","Would you like to invite contact? \nYou will be logged out. (y/n): ","Would you like to search for another person? (y/n): ","Enter their first name: ","Enter their last name: ", "They are not yet a part of the InCollege system yet!", "Would you like to invite contact? \nYou will be logged out. (y/n): ",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video: "]
  assert output == expectedOut
   
#Test Job Posting Creation 
def test_job_posting():
  clearFile("jobList.txt")
  set_keyboard_input(["Login","Dominos","Dominos@2","1","2","Intern","you intern","Big Inc","Tampa Fl","$15/hour","2","Cook","you cook","Cookers Inc","Tampa Fl","$12/hour","2","Intern","you intern","Big Inc","Tampa Fl","$15/hour","2","Cook","you cook","Cookers Inc","Tampa Fl","$12/hour","2","Intern","you intern","Big Inc","Tampa Fl","$15/hour","2","1","1","9","4","Exit"])
  expectedOut = ["*************************************************************",
    "*  \"InCollege has helped me throughout my whole journey -   *",
    "*  whether it be developing skills, making connections,     *",
    "*  or even landing my first job, InCollege has been there   *",
    "*  to support me every step of the way with its simple yet  *",
    "*  engaging design.\"                                        *",
    "*                                                           *",
    "*                     - Quandale Dingle                     *",
    "*************************************************************",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video: ","Enter in the username: ","Enter in the password: ","You have successfully logged in.\n","Mohammed Haque","1. Search for a job/internship \n2. Find someone you know \n3. Learn a new skill","\nPlease select a option from the list above: ","1. Job Board \n2. Post a job \n9. Back","Please select an option from the list above: ","Enter job title: ","Enter job description: ","Enter job employer: ","Enter job location: ","Enter job's salary: ","1. Job Board \n2. Post a job \n9. Back","Please select an option from the list above: ","Enter job title: ","Enter job description: ","Enter job employer: ","Enter job location: ","Enter job's salary: ","1. Job Board \n2. Post a job \n9. Back","Please select an option from the list above: ","Enter job title: ","Enter job description: ","Enter job employer: ","Enter job location: ","Enter job's salary: ","1. Job Board \n2. Post a job \n9. Back","Please select an option from the list above: ","Enter job title: ","Enter job description: ","Enter job employer: ","Enter job location: ","Enter job's salary: ","1. Job Board \n2. Post a job \n9. Back","Please select an option from the list above: ","Enter job title: ","Enter job description: ","Enter job employer: ","Enter job location: ","Enter job's salary: ","1. Job Board \n2. Post a job \n9. Back","Please select an option from the list above: ", "ERROR: Job board full, please try again later", "1. Job Board \n2. Post a job \n9. Back","Please select an option from the list above: ","1. Intern","2. Cook","3. Intern","4. Cook","5. Intern","9. Back","Select one of the jobs to view its details: ","\nJob Title: Intern\n","Job Description: you intern\n","Job Employer: Big Inc\n","Job Location: Tampa Fl\n","Job Salary: $15/hour\n","1. Job Board \n2. Post a job \n9. Back","Please select an option from the list above: ","1. Search for a job/internship \n2. Find someone you know \n3. Learn a new skill","\nPlease select a option from the list above: ",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video: "]
  main.main()
  output = get_display_output()
  assert output == expectedOut

  
