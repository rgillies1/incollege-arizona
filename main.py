import os
import fileinput
import ast


def getUserInfo():
    usernameList = []
    passwordList = []
    nameList = []
    langList = []
    file = open("userList.txt", "r")
    for i in file:
        uname, pwd, fname, lname, language = i.split(",")
        pwd = pwd.strip()
        fname = fname.strip()
        lname = lname.strip()
        usernameList.append(uname)
        passwordList.append(pwd)
        nameList.append(fname + " " + lname)
        langList.append(language)
    return usernameList, passwordList, nameList, langList


def saveDefaultSettings(username):
    defaultSettings = {
        "email": True,
        "sms_notif": True,
        "targets_advertising": True,
        "language": 'en-US'
    }

    file = open("userSettings.txt", "a")
    file.write(username + "=")
    file.write(str(defaultSettings) + "\n")
    return defaultSettings


def getUserSettings(username):
    settings = {}
    file = open("userSettings.txt", "r")
    for i in file:
        uname, settings = i.split("=")
        if uname == username:
            print(type(ast.literal_eval(settings)))
            return ast.literal_eval(settings)

    # If no settings are found, generate default ones and use those
    return saveDefaultSettings(username)


def updateUserSettings(username,
                       email=None,
                       sms_notif=None,
                       targets_advertising=None,
                       language=None):
    oldSettings = getUserSettings(username)
    newSettings = {
        "email":
        email if email != None else list(oldSettings.values())[0],
        "sms_notif":
        sms_notif if sms_notif != None else list(oldSettings.values())[1],
        "targets_advertising":
        targets_advertising
        if targets_advertising != None else list(oldSettings.values())[2],
        "language":
        language if language != None else list(oldSettings.values())[3]
    }
    for line in fileinput.input("userSettings.txt", inplace=1):
        lineUsername, lineSettings = line.split("=")
        if (username == lineUsername):
            newLine = username + "=" + str(newSettings)
            print(newLine)
        else:
            print(line.replace("\n", ""))


def getContacts():
    nameList = []
    file = open("contactList.txt", "r")
    for i in file:
        fname, lname = i.split(",")
        fname = fname.strip()
        lname = lname.strip()
        nameList.append(fname + " " + lname)
    return nameList


def signup():
    global language
    usernameList = getUserInfo()[0]

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
                # IN-15: also ask for first and last name
                fname = input("Enter your first name: ")
                lname = input("Enter your last name: ")
                language = "English"
                file = open("userList.txt", "a")
                file.write(username + ", " + str(pwd1) + ", " + fname + ", " +
                           lname + ", " + language + "\n")
                print("You have successfully signed up to InCollege!")
                saveDefaultSettings(username)
            else:
                print(
                    "ERROR: Please ensure that the password follows all the requirements!"
                )
                signup()


def login():
    global logged_in
    global loggedin_user
    global currentUserSettings
    currentUserSettings = dict()
    username = input("Enter in the username: ")
    pwd = input("Enter in the password: ")
    logged_in = False
    unList, pwdList, langList, _ = getUserInfo()
    if username in unList and pwd in pwdList:
        unIndex = unList.index(username)
        pwdIndex = pwdList.index(pwd)
        if unIndex == pwdIndex:
            print("You have successfully logged in.\n")
            nameList = getUserInfo()[2]
            langList = getUserInfo()[3]
            selected_lang = langList[unIndex]
            fullName = nameList[unIndex]
            loggedin_user = username
            logged_in = True
            currentUserSettings = getUserSettings(username)
            return fullName, selected_lang
        else:
            print("Incorrect username / password, please try again.")
            login()
    else:
        print("Incorrect username / password, please try again.")
        login()


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


