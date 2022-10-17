#import pytest
from unittest import mock
import main
from tud_test_base import get_display_output, set_keyboard_input, clearFile, writeToFile, appendToFile
import os


# So long as we can exit the program, them whether the output is correct should be tested manually
@mock.patch("main.importantlinks")
def test_importantLinks(importantlinks_mock):  #Display the new login space
    set_keyboard_input(["importantlinks", "10", "Exit"])
    main.main()
    importantlinks_mock.assert_called()


def test_importantLinks2():
    clearFile("userList.txt")
    writeToFile(
        "userList.txt",
        "Dominos, Dominos@2, Mohammed, Haque, English, History, USF\n")
    appendToFile(
        "userList.txt",
        "Popeyes, Popeyes@2, David, Hamilton, English, ComputerEngineering, FSU\n"
    )
    appendToFile(
        "userList.txt",
        "Pizzahut, Pizzahut@2, John, Ha, English, ComputerScience, USF\n")
    appendToFile(
        "userList.txt",
        "Starbucks, Starbucks@2, Arthur, Gusmao De Almeida, English, ComputerScience, UF\n"
    )
    appendToFile(
        "userList.txt",
        "Dunkins, Dunkins@2, Raymond, Gillies, English, PoliticalScience, UT\n"
    )
    set_keyboard_input([
        "Login", "Pizzahut", "Pizzahut@2", "4", "1", "5", "0", "4", "9", "1",
        "10", "10", "Exit"
    ])
    main.main()
    output = get_display_output()

    copyright_notice = "\nWe are committed to safeguarding the privacy of InCollege users. This notice applies where we are acting as a data controller with respect to the personal data of such persons; in other words, where we determine the purposes and means of the processing of that personal data.Our website incorporates privacy controls which affect how we will process your personal data.You can access the privacy controls via privacy policy page\n"

    privacy_notice = "\nThe privacy policy for In College describes how and why we might collect store, use and/or share your information when you use our services(such as visiting our website or engaging with us in other related ways). We collect personal information that you voluntarily provide to us when you register to use our services, express an interest in using our services or you participate in the activities on the services we provide. These informations include but are not limited to names, phone numbers, email address, job  titles and passwords. We process your information to provide, improve and administer our services, communicate with you, for security and fraud prevention(with your consent)\n"

    assert copyright_notice in output and privacy_notice in output
    # We are logged in as John Ha, who we made the 3rd user. The 5th arg of getUserInfo is language
    assert "Spanish" in main.getUserInfo()[4][2]


def test_usefulLinks():
    set_keyboard_input([
        "UsefulLinks", "4", "UsefulLinks", "1", "3", "UsefulLinks", "1", "8",
        "5", "Exit"
    ])
    main.main()
    output = get_display_output()

    tempText = "Under Construction"
    aboutText = "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide"
    genHeaderText = "********** USEFUL LINKS: GENERAL **********"

    assert tempText in output and aboutText in output and genHeaderText in output


def test_userSettings():
    set_keyboard_input([
        "Login", "Pizzahut", "Pizzahut@2", "4", "5", "0", "1", "2", "3", "4",
        "10", "10", "Exit"
    ])
    main.main()

    userSettings = main.getUserSettings("Pizzahut")
    assert userSettings["sms_notif"] == False
    assert userSettings["email"] == False
    assert userSettings["targets_advertising"] == False
