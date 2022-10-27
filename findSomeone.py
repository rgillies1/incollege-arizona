from database import findContact,findUser,addContact,newFriendRequest
from signup import validName,validPhone,validEmail

def searchStudents():#Search users on the system
    print("\nFind a student you know!")
    print(
        "Enter the last name, university or major and we'll search for the student in our system!\n"
    )
    print("1. Search using last names \n2. Search using majors \n3. Search using Colleges \n4. To go back to the landing page!")
    choice = int(
        input(
            "Enter your choice: "
        ))
    if choice == 1:#Search via last names
        lname = input("Enter their last name: ")
        students = findUser(lastName=lname)
        for i in range(0,len(students)):#Prints list of possible students to select
            if(students[i][0]==None):#person is on contact list, but not a user
                students.pop(i)
                i-=1
                continue
            print("{0}. {1} {2}".format(i+1,students[i][1],students[i][2]))
        if(len(students)>0):
            option = int(input("Select user from list to send friend request to, or Press 0 to go back: "))
            if(option>0 or option <= len(students)):
                newFriendRequest(students[option-1][0])#Goes to database.py to send friend requests
            searchStudents()
        else:
            print("Not apart of InCollege")#Student not in InCollege
            searchStudents()

    elif choice == 2:#Search via major
        #print("NOT WORKING CURRENTLY AS MAJOR STORAGE LOCATION CHANGED AS OF 10/20")
        #searchStudents()
        major = input("Enter their major: ")  #for major in list of majors
        students = findUser(major=major)
        for i in range(0,len(students)):
            if(students[i][0]==None):#person is on contact list, but not a user
                students.pop(i)
                i-=1
                continue
            print("{0}. {1} {2}".format(i+1,students[i][1],students[i][2]))#prints possible students from list
        if(len(students)>0):
            option = int(input("Select user from list to send friend request to, or Press 0 to go back: "))
            if(option>0 or option <= len(students)):
                newFriendRequest(students[option-1][0])
            searchStudents()
        else:
            print("Not apart of InCollege")
            searchStudents()
          
    elif choice == 3:#Search via university names
        #print("NOT WORKING CURRENTLY AS UNIVERSITY STORAGE LOCATION CHANGED AS OF 10/20")
        #searchStudents()
        uni = input("Enter the name of University: "
                    )  #for university in list of universities
        students = findUser(university=uni)
        for i in range(0,len(students)):
            if(students[i][0]==None):#person is on contact list, but not a user
                students.pop(i)
                i-=1
                continue
            print("{0}. {1} {2}".format(i+1,students[i][1],students[i][2]))#prints possible students from list
        if(len(students)>0):
            option = int(input("Select user from list to send friend request to, or Press 0 to go back: "))
            if(option>0 or option <= len(students)):
                newFriendRequest(students[option-1][0])
            searchStudents()
        else:
            print("Not apart of InCollege")
            searchStudents()
    elif choice == 4:
        pass
    else:
        print(
            "Wrong choice! Enter your choice as follows: \n1.To search using usernames, \n2. Search using university or \n3. To search using majors! \n4. To go back to the landing page!"
        )


def findSomeone():#Find someone that may not be on InCollege and add new users contact
    print("\nFind Someone You Know")
    print(
        "Enter a first and last name and we'll let you know if they're on InCollege!"
    )
    while True:
        fname = input("\nEnter their first name: ")
        lname = input("Enter their last name: ")
        valid,fname,lname = validName(fname,lname)
        if(not valid):
            print("Invalid input detected in either first name or last name.  If you believe this to be an error, please contact us through the information that is currently not provided.")
        if(valid):      
            search = findContact(fname,lname)
            if search==None:
                print("They are not yet a part of the InCollege system yet!")
                option = ""
                while option != "y" and option != "n":
                    option = input(
                        "Would you like to invite contact? \nYou will be logged out after providing contact information. (y/n): "
                    )
                    if option == "n":
                        break
                    elif option == "y":
                        valid = False
                        while not valid:
                            phone = input("\nPlease provide their phone number(Format: '###-###-####'): ")
                            valid = validPhone(phone)
                            if(not valid):
                                print("Invalid input detected in phone number provided.  If you believe this to be an error, please contact us through the information that is currently not provided.")
                                exit=input("Would you like to exit?(y/n): ")
                                if(exit=='y'):
                                    return None
                        valid = False 
                        while not valid:
                            email = input("\nPlease provide their email:")
                            valid = validEmail(email)
                            if(not valid):
                                print("Invalid input detected in email provided.  If you believe this to be an error, please contact us through the information that is currently not provided.")
                                exit=input("Would you like to exit?(y/n): ")
                                if(exit=='y'):
                                    return None
                        addContact(fname,lname,phone,email)
                        pass
            elif(search[0]!=None):
                print("They are a part of the InCollege system!")
            elif (search[0]==None):
                print(
                    "Contact found but they are not yet part of the InCollege system"
                )
                option = ""
                while option != "y" and option != "n":
                    option = input(
                        "Would you like to invite contact? \nYou will be logged out. (y/n): "
                    )
                    if option == "n":
                        break
                    elif option == "y":
                        pass
        exit = ""
        while exit != "y" and exit != "n":
            exit = input(
                "Would you like to search for another person? (y/n): ")

        if exit == "n":
            break
