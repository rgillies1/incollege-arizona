from unittest import mock
from testing_base import get_display_output, set_keyboard_input, clearTables, addNewUsers, addContacts
from database import allRecords
import main


def test_main_and_video_then_exit():  #Display the new login space
    set_keyboard_input(["Video", "Exit"])
    main.main()

    output = get_display_output()
    assert "Video is now playing...\n" in output


def test_connect_users():
    clearTables()
    addNewUsers()
    addNewUsers()

    for _ in range(8):
        addContacts()

    login = ["Login", "Dominos", "Dominos@2", "2"]
    part_of_system = ["David", "Hamilton", "y"]
    not_part_contact = ["Santi", "Pinkman", "y", "y"]
    not_part_no_contact = [
        "Walter", "White", "y", "123-456-7890", "mail@mail.com", "y"
    ]
    bad_input = ["\n", "\n", "y", "", "", "y", "0", "1", "y", "'", "/", "0"]
    exit = ["n", "Exit", "Exit"]

    set_keyboard_input(login + part_of_system + not_part_contact +
                       not_part_no_contact + bad_input + exit)
    main.main()

    output = get_display_output()

    foundAndInSystem = "They are a part of the InCollege system!" in output
    foundButNotInSystem = "Contact found but they are not yet part of the InCollege system" in output
    notFound = "They are not yet a part of the InCollege system yet!" in output

    assert foundAndInSystem and foundButNotInSystem and notFound


def test_job_posting(capsys):
    login = ["Login", "Dominos", "Dominos@2", "1", "2"]
    job_1 = ["Intern", "you intern", "Big Inc", "Tampa Fl", "$15/hour"]
    job_2 = ["Cook", "you cook", "Cookers Inc", "Tampa Fl", "$12/hour"]
    bad_job = ["\n", "\0", "'", "\"", "null"]
    exit = ["9", "Exit", "Exit"]

    set_keyboard_input(login + job_1 + ["2"] + job_2 + ["2"] + bad_job + exit)
    main.main()

    jobBoard = allRecords("JobBoard")

    job_1_t = tuple(job_1 + ["Mohammed Haque"])
    job_2_t = tuple(job_2 + ["Mohammed Haque"])

    assert job_1_t in jobBoard and job_2_t in jobBoard
