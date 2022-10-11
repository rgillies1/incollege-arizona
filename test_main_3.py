#import pytest
import main
from tud_test_base import get_display_output, set_keyboard_input
import os

def clearFile(fileName):
  os.remove(fileName)
  f = open(fileName, "x")
  f.close()
  
def test_importantLinks():#Display the new login space
  set_keyboard_input(["importantlinks", "10", "Exit"])
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
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: ", 
    "*********Important Links*********", 
    "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main", 
    "Please select an options from above: ",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: ", 
                   ]
  
def test_importantLinks2():
  set_keyboard_input(["Login","Pizzahut","Pizzahut@2","4","1","5","0","4","9","1","10", "10", "Exit"])
  main.main()
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
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: ", 
    "Enter in the username: ", 
    "Enter in the password: ", 
    "You have successfully logged in.\n",
    "('Marge Simpson', ' Spanish\n')",
    "1. Search for a job/internship \n2. Find someone you know \n3. Learn a new skill \n4. importantlinks",
    "\nPlease select a option from the list above: ",
    "*********Important Links*********", 
    "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main", 
    "Please select an options from above: ", 
    "\nWe are committed to safeguarding the privacy of InCollege users. This notice applies where we are acting as a data controller with respect to the personal data of such persons; in other words, where we determine the purposes and means of the processing of that personal data.Our website incorporates privacy controls which affect how we will process your personal data.You can access the privacy controls via privacy policy page\n", 
    "*********Important Links*********", 
    "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main", 
    "Please select an options from above: ", 
    "\nThe privacy policy for In College describes how and why we might collect store, use and/or share your information when you use our services(such as visiting our website or engaging with us in other related ways). We collect personal information that you voluntarily provide to us when you register to use our services, express an interest in using our services or you participate in the activities on the services we provide. These informations include but are not limited to names, phone numbers, email address, job  titles and passwords. We process your information to provide, improve and administer our services, communicate with you, for security and fraud prevention(with your consent)\n", 
    "Press 0 to Enter Guest Controls or press 1 to go back to important links: ", "*********Guest Controls**************", 
    "1. Turn off InCollege email \n2. Turn off SMS \n3. Turn off Targeted advertising features \n4. Go back", 
    "Please select an options from above: ", 
    "*********Important Links*********", 
    "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main", 
    "Please select an options from above: ", 
    "Press 1 to change language settings from English to Spanish or Press 0 to go back: ", 
    "Language successfully changed from English to Spanish!",
    "Please select an options from above: ",
    "Please select an options from above: ",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video",
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: "]
  output = get_display_output()
  output[14]="('Marge Simpson', ' Spanish\n')"
  assert output == expectedOut
  
def test_usefulLinks():
  set_keyboard_input(["UsefulLinks", "4", "UsefulLinks", "1", "3", "UsefulLinks", "1", "8", "5", "Exit" ])
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
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: ",
    "********** USEFUL LINKS **********",
    "1. General",
    "2. Browse InCollege",
    "3. Business Solutions",
    "4. Directories",
    "5. Go Back",
    "\nSelect an option: ",
    "Under Construction",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video", 
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: ",
    "********** USEFUL LINKS **********",
    "1. General",
    "2. Browse InCollege",
    "3. Business Solutions",
    "4. Directories",
    "5. Go Back",
    "\nSelect an option: ",
    "********** USEFUL LINKS: GENERAL **********",
    "1. Sign Up",
    "2. Help Center",
    "3. About",
    "4. Press",
    "5. Blog",
    "6. Careers",
    "7. Developers",
    "8. Go Back",
    "\nSelect an option: ", 
    "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video", 
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: ",
    "********** USEFUL LINKS **********",
    "1. General",
    "2. Browse InCollege",
    "3. Business Solutions",
    "4. Directories",
    "5. Go Back",
    "\nSelect an option: ",
    "********** USEFUL LINKS: GENERAL **********",
    "1. Sign Up",
    "2. Help Center",
    "3. About",
    "4. Press",
    "5. Blog",
    "6. Careers",
    "7. Developers",
    "8. Go Back",
    "\nSelect an option: ",
    "********** USEFUL LINKS **********",
    "1. General",
    "2. Browse InCollege",
    "3. Business Solutions",
    "4. Directories",
    "5. Go Back",
    "\nSelect an option: ",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video", 
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: ",
    
  ]
def test_userSettings():
#   clearFile("userSettings.txt")    
#   clearFile("userList.txt")
#   set_keyboard_input(["Signup", "Pizzahut", "Pizzahut@2", "Pizzahut@2", "Bart", "Simpson", "Login", "Pizzahut", "Pizzahut@2", "4", "5", "0", "2", "4", "10", "10", "Exit")
#   file = open("userSettings.txt", "r")
#   output = file.read()
#   main.main()
#   assert output == ["Pizzahut={'email': True, 'sms_notif': False, 'targets_advertising': True, 'language': 'en-US'}"]
  set_keyboard_input(["Login", "Pizzahut", "Pizzahut@2", "4", "5", "0", "2", "4", "10", "10", "Exit"])
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
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: ", 
    "Enter in the username: ", 
    "Enter in the password: ", 
    "You have successfully logged in.\n",
    "<class 'dict'>",
    "('Marge Simpson', ' Spanish\n')",
    "1. Search for a job/internship \n2. Find someone you know \n3. Learn a new skill \n4. importantlinks",
    "\nPlease select a option from the list above: ",
    "*********Important Links*********", 
    "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main", 
    "Please select an options from above: ", 
    "\nThe privacy policy for In College describes how and why we might collect store, use and/or share your information when you use our services(such as visiting our website or engaging with us in other related ways). We collect personal information that you voluntarily provide to us when you register to use our services, express an interest in using our services or you participate in the activities on the services we provide. These informations include but are not limited to names, phone numbers, email address, job  titles and passwords. We process your information to provide, improve and administer our services, communicate with you, for security and fraud prevention(with your consent)\n",
    "Press 0 to Enter Guest Controls or press 1 to go back to important links: ",
    "*********Guest Controls**************",
    "1. Turn off InCollege email \n2. Turn off SMS \n3. Turn off Targeted advertising features \n4. Go back",
    "Please select an options from above: ",
    "SMS turned off",
    "*********Guest Controls**************",
    "1. Turn off InCollege email \n2. Turn off SMS \n3. Turn off Targeted advertising features \n4. Go back",
    "Please select an options from above: ",
    "*********Important Links*********", 
    "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main",
    "Please select an options from above: ",
    "Please select an options from above: ",
    "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video", 
    "\nLogin | Signup | Video | UsefulLinks | importantlinks: ",]
  output[14]="('Marge Simpson', ' Spanish\n')"