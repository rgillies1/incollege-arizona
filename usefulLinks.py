from signup import signup
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
