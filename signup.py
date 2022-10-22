from database import getRecordCount, exist, newAccount

def checkPassword(password):#Checks Password Requirements
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

def signup(exit="n"):#Signs up user
    table = "UserLogin" 
    global language
    global major
    global university
    #usernameList = getUserInfo()[0]
  
    if(exit=="y"):#Allows exit if they want to give up trying to sign up
        pass
    
    if getRecordCount() >= 10:  #maximum 10 accounts permitted
        print(
            "ERROR: All permitted accounts have been created, please come back later"
        )
        pass
    else:
        username = input("Enter a username: ")

        print(
            "\nBefore entering a password, make sure it is between 8 and 12 characters long. Must include at least one capital letter, at least one digit, and at least one special chracter('$', '@', '#', '!', '%', '^', '&', '*')!\n"
        )
        pwd1 = input("Enter a password: ")
        pwd2 = input("Confirm the password: ")

    if exist(table, "username", username):#checks to see if values already exist in db
        print("ERROR: Username already exist!")
        exit = input("Would you like to exit(y/n):")
        signup(exit)
    else:
        #Check if password are the same
        if pwd1 != pwd2:
            print("ERROR: Password does not match: ")
            exit = input("Would you like to exit(y/n):")
            signup(exit)
        else:
            #if password and username meets the requirements we can append it to the file
            if checkPassword(pwd1) == True:
                # IN-15: also ask for first and last name
                fname = input("Enter your first name: ")
                lname = input("Enter your last name: ")
                #major = input("Enter your major: ")
                #university = input("Enter your university: ")
                email = input("Enter your email: ")
                phone = input("Enter your phone number(Please Format Like ###-###-####): ")
                #newAccount(username,pwd1,fname,lname,major,university,email,phone)
                newAccount(username,pwd1,fname,lname,email,phone)
            else:
                print(
                    "ERROR: Please ensure that the password follows all the requirements!"
                )
                exit = input("Would you like to exit(y/n):")
                signup(exit)
