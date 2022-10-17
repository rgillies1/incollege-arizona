#import pytest
import main
from tud_test_base import get_display_output, set_keyboard_input, clearFile, writeToFile, appendToFile
import os


def test_numOfAccts():  #attempts to create 11 accs, only 10 should be created
    clearFile("userList.txt")
    clearFile("friendList.txt")
    clearFile("friendRequest.txt")
    f = open("friendRequest.txt", "w")
    f.write("Dominos,Popeyes")
    f.close()

    set_keyboard_input([
        "Signup", "Dominos", "Dominos@2", "Dominos@2", "Mohammed", "Haque",
        "History", "USF", "Signup", "Popeyes", "Popeyes@2", "Popeyes@2",
        "David", "Hamilton", "ComputerEngineering", "FSU", "Signup",
        "Pizzahut", "Pizzahut@2", "Pizzahut@2", "John", "Ha",
        "ComputerScience", "USF", "Signup", "Starbucks", "Starbucks@2",
        "Starbucks@2", "Arthur", "Gusmao De Almeida", "ComputerScience", "UF",
        "Signup", "Dunkins", "Dunkins@2", "Dunkins@2", "Raymond", "Gillies",
        "PoliticalScience", "UT", "Signup", "Tacobell", "Tacobell@2",
        "Tacobell@2", "Mo", "Haque", "Electrical", "UF", "Signup", "Wendys",
        "Wendys@2", "Wendys@2", "David", "H", "Mechanical", "FIU", "Signup",
        "Pollotrop", "Pollotrop@2", "Pollotrop@2", "Jacob", "Hawk",
        "ComputerScience", "USF", "Signup", "McDis", "McDonalds@2",
        "McDonalds@2", "Lucas", "Firmino", "History", "UCF", "Signup",
        "BurgerKing", "BurgerKing@2", "BurgerKing@2", "Santi", "Pinkman",
        "Economics", "USF", "Signup", "LinkedIn", "LinkedIn@2", "LinkedIn@2",
        "Larry", "Jesus", "Bio", "FSU", "Exit"
    ])
    main.main()
    # Checks list of usernames, should be of length 10
    assert len(main.getUserInfo()[0]) == 10


def test_friendSearchLastName():
    clearFile("friendRequest.txt")
    set_keyboard_input([
        "Login", "Dominos", "Dominos@2", "5", "1", "Gillies", "1", "1",
        "Gillies", "1", "4", "Exit"
    ])
    main.main()

    with open("friendRequest.txt", "r") as requests:
        assert requests.readlines().count("Dominos,Dunkins\n") == 1


def test_friendSearchMajor():
    set_keyboard_input([
        "Login", "Dominos", "Dominos@2", "5", "2", "Mechanical", "1", "2",
        "Mechanical", "1", "4", "Exit"
    ])
    main.main()

    with open("friendRequest.txt", "r") as requests:
        assert requests.readlines().count("Dominos,Wendys\n") == 1


def testFriendUni():
    set_keyboard_input([
        "Login", "Dominos", "Dominos@2", "5", "3", "UCF", "1", "3", "UCF", "1",
        "4", "Exit"
    ])
    main.main()

    with open("friendRequest.txt", "r") as requests:
        assert requests.readlines().count("Dominos,McDis\n") == 1


def test_friendRequest():
    clearFile("friendRequest.txt")
    writeToFile("friendRequest.txt", "Dominos,Popeyes")
    set_keyboard_input([
        "Login", "Dominos", "Dominos@2", "6", "3", "1", "1", "4", "Exit",
        "Exit"
    ])
    main.main()

    isFriends1, isFriends2 = False, False

    list = open("friendList.txt", "r")
    for line in list:
        if line == "Dominos,Popeyes\n":
            isFriends1 = True
        if line == "Popeyes,Dominos\n":
            isFriends2 = True

    list.close()
    assert isFriends1 and isFriends2


def test_friendNetwork():
    clearFile("friendList.txt")
    f = open("friendList.txt", "w")
    f.write("Dominos,Popeyes\n")
    f.write("Popeyes,Dominos")
    f.close()

    set_keyboard_input(
        ["Login", "Dominos", "Dominos@2", "6", "2", "1", "4", "Exit", "Exit"])
    main.main()

    isRemoved1, isRemoved2 = False, False

    list = open("friendList.txt", "r")
    for line in list:
        if line == "Dominos,\n":
            isRemoved1 = True
        if line == "Popeyes,\n":
            isRemoved2 = True

    list.close()

    assert isRemoved1 and isRemoved2
