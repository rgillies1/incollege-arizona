from unittest import mock
from testing_base import get_display_output, set_keyboard_input,clearTables
import main

# Test if the program can be exited by typing 'Exit'
def test_main_exit():
    # In reality, if we call main and input "Exit" and it returns at all, then it should pass
    set_keyboard_input(["Exit"])
    ret = main.main()
    assert ret == 0

# Tests signup and if only passwords that meet security criteria are allowed
@mock.patch("home.landingPage")
def test_checkPassword(landingPage_mock):
    clearTables()
    too_short = [ "username", "Asdfg@2", "Asdfg@2", "n" ]
    too_long = [ "username", "Asdfg@2qwerty", "Asdfg@2qwerty", "n" ]
    no_capital = [ "username", "asdfg@2qw", "asdfg@2qw", "n" ]
    no_special = [ "username", "Asdfg12qw", "Asdfg12qw", "n" ]
    no_number = [ "username", "Asdfg@!qw", "Asdfg@!qw", "n" ]
    correct_input = [
        "username", "Password@2", "Password@2", "firstname", "lastname",
        "email@mail.com", "123-456-7890"
    ]
    login = ["Login", "username", "Password@2", "Exit", "Exit"]
    set_keyboard_input(["Signup"] + too_short + too_long + no_capital 
                       + no_special + no_number + correct_input + login)
    main.main()

    signup_successful = False
    landingPage_mock.assert_called()

# Test an unsuccessful and successful login
@mock.patch("home.landingPage")
def test_main_login(landingPage_mock):
  set_keyboard_input(["Login", "username", "Password@2", "n", "username", 
                      "Password@2", "Exit", "Exit"])
  main.main()
  landingPage_mock.assert_called()

#checks if the landing page and the new skills function is working correctly
def test_landingPage_newSkill():
    set_keyboard_input([
        "Login", "username", "Password@2", "3", "1", "2", "3", "4", "5", "7",
        "Exit", "Exit"
    ])
    output = get_display_output()
    main.main()
    assert output.count("This feature is under construction") > 0