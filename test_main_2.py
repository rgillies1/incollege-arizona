#import pytest

import main
from tud_test_base import get_display_output, set_keyboard_input, clearFile, writeToFile, appendToFile
import os


def test_main_and_video_then_exit():  #Display the new login space
    set_keyboard_input(["Video", "Exit"])
    main.main()

    output = get_display_output()
    assert "Video is now playing...\n" in output


def test_connect_users():  #Test the connect uses function and inviting option
    clearFile("userList.txt")
    writeToFile(
        "userList.txt",
        "Dominos, Dominos2@, Dom, Inos, English, Culinary Arts, USF\n")
    appendToFile(
        "userList.txt",
        "Popeyes, Popeyes@2, David, Hamilton, English, ComputerEngineering, FSU\n"
    )
    set_keyboard_input([
        "Login", "Dominos", "Dominos2@", "2", "David", "Hamilton", "y",
        "Walter", "White", "n", "y", "MF", "DOOM", "y", "Exit"
    ])
    main.main()
    output = get_display_output()

    foundAndInSystem = "They are a part of the InCollege system!" in output
    foundButNotInSystem = "Contact found but they are not yet part of the InCollege system" in output
    notFound = "They are not yet a part of the InCollege system yet!" in output

    assert foundAndInSystem and foundButNotInSystem and notFound


#Test Job Posting Creation
def test_job_posting():
    clearFile("jobList.txt")

    set_keyboard_input([
        "Login", "Dominos", "Dominos2@", "1", "2", "Intern", "you intern",
        "Big Inc", "Tampa Fl", "$15/hour", "2", "Cook", "you cook",
        "Cookers Inc", "Tampa Fl", "$12/hour", "2", "Intern", "you intern",
        "Big Inc", "Tampa Fl", "$15/hour", "2", "Cook", "you cook",
        "Cookers Inc", "Tampa Fl", "$12/hour", "2", "Intern", "you intern",
        "Big Inc", "Tampa Fl", "$15/hour", "9", "Exit", "Exit"
    ])
    main.main()

    with open("jobList.txt", "r") as jobs:
        lines = jobs.readlines()
        assert lines.count(
            "Intern| you intern| Big Inc| Tampa Fl| $15/hour| None\n") == 3
        assert lines.count(
            "Cook| you cook| Cookers Inc| Tampa Fl| $12/hour| None\n") == 2
