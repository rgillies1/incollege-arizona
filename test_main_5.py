from unittest import mock
from testing_base import get_display_output, set_keyboard_input, clearTables, addNewUsers
from database import getProfile, getJobExperience, getEducation, setProfile, setJobExperience, setEducation, addFriend, customCommand
import main

title = "testtitle"
major = "testmajor"
degree = "testdegree"
uni_name = "testuni_name"
year = 4
about = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
job_title = "testjob_title"
employer = "testemployer"
start_date = "teststart_date"
end_date = "testend_date"
location = "testlocation"
description = "- Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.\n- Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.\n- Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem."


def make_capital(str):
    r1, r2 = str.split("_")
    r1 = r1.capitalize()
    r2 = r2.capitalize()
    result = r1 + "_" + r2

    return result


def test_createProfile():
    clearTables()
    addNewUsers()

    login = ["Login", "Dominos", "Dominos@2", "6"]
    create_profile = ["3", "1"]
    set_title_and_about = ["1", title, "2", about, "Exit"]
    set_education = [
        "2", "1", uni_name, "2", major, "3", degree, "4", year, "Exit"
    ]
    set_job = [
        "3", "0", "1", "1", job_title, "2", employer, "3", start_date, "4",
        end_date, "5", location, "6", description, "Exit"
    ]
    set_job_2 = [
        "3", "0", "2", "1", job_title, "2", employer, "3", start_date, "4",
        end_date, "5", location, "6", description
    ]
    exit = ["Exit", "Exit", "Exit", "Exit", "Exit", "Exit", "Exit"]

    set_keyboard_input(login + create_profile + set_title_and_about +
                       set_education + set_job + set_job_2 + exit)

    main.main()

    profile = getProfile(1)
    education = getEducation(1)
    experience = getJobExperience(1)

    assert title.capitalize() in profile
    assert about in profile
    assert major.capitalize() in education
    assert make_capital(uni_name) in education
    assert degree in education
    assert year in education
    assert job_title in experience[0]
    assert employer in experience[0]
    assert start_date in experience[0]
    assert end_date in experience[0]
    assert location in experience[0]
    assert description in experience[0]
    assert job_title in experience[1]
    assert employer in experience[1]
    assert start_date in experience[1]
    assert end_date in experience[1]
    assert location in experience[1]
    assert description in experience[1]


def test_viewProfile():
    login = ["Login", "Dominos", "Dominos@2", "6"]
    exit = ["Exit", "Exit", "Exit"]

    set_keyboard_input(login + exit)

    main.main()

    output = get_display_output()
    output = ' '.join(
        output
    )  # Convert the program output into a single string, for the sake of my own sanity

    assert title.capitalize() in output
    assert about in output
    assert major.capitalize() in output
    assert make_capital(uni_name) in output
    assert degree in output
    assert str(year) in output
    assert job_title in output
    assert employer in output
    assert start_date in output
    assert end_date in output
    assert location in output
    assert description in output
    assert job_title in output
    assert employer in output
    assert start_date in output
    assert end_date in output
    assert location in output
    assert description in output


def test_friendProfile():
    addNewUsers()
    # To give the friend profile unique inputs, just reverse the strings of the current profile
    setProfile(title[::-1], about[::-1], 2)
    setEducation(uni_name[::-1], major[::-1], degree[::-1], year - 1, 2)
    customCommand(
        "INSERT INTO JobExperience (id,jobNum) VALUES ({0},{1});".format(2, 0))
    setJobExperience(0, job_title[::-1], employer[::-1], start_date[::-1],
                     end_date[::-1], location[::-1], description[::-1], 2)

    addFriend(2, 1)

    login = ["Login", "Dominos", "Dominos@2", "6", "1", "1"]
    exit = ["Exit", "Exit", "Exit", "Exit", "Exit"]

    set_keyboard_input(login + exit)

    main.main()
  
    output = get_display_output()
    output = ' '.join(output)

    assert len(output) > 0
    assert title[::-1].capitalize() in output
    assert about[::-1] in output
    assert major[::-1].capitalize() in output
    assert make_capital(uni_name[::-1]) in output
    assert degree[::-1] in output
    assert str(year) in output
    assert job_title[::-1] in output
    assert employer[::-1] in output
    assert start_date[::-1] in output
    assert end_date[::-1] in output
    assert location[::-1] in output
    assert description[::-1] in output
    assert job_title[::-1] in output
    assert employer[::-1] in output
    assert start_date[::-1] in output
    assert end_date[::-1] in output
    assert location[::-1] in output
    assert description[::-1] in output