def findSomeone():
    print("\nFind Someone You Know")
    print(
        "Enter a first and last name and we'll let you know if they're on InCollege!"
    )
    while True:
        fname = input("Enter their first name: ")
        lname = input("Enter their last name: ")
        if fname + " " + lname in getUserInfo()[2]:
            print("They are a part of the InCollege system!")
        elif fname + " " + lname in getContacts():
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
                    return
        else:
            print("They are not yet a part of the InCollege system yet!")
            option = ""
            while option != "y" and option != "n":
                option = input(
                    "Would you like to invite contact? \nYou will be logged out. (y/n): "
                )
                if option == "n":
                    break
                elif option == "y":
                    return
        exit = ""
        while exit != "y" and exit != "n":
            exit = input(
                "Would you like to search for another person? (y/n): ")

        if exit == "n":
            break
    landingPage()


def usefulLinks():
    options = ["1", "2", "3", "4", "5"]
    generalOptions = ["1", "2", "3", "4", "5", "6", "7", "8"]
    print("********** USEFUL LINKS **********")
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Go Back")

    selection = ""

    while selection == "":
        selection = input("\nSelect an option: ")
        if selection in options:
            break

    if selection == "1":
        print("********** USEFUL LINKS: GENERAL **********")
        print("1. Sign Up")
        print("2. Help Center")
        print("3. About")
        print("4. Press")
        print("5. Blog")
        print("6. Careers")
        print("7. Developers")
        print("8. Go Back")

        genSelection = ""

        while genSelection == "":
            genSelection = input("\nSelect an option: ")
            if genSelection in generalOptions:
                break

        if genSelection == "1":
            signup()
        elif genSelection == "2":
            print("We're ready to help!")
        elif genSelection == "3":
            print(
                "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide"
            )
        elif genSelection == "4":
            print(
                "In College Pressroom: Stay on top of the latest news, updates, and reports"
            )
        elif genSelection == "8":
            usefulLinks()
        else:
            print("Under Construction")
    elif selection == "5":
        return
    else:
        print("Under Construction")


def landingPage():
    print(
        "1. Search for a job/internship \n2. Find someone you know \n3. Learn a new skill \n4. importantlinks"
    )

    option = int(input("\nPlease select a option from the list above: "))
    logged_in = True
    if option == 1:
        jobSearch()
    elif option == 2:
        findSomeone()
    elif option == 3:
        newSkill()
    elif option == 4:
        importantlinks()
    pass


def jobSearch():
    print("1. Job Board \n2. Post a job \n3. importantlinks \n9. Back")
    option = int(input("Please select an option from the list above: "))
    titleList = []
    descriptionList = []
    employerList = []
    locationList = []
    salaryList = []
    nameList = []
    file = open("jobList.txt", "r")
    if os.stat("jobList.txt").st_size != 0:
        for i in file:
            a, b, c, d, e, f = i.split("|")
            b = b.strip()
            c = c.strip()
            d = d.strip()
            e = e.strip()
            f = f.strip()
            titleList.append(a)
            descriptionList.append(b)
            employerList.append(c)
            locationList.append(d)
            salaryList.append(e)
            nameList.append(f)
    file.close()

    if option == 2:
        if len(titleList) >= 5:
            print("ERROR: Job board full, please try again later")
            jobSearch()
        else:
            jobTitle = input("Enter job title: ")
            jobDescription = input("Enter job description: ")
            jobEmployer = input("Enter job employer: ")
            jobLocation = input("Enter job location: ")
            jobSalary = input("Enter job's salary: ")
            file = open("jobList.txt", "a")
            file.write(jobTitle + "| " + str(jobDescription) + "| " +
                       str(jobEmployer) + "| " + str(jobLocation) + "| " +
                       str(jobSalary) + "| " + str(fullName) + "\n")
            file.close()
            jobSearch()

    elif option == 1:
        if os.stat("jobList.txt").st_size != 0:
            i = 0
            for i in range(len(titleList)):
                print(str(1 + i) + ". " + titleList[i])
            print("9. Back")
            jobOption = int(
                input("Select one of the jobs to view its details: "))
            if (jobOption == 9):
                jobSearch()
            print("\nJob Title: " + titleList[jobOption - 1] + "\n")
            print("Job Description: " + descriptionList[jobOption - 1] + "\n")
            print("Job Employer: " + employerList[jobOption - 1] + "\n")
            print("Job Location: " + locationList[jobOption - 1] + "\n")
            print("Job Salary: " + salaryList[jobOption - 1] + "\n")
        else:
            print("Job board empty")
        jobSearch()

    elif option == 9:
        landingPage()
    elif option == 3:
      importantlinks()


