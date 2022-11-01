from jobSearch import jobSearch
from newSkill import newSkill
from importantLinks import importantLinks
from usefulLinks import usefulLinks
from findSomeone import findSomeone, searchStudents
from friendNetwork import friendNetwork
from database import getFriendRequests,logout
from profiles import profile

def landingPage():#Landing page for inCollege, the first place you go after you log in
    print(
        "\n~~~~LANDING PAGE~~~~\n\n1. Search for a job/internship \n2. Find someone you know \n3. Learn a new skill \n4. Find a student \n5. Show my network \n6. View Profile \n7. UsefulLinks \n8. ImportantLinks \nType 'Exit' to exit"
    )
    openFriendRequests = getFriendRequests()
    if (len(openFriendRequests) > 0):
        print("\n\nYou have a pending friend request.  Select option 5 to respond")
    option = input("\nPlease select a option from the list above: ")
    #logged_in = True
    if option == "1":#Goto jobSearch
        jobSearch()
    elif option == "2":#goto findSomeone
        findSomeone()
    elif option == "3":#goto newSkill
        newSkill()
    elif option == "4":#go to findSomeone
        searchStudents()
    elif option == "5":#goto friendNetwork
        friendNetwork()
    elif option == "6":#go to profiles 
        profile()
    elif option == "7":#goto usefulLinks
        usefulLinks()
    elif option == "8":#goto importantLinks
        importantLinks()
    elif option == "Exit":#exit
        logout()
        return None
    else:
        print("Invalid option, please try again \n")
    landingPage()
