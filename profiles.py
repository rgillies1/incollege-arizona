from database import setProfile, setEducation, setJobExperience, getProfile, getEducation, getJobExperience, getUserFirstLastName, getFriends
from friendNetwork import friendNetwork
from importantLinks import importantLinks
from usefulLinks import usefulLinks


def editProfile():  #Edit logged in user profilepro = getProfile()

    def prof():
        title, about = getProfile()
        if (title != None):
            print(title.title() + "\n\n")
        if (about != None):
            print("About: " + about + "\n")
        print("\n\t1. Title \n\t2. About\nExit")
        selection = -1
        selections = ['1', '2', 'Exit']
        while selection not in selections:
            selection = input(
                "Choose option from above or Type 'Exit' to exit: ")
        if (selection == 'Exit'):
            return None
        if (selection == '1'):
            title = input("Title: ").title()
            setProfile(title=title)
        elif (selection == '2'):
            about = input("About: ")
            setProfile(about=about)
        return prof()

    def educ():
        university, major, degree, years = getEducation()
        print("**Education**")
        if (university != None):
            print("\tUniversity: " + university.title())
        if (major != None):
            print("\tMajor: " + major.title())
        if (degree != None):
            print("\tDegree: " + degree)
        if (years != None):
            print("\tYear: " + str(years))

        print(
            "\n\t1. University \n\t2. Major \n\t3. Degree \n\t4. Years \nExit")
        selection = -1
        selections = ['1', '2', '3', '4', 'Exit']
        while selection not in selections:
            selection = input(
                "Choose option from above or Type 'Exit' to exit: ")
        if (selection == 'Exit'):
            return None
        if (selection == '1'):
            university = input("University: ").title()
            setEducation(university=university)
        elif (selection == '2'):
            major = input("Major: ").title()
            setEducation(major=major)
        elif (selection == '3'):
            degree = input("Degree: ")
            setEducation(degree=degree)
        elif (selection == '4'):
            years = input("Years: ")
            setEducation(years=years)
        return educ()

    def jobExp():
        jobs = getJobExperience()
        print("**Job Experience**")
        for i in range(0, len(jobs)):
            jobNum, job, boss, start, end, loc, desc = jobs[i]
            if (job != None):
                print("\n\tJob Title: " + job)
            if (boss != None):
                print("\t\tEmployer: " + boss)
            if (start != None and end != None):
                print("\t\tFrom {0} to {1}".format(start, end))
            elif (start != None):
                print("\t\tStart Date: " + start)
            elif (end != None):
                print("\t\tEnd Date: " + end)
            if (loc != None):
                print("\t\tLocation: " + loc)
            if (desc != None):
                print("\t\tDescription: " + desc)
        if (len(jobs) < 3):
            print("\n\t0. New Job ")

        for i in range(0, len(jobs)):
            print("\t{0}. Job".format(i + 1))
        print("\nExit")
        selection = -1
        selections = ['0', '1', '2', '3', 'Exit']
        while selection not in selections:
            selection = input(
                "Choose option from above or Type 'Exit' to exit: ")
            if (selection.isnumeric()):
                if (selection == '0' and len(jobs) == 3 or
                    (int(selection) > len(jobs))):  #Checks selection is valid
                    selection = -1
        if (selection == 'Exit'):
            return None
        if (selection == '0'):
            #print("here")
            setJobExperience(jobNum=-1)
        else:
            jobNum = int(selection)
            opt = "n"
            while opt != "Exit":
                waste, job, boss, start, end, loc, desc = jobs[jobNum - 1]
                if (job != None):
                    print("\n\tJob Title: " + job)
                if (boss != None):
                    print("\t\tEmployer: " + boss)
                if (start != None and end != None):
                    print("\t\tFrom {0} to {1}".format(start, end))
                elif (start != None):
                    print("\t\tStart Date: " + start)
                elif (end != None):
                    print("\t\tEnd Date: " + end)
                if (loc != None):
                    print("\t\tLocation: " + loc)
                if (desc != None):
                    print("\t\tDescription: " + desc)
                print(
                    "\n\n\t1. Job Title \n\t2. Employer \n\t3. Start Date \n\t4. End Date \n\t5. Location \n\t6. Description \nExit"
                )
                validOpts = ['1', '2', '3', '4', '5', '6', 'Exit']
                opt = -1
                while opt not in validOpts:
                    opt = input(
                        "Choose option from above or Type 'Exit' to exit: ")
                if (opt == '1'):
                    position = input("Job Title: ")
                    setJobExperience(jobNum=jobNum, jobTitle=position)
                if (opt == '2'):
                    employer = input("Employer: ")
                    setJobExperience(jobNum=jobNum, employer=employer)
                if (opt == '3'):
                    start = input("Start Date: ")
                    setJobExperience(jobNum=jobNum, startDate=start)
                if (opt == '4'):
                    end = input("End Date: ")
                    setJobExperience(jobNum=jobNum, endDate=end)
                if (opt == '5'):
                    location = input("Location: ")
                    setJobExperience(jobNum=jobNum, location=location)
                if (opt == '6'):
                    description = input("Description: ")
                    setJobExperience(jobNum=jobNum, description=description)
        return jobExp()

    print(
        "1. Title and About \n2. Education Information \n3. Job Experience Information \nExit"
    )
    option = -1  #Place holder value
    validOptions = ['1', '2', '3', 'Exit']
    while option not in validOptions:
        option = input("Choose option from above or Type 'Exit' to exit: ")
    if (option == 'Exit'):
        return None
    elif (option == '1'):
        prof()
    elif (option == '2'):
        educ()
    elif (option == '3'):
        jobExp()
    return editProfile()