def newSkill():
    print(
        "1. Study Habits \n2. Creative Thinking \n3. Critical Thinking \n4. Work/School Life Balance \n5. Scheduling \n6. importantlinks \n7. return back to landing page"
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
        importantlinks()
    elif option == 7:
        landingPage()
    else:
        print("Please enter in a number based on the skill you want to learn!")
        newSkill()
    pass


def changelanguage(userLogin):
    replace_language = "Spanish"
    search_language = "English"

    with open('userList.txt', 'r+') as f:
        newline = []
        x = f.readlines()
        for line in x:
            feild = line.split(',')
            if feild[0] == userLogin:
                feild[4] = feild[4].replace(search_language, replace_language)
                newline.append(','.join(feild))
            else:
                newline.append(','.join(feild))

    with open('userList.txt', 'w+') as f:
        for line in newline:
            f.write(line)


def GuestControls():
    global loggedin_user
    global logged_in
    print("*********Guest Controls**************")
    print(
        "1. Turn off InCollege email \n2. Turn off SMS \n3. Turn off Targeted advertising features \n4. Go back"
    )
    input_selection = int(input("Please select an options from above: "))
    if logged_in == True: 
      if input_selection == 1:
          updateUserSettings(loggedin_user, email=False)
          print("InCollege email turned off.")
          GuestControls()
      elif input_selection == 2:
          updateUserSettings(loggedin_user, sms_notif=False)
          print("SMS turned off")
          GuestControls()
      elif input_selection == 3:
          updateUserSettings(loggedin_user, targets_advertising=False)
          print("targeted advertising turned off")
          GuestControls()
      elif input_selection == 4:
          importantlinks()
    else:
      print("You need to first sign in to use guest controls.")
      login()

#In college important links option
def importantlinks():
    global logged_in
    print("*********Important Links*********")
    print(
        "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main"
    )

    input_selection = int(input("Please select an options from above: "))

    if input_selection == 1:
        print(
            "\nWe are committed to safeguarding the privacy of InCollege users. This notice applies where we are acting as a data controller with respect to the personal data of such persons; in other words, where we determine the purposes and means of the processing of that personal data.Our website incorporates privacy controls which affect how we will process your personal data.You can access the privacy controls via privacy policy page\n"
        )
        importantlinks()

    elif input_selection == 2:
        print(
            "\nWelcome to In College! We are a large professional network with millions of members spreaded globally across many countries. Our Vision is to make jobs accessible to all members of the global workforce and our mission is to connect students to make them more productive and successful. InCollege begin in co-founder Jim Andersons Classroom in September 2022\n"
        )
        importantlinks()

    elif input_selection == 3:
        print(
            "\nInCollege is a space where every member of the global student workforce can find opportunity. Whatever your goals, ideas, abilities are we are here for you to succeed. We are on a journey to make accessibility and inclusive design part of our core principles, building accessibility from the ground up and testing our products with assistive technology to make sure that everyone can use InCollege to advance their professional goals.\n"
        )
        importantlinks()
    elif input_selection == 4:
        print(
            "\n These Terms of Use constitute a legally binding agreement made between you, whether personally or on behalf of an entity(you) and company(we, us , ours), and concerning your address to and use of InCollege.com website as well as any other media form, media channel, media website or mobile application related, linked or otherwise connected. You agree that by accessing the Site, you have read and understood and agreed to be bound by all these terms of use IF YOU DO NOT AGREE WITH ALL OF THESE TERMS OF USE, THEN YOU ARE EXPRESSLY PROHIBITED FROM USING THE SITE AND YOU MUST DISCONTINUE USE IMMEDIATELY. \n"
        )
        importantlinks()

    elif input_selection == 5:
        print(
            "\nThe privacy policy for In College describes how and why we might collect store, use and/or share your information when you use our services(such as visiting our website or engaging with us in other related ways). We collect personal information that you voluntarily provide to us when you register to use our services, express an interest in using our services or you participate in the activities on the services we provide. These informations include but are not limited to names, phone numbers, email address, job  titles and passwords. We process your information to provide, improve and administer our services, communicate with you, for security and fraud prevention(with your consent)\n"
        )
        user_selection = int(
            input(
                "Press 0 to Enter Guest Controls or press 1 to go back to important links: "
            ))
        if user_selection == 0:
            GuestControls()

        elif user_selection == 1:
            importantlinks()
        else:
            print("Invalid Input!")
            user_selection = int(
                input(
                    "Press 0 to Enter Guest Controls or press 1 to go back to important links: "
                ))
    elif input_selection == 6:
        print(
            "\nCookies and Ip Addresses allow us to improve our web content. We may use cookies and similar tracking technologies(like web beacons and pixels) to access or store information. Specific information about how we use such technogies and how you can refuse certain cookies is set out in our Cookies notice. We may transfer store and process your information in countries other than your own. However we will take all neccessary measures to protect your personal information in accordance with this privacy notice and applicable law\n"
        )
        importantlinks()

    elif input_selection == 7:
        print(
            "\nPursuant to the Digital Millennium Copyright Act (17 U.S.C. § 512), InCollege has implemented procedures for receiving written notification of claimed infringements.If you believe in good faith that your copyright has been infringed, you may read the notice of copyright and inform it to the InCollege team so that we can take appropriate actions\n"
        )
        importantlinks()

    elif input_selection == 8:
        print(
            "\nOur InCollege brand features and trademarks are protected by law. You will need our permission(InCollege admin) in order to use them. You can request for the permission requests, contact InCollegepermission_request@InCollege.com. InCollege does not permit its members or any third party services to use its trademark, logos, web pages, screenshots and any other brand features. Any other uses must obtain prior approval from InCollege.\n"
        )
        importantlinks()
    elif input_selection == 9:
        #check if the user is signed in
        #then prompts that language is changed to spanish
        if logged_in == True:
            input_gen = int(
                input(
                    "Press 1 to change language settings from English to Spanish or Press 0 to go back: "
                ))
            if input_gen == 1:
                changelanguage(loggedin_user)
                print("Language successfully changed from English to Spanish!")
                return None
            elif input_gen == 0:
                importantlinks()
            else:
                print("Please enter a correct digit to move forward.")
        else:
            print(
                "You need to login in order to change the language. Please login with you credentials from the main menu."
            )
            return None

    elif input_selection == 10:
        return None

    else:
        print("Please enter a correct digit to move forward.")
        print(
            "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main"
        )

    input_selection = int(input("Please select an options from above: "))


def main():
    global logged_in
    logged_in = False
    global fullName
    print("*************************************************************")
    print("*  \"InCollege has helped me throughout my whole journey -   *")
    print("*  whether it be developing skills, making connections,     *")
    print("*  or even landing my first job, InCollege has been there   *")
    print("*  to support me every step of the way with its simple yet  *")
    print("*  engaging design.\"                                        *")
    print("*                                                           *")
    print("*                     - Quandale Dingle                     *")
    print("*************************************************************")
    stay = True
    while stay:
        print(
            "Welcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video"
        )
        option = input(
            "\nLogin | Signup | Video | UsefulLinks | importantlinks: ")
        if option == "Login":
            fullName = login()[0]
            print(fullName)
            landingPage()
        elif option == "Signup":
            signup()
        elif option == "Video":
            print("Video is now playing...\n")
        elif option == "UsefulLinks":
            usefulLinks()
        elif option == "importantlinks":
            importantlinks()
        elif option == "Exit":
            stay = False
        else:
            #print(option)
            print("\nERROR: please check spellings, this is case-sensitive\n")


fullName = None

#main()
