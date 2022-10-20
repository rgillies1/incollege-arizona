from signup import signup
from usefulLinks import usefulLinks
from importantLinks import importantLinks
from login import login
from landingPage import landingPage
import os

def homePage():
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
            "\n\nWelcome to InCollege! \nTo Log in to an existing InCollege account TYPE: Login \nTo create a new InCollege account TYPE: Signup\nTo view a video highlighting the advantages of joining InCollege TYPE: Video"
        )
        option = input(
            "\nLogin | Signup | Video | UsefulLinks | importantLinks | Exit: ")
        if option == "Login":
            if(login()):
                  landingPage()
        elif option == "Signup":
            signup()
        elif option == "Video":
            print("Video is now playing...\n")
        elif option == "UsefulLinks":
            usefulLinks()
        elif option == "importantLinks":
            importantLinks()
        elif option == "Exit":
            stay = False
        else:
            print("\nERROR: please check spellings, this is case-sensitive\n")
    return 0