def friendProfiles(
):  #Prints friends and allows to choose which friend profile to view
    friends = getFriends()
    print("")
    if (len(friends) == 0):
        print("You are a lonely loser")
        return None
    else:
        print("Friend Profiles:")
        for i in range(0, len(friends)):
            print("\t" + str(i + 1) + ". " + friends[i][0])
        friend = input("Pick which friend's profile to view, or type 'Exit': ")
        if (friend == 'Exit'):
            return None
        elif (friend.isnumeric()):
            if (int(friend) > 0 and int(friend) <= len(friends)):
                profile(friends[int(friend) - 1][1])
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")
    friendProfiles()


def profile(
    userId=-1
):  #Displays profile of selected userId.  userId=-1 means logged in user
    user, first, last = getUserFirstLastName(userId)
    pro = getProfile(userId)
    edu = getEducation(userId)
    jobs = getJobExperience(userId)
    print("\n~~~~~~{0} {1}'s Profile~~~~~~\n\n".format(first, last))

    if (pro != (None, None)):  #Title and about check
        title, about = pro
        if (title != None):
            print(title.title() + "\n\n")
        if (about != None):
            print("About: " + about + "\n")

    if (edu != (None, None, None, None)):  #Education check
        university, major, degree, years = edu
        print("**Education**")
        if (university != None):
            print("\tUniversity: " + university.title())
        if (major != None):
            print("\tMajor: " + major.title())
        if (degree != None):
            print("\tDegree: " + degree)
        if (years != None):
            print("\tYear: " + str(years))
        print("\n")

    if (jobs != [] and jobs != [(None, None, None, None, None, None, None)
                                ]):  #Job Experience check
        print("**Job Experience**")
        for i in range(0, len(jobs)):
            jobNum, job, boss, start, end, loc, desc = jobs[i]
            if (job != None):
                print("\n\tJob Title: " + job)
            if (boss != None):
                print("\t\tEmployer: " + boss)
            if (start != None and end != None):
                print("\t\tFrom {0} to {1}".format(start, end))
            elif (start != None):
                print("\t\tStart Date: " + start)
            elif (end != None):
                print("\t\tEnd Date: " + end)
            if (loc != None):
                print("\t\tLocation: " + loc)
            if (desc != None):
                print("\t\tDescription: " + desc)
            print("\n")

    if (userId == -1):
        print(
            "\nOptions:\n\t1. Friend Profiles \n\t2. Friend Network \n\t3. Edit Profile \n\t4. Useful Links \n\t5. Important Links \nExit"
        )
        choice = -1
        validChoices = ['1', '2', '3', '4', 'Exit']
        while choice not in validChoices:
            choice = input(
                "Please choose from the options above. Type 'Exit' to exit: ")
        if (choice == '1'):
            friendProfiles()
        elif (choice == '2'):
            friendNetwork()
        elif (choice == '3'):
            editProfile()
        elif (choice == '4'):
            usefulLinks()
        elif (choice == '5'):
            importantLinks()
        else:
            return None
    return profile()
