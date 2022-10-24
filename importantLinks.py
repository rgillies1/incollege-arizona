from login import login
from database import updateUser,authUser
#from login import logged_in, loggedin_user

def changelanguage():#Updates language of the logged in user
    replace_language = "Spanish"
    search_language = "English"
    updateUser("UserSettings","Language", search_language)#Missing userId, #"es-mx"
    updateUser("UserData","Language",replace_language)#Missing userId

def GuestControls():#Disables different user settings
    global loggedin_user
    global logged_in
    print("\n*********Guest Controls**************")
    print(
        "1. Turn off InCollege email \n2. Turn off SMS \n3. Turn off Targeted advertising features \n4. Go back"
    )
    input_selection = int(input("Please select an options from above: "))
    if authUser()[0] == True:
        if input_selection == 1:
            #updateUserSettings(loggedin_user, email=False)
            updateUser("UserSettings","emailNotif",0)#Disables email notifications
            print("InCollege Email Notifications Disabled")
            GuestControls()
        elif input_selection == 2:
            #updateUserSettings(loggedin_user, sms_notif=False)
            updateUser("UserSettings","smsNotif",0)#Disabled SMS Notifications
            print("SMS Notifications Disabled")
            GuestControls()
        elif input_selection == 3:
            #updateUserSettings(loggedin_user, targets_advertising=False)
            updateUser("UserSettings","targetAds",0)#Disables targeted ads
            print("Targeted Advertising Disabled")
            GuestControls()
        elif input_selection == 4:
            importantLinks()
    else:
        print("You need to first sign in to use guest controls.")
        log = input("Would you like to login?(y/n): ")
        if(log=="y"):#Allows user to login and then edit guestControls
            login()
        GuestControls()


#In college important links option
def importantLinks():
    #global logged_in
    logged_in = True
    print("\n*********Important Links*********")
    print(
        "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main"
    )

    input_selection = int(input("Please select an options from above: "))

    if input_selection == 1:#Copyright Notice
        print(
            "\nWe are committed to safeguarding the privacy of InCollege users. This notice applies where we are acting as a data controller with respect to the personal data of such persons; in other words, where we determine the purposes and means of the processing of that personal data.Our website incorporates privacy controls which affect how we will process your personal data.You can access the privacy controls via privacy policy page\n"
        )
        importantLinks()

    elif input_selection == 2:#About
        print(
            "\nWelcome to In College! We are a large professional network with millions of members spreaded globally across many countries. Our Vision is to make jobs accessible to all members of the global workforce and our mission is to connect students to make them more productive and successful. InCollege begin in co-founder Jim Andersons Classroom in September 2022\n"
        )
        importantLinks()

    elif input_selection == 3:#Accessability
        print(
            "\nInCollege is a space where every member of the global student workforce can find opportunity. Whatever your goals, ideas, abilities are we are here for you to succeed. We are on a journey to make accessibility and inclusive design part of our core principles, building accessibility from the ground up and testing our products with assistive technology to make sure that everyone can use InCollege to advance their professional goals.\n"
        )
        importantLinks()
    elif input_selection == 4:#User Agreement
        print(
            "\n These Terms of Use constitute a legally binding agreement made between you, whether personally or on behalf of an entity(you) and company(we, us , ours), and concerning your address to and use of InCollege.com website as well as any other media form, media channel, media website or mobile application related, linked or otherwise connected. You agree that by accessing the Site, you have read and understood and agreed to be bound by all these terms of use IF YOU DO NOT AGREE WITH ALL OF THESE TERMS OF USE, THEN YOU ARE EXPRESSLY PROHIBITED FROM USING THE SITE AND YOU MUST DISCONTINUE USE IMMEDIATELY. \n"
        )
        importantLinks()

    elif input_selection == 5:#Privacy Policy and GuestControls
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
            importantLinks()
        else:
            print("Invalid Input!")
            user_selection = int(
                input(
                    "Press 0 to Enter Guest Controls or press 1 to go back to important links: "
                ))
    elif input_selection == 6:#Cookie Policy
        print(
            "\nCookies and Ip Addresses allow us to improve our web content. We may use cookies and similar tracking technologies(like web beacons and pixels) to access or store information. Specific information about how we use such technogies and how you can refuse certain cookies is set out in our Cookies notice. We may transfer store and process your information in countries other than your own. However we will take all neccessary measures to protect your personal information in accordance with this privacy notice and applicable law\n"
        )
        importantLinks()

    elif input_selection == 7:#Copyright Policy
        print(
            "\nPursuant to the Digital Millennium Copyright Act (17 U.S.C. § 512), InCollege has implemented procedures for receiving written notification of claimed infringements.If you believe in good faith that your copyright has been infringed, you may read the notice of copyright and inform it to the InCollege team so that we can take appropriate actions\n"
        )
        importantLinks()

    elif input_selection == 8:
        print(
            "\nOur InCollege brand features and trademarks are protected by law. You will need our permission(InCollege admin) in order to use them. You can request for the permission requests, contact InCollegepermission_request@InCollege.com. InCollege does not permit its members or any third party services to use its trademark, logos, web pages, screenshots and any other brand features. Any other uses must obtain prior approval from InCollege.\n"
        )
        importantLinks()
    elif input_selection == 9:
        #check if the user is signed in
        #then prompts that language is changed to spanish
        if authUser()[0] == True:
            input_gen = int(
                input(
                    "Press 1 to change language settings from English to Spanish or Press 0 to go back: "
                ))
            if input_gen == 1:
                changelanguage()
                print("Language successfully changed from English to Spanish!")
                importantLinks()
            elif input_gen == 0:
                importantLinks()
            else:
                print("Please enter a correct digit to move forward.")
        else:
            print(
                "You need to login in order to change the language. Please login with you credentials from the main menu."
            )
            return None

    elif input_selection == 10:
        return None
    '''else:
        print("Please enter a correct digit to move forward.")
        print(
            "1. Copyright Notice \n2. About \n3. Accessibility \n4. User Agreement \n5. Privacy Policy \n6. Cookie policy \n7. Copyright Policy \n8. Brand Policy \n9. Languages \n10. return back to main"
        )

    input_selection = int(input("Please select an options from above: "))'''