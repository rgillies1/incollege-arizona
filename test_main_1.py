import pytest
from unittest import mock
import main
from tud_test_base import get_display_output, set_keyboard_input
import os


def clearUserList():
    os.remove("userList.txt")
    f = open("userList.txt", "x")
    f.close()


# Test if the program can be exited by typing 'Exit'
def test_main_exit():
    # In reality, if we call main and input "Exit" and it returns at all, then it should pass
    set_keyboard_input(["Exit"])
    ret = main.main()
    assert ret == 0


# Tests signup and if only passwords that meet security criteria are allowed
def test_checkPassword():
    clearUserList()
    set_keyboard_input([
        "Signup", "Dominos", "dom", "dom", "dom", "Dominos2@1234",
        "Dominos2@1234", "Dominos", "Dominos2@", "Dominos2@", "Dom", "Inos",
        "Culinary Arts", "USF", "Exit"
    ])
    main.main()

    signup_successful = False
    with open("userList.txt", "r") as list:
        for line in list:
            if line == "Dominos, Dominos2@, Dom, Inos, English, Culinary Arts, USF\n":
                signup_successful = True

    assert signup_successful


# Test an unsuccessful and successful login
@mock.patch("main.landingPage")
def test_main_login(landingPage_mock):  #
    set_keyboard_input([
        "Login", "Dominos", "Dominos2", "Dominos", "Dominos2@", "Exit", "Exit"
    ])
    main.main()
    landingPage_mock.assert_called()


#checks if the landing page and the new skills function is working correctly
def test_landingPage_newSkill():
    set_keyboard_input([
        "Login", "Dominos", "Dominos2@", "3", "1", "2", "3", "4", "5", "7",
        "Exit", "Exit"
    ])
    output = get_display_output()
    main.main()
    assert output.count("This feature is under construction") > 0
