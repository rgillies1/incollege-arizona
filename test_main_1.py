from unittest import mock
from testing_base import get_display_output, set_keyboard_input, clearTables
from database import allRecords, getRecordCount
import main


# Test if the program can be exited by typing 'Exit'
def test_main_exit():
    clearTables()
    # In reality, if we call main and input "Exit" and it returns at all, then it should pass
    set_keyboard_input(["Exit"])
    ret = main.main()
    assert ret == 0


# Tests signup and if only passwords that meet security criteria are allowed
def test_checkPassword():
    clearTables()
    too_short = ["username", "Asdfg@2", "Asdfg@2", "n"]
    too_long = ["username", "Asdfg@2qwerty", "Asdfg@2qwerty", "n"]
    no_capital = ["username", "asdfg@2qw", "asdfg@2qw", "n"]
    no_special = ["username", "Asdfg12qw", "Asdfg12qw", "n"]
    no_number = ["username", "Asdfg@!qw", "Asdfg@!qw", "n"]
    correct_input = [
        "username", "Password@2", "Password@2", "firstname", "lastname",
        "email@mail.com", "123-456-7890"
    ]
    exit = ["Exit"]
    set_keyboard_input(["Signup"] + too_short + too_long + no_capital +
                       no_special + no_number + correct_input + exit)
    main.main()

    users = allRecords("UserData")
    loginCreds = allRecords("UserLogin")
    contact = allRecords("Contacts")

    # Expected state: only 1 account in database, matches entered credentials
    assert getRecordCount("UserData") == 1
    assert getRecordCount("UserLogin") == 1
    assert getRecordCount("Contacts") == 1
    assert "firstname" in users[0]
    assert "lastname" in users[0]
    assert "username" in loginCreds[0]
    assert "Password@2" in loginCreds[0]
    assert "email@mail.com" in contact[0]
    assert "123-456-7890" in contact[0]


# Test an unsuccessful and successful login
@mock.patch("home.landingPage")
def test_main_login(landingPage_mock):
    set_keyboard_input([
        "Login", "username", "Password@2", "n", "username", "Password@2",
        "Exit", "Exit"
    ])
    main.main()
    landingPage_mock.assert_called()


#checks if the landing page and the new skills function is working correctly
def test_landingPage_newSkill():

    login = ["Login", "username", "Password@2", "3"]
    test_options = ["1", "2", "3", "4", "5"]
    bad_inputs = ["9", "a", "\n", "", "\0"]
    exit = ["Exit", "Exit", "Exit"]
    set_keyboard_input(login + test_options + bad_inputs + exit)
    output = get_display_output()
    main.main()
    assert output.count("This feature is under construction") > 0
