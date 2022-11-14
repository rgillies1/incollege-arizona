from unittest import mock
from database import getRecordCount, allRecords, setEducation, getFriends, newFriendRequest
from testing_base import get_display_output, set_keyboard_input, clearTables, clearTable
import main


def test_numOfAccts():
    clearTables()
    set_keyboard_input(
        [
            "Signup", "Dominos", "Dominos@2", "Dominos@2", "Mohammed", "Haque",
            "dom@dom.com", "000-000-0000", "2", "Signup", "Popeyes", "Popeyes@2",
            "Popeyes@2", "David", "Hamilton", "pop@pop.com", "111-111-1111",
            "1", "Signup", "Pizzahut", "Pizzahut@2", "Pizzahut@2", "John", "Ha",
            "piz@piz.com", "222-222-2222", "2", "Signup", "Starbucks",
            "Starbucks@2", "Starbucks@2", "Arthur", "Gusmao De Almeida",
            "star@star.com", "333-333-3333", "2", "Signup", "Dunkins", "Dunkins@2",
            "Dunkins@2", "Raymond", "Gillies", "dunk@dunk.com", "444-444-4444",
            "1", "Signup", "Tacobell", "Tacobell@2", "Tacobell@2", "Mo", "Haq",
            "taco@taco.com", "555-555-5555", "1", "Signup", "Wendys", "Wendys@2",
            "Wendys@2", "Dave", "Ham", "wen@wen.com", "666-666-6666", "1", "Signup",
            "Pollotrop", "Pollotrop@2", "Pollotrop@2", "Jon", "H",
            "pol@pol.com", "777-777-7777", "2", "Signup", "McDonalds",
            "McDonalds@2", "McDonalds@2", "Art", "Almieda De Gusmao",
            "mc@mc.com", "888-888-8888", "2", "Signup", "BurgerKing",
            "BurgerKing@2", "BurgerKing@2", "Santi", "Pinkman",
            "burg@burg.com", "999-999-9999", "1", "Signup", "Exit"
        ]
    )  #Was missing double passwords and some lastnames got doubled which isnt allowed because last names need to be unique.

    main.main()
    assert getRecordCount() == 10 


def test_friendSearchLastName():
    clearTable("FriendRequest")
    login = ["Login", "Dominos", "Dominos@2", "4"]
    search_by_last = ["1", "Hamilton", "1"]
    exit = ["4", "Exit", "Exit"]

    set_keyboard_input(login + search_by_last + exit)
    main.main()

    requests = allRecords("FriendRequest")

    assert (1, 2) in requests


def test_friendSearchMajor():
    clearTable("FriendRequest")
    setEducation("USF", "Computer Science", "Computer Science", 4, 2)

    login = ["Login", "Dominos", "Dominos@2", "4"]
    search_by_major = ["2", "Computer Science", "1"]
    exit = ["4", "Exit", "Exit"]

    set_keyboard_input(login + search_by_major + exit)
    main.main()

    requests = allRecords("FriendRequest")

    assert (1, 2) in requests


def test_friendSearchUni():
    clearTable("FriendRequest")

    login = ["Login", "Dominos", "Dominos@2", "4"]
    search_by_uni = ["3", "USF", "1"]
    exit = ["4", "Exit", "Exit"]
    set_keyboard_input(login + search_by_uni + exit)
    main.main()

    requests = allRecords("FriendRequest")

    assert (1, 2) in requests


def test_friendRequestAccept():
    clearTable("FriendRequest")
    newFriendRequest(2, 1)
    requests = allRecords("FriendRequest")

    assert (1, 2) in requests

    login = ["Login", "Popeyes", "Popeyes@2", "5"]
    add_friend = ["3", "1", "1"]
    exit = ["4", "Exit", "Exit"]

    set_keyboard_input(login + add_friend + exit)

    main.main()

    friends_1 = getFriends(1)[0]
    friends_2 = getFriends(2)[0]

    assert 2 in friends_1 and 1 in friends_2
