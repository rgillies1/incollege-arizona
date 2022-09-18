def signup():
    usernameList = []
    file = open("userList.txt", "r")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        c = a, b
        usernameList.append(a)

    if len(usernameList) >= 5:
        print(
            "ERROR: All permitted accounts have been created, please come back later"
        )
        return
    else:
        username = input("Enter a username: ")

        print(
            "\nBefore entering a password, make sure it is between 8 and 12 characters long. Must include at least one capital letter, at least one digit, and at least one special chracter('$', '@', '#', '!', '%', '^', '&', '*')!\n"
        )
        pwd1 = input("Enter a password: ")
        pwd2 = input("Confirm the password: ")

    if username in usernameList:
        print("ERROR: Username already exist!")
        signup()
    else:
        #Check if password are the same
        if pwd1 != pwd2:
            print("ERROR: Password does not match: ")
            signup()
        else:
            #if password and username meets the requirements we can append it to the file
            if checkPassword(pwd1) == True:
                file = open("userList.txt", "a")
                file.write(username + ", " + str(pwd1) + "\n")
                print("You have successfully signed up to InCollege!")
            else:
                print(
                    "ERROR: Please ensure that the password follows all the requirements!"
                )
                signup()
    pass


def login():
    username = input("Enter in the username: ")
    pwd = input("Enter in the password: ")

    #open files to read
    file = open("userList.txt", "r")

    unList = []
    pwdList = []
    for i in file:
      a, b = i.split(",")
      b = b.strip()

      unList.append(a)
      pwdList.append(b)

    if username in unList and pwd in pwdList:
      unIndex = unList.index(username)
      pwdIndex = pwdList.index(pwd)
      if unIndex == pwdIndex:
        print("You have successfully logged in.\n")
        landingPage()
      else:
        print("Incorrect username / password, please try again.")
        login()
    else:
      print("Incorrect username / password, please try again.")
      login()

    pass


def checkPassword(password):
    specialChar = ['$', '@', '#', '!', '%', '^', '&', '*']
    valid = True
    if len(password) < 8:
        print("Password must have at least 8 characters.")
        #signup()
        valid = False
    if len(password) > 12:
        print("Password must be less than 12 characters.")
        #signup()
        valid = False
    if not any(char.isdigit() for char in password):
        print("Password must contain a digit.")
        #signup()
        valid = False
    if not any(char.isupper() for char in password):
        print("Password must contain one upper.")
        #signup()
        valid = False
    if not any(char in specialChar for char in password):
        print("Password must contain a special character.")
        #signup()
        valid = False
    if valid:
        return valid


#----------------------------------------------------------


def landingPage():
    print(
        "1. Search for a job \n2. Find someone you know \n3. Learn a new skill"
    )

    option = int(input("\nPlease select a option from the list above: "))

    if option == 1:
        print("\nThis feature is under construction!")
        landingPage()
    elif option == 2:
        print("\nThis feature is under construction!")
        landingPage()
    elif option == 3:
        newSkill()
    pass


#----------------------------------------------------------
def newSkill():
    print(
        "1. Study Habits \n2. Creative Thinking \n3. Critical Thinking \n4. Work/School Life Balance \n5. Scheduling \n6. return back to landing page"
    )

    option = int(input("Please select a skill you would like to learn: "))

    if option == 1:
        print("This feature is under construction")
        newSkill()
    elif option == 2:
        print("This feature is under construction")
        newSkill()
    elif option == 3:
        print("This feature is under construction")
        newSkill()
    elif option == 4:
        print("This feature is under construction")
        newSkill()
    elif option == 5:
        print("This feature is under construction")
        newSkill()
    elif option == 6:
        landingPage()
    else:
        print("Please enter in a number based on the skill you want to learn!")
        newSkill()
    pass


def main():
    stay = True
    print(
        "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE:Login \nTo create a new InCollege account TYPE: Signup"
    )
    option = input("\nLogin | Signup: ")
    if option == "Login":
        login()
    elif option == "Signup":
        signup()
    elif option == "Exit":
        stay=False
    else:
        #print(option)
        print("\nERROR: please check spellings, this is case-sensitive\n")
    if(stay):
        main()
#main()