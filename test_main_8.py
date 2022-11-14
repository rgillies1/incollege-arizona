from unittest import mock
from testing_base import get_display_output, set_keyboard_input, clearTables, addNewUsers
from database import getProfile, sendNotification, newJobPost, apply, removeJobPost
import main
from ProfileNotification import P_Notifications

#Unable to test notification on users who have not registered for jobs within 7 days, because we cannot change the system time on replit

def test_applied_jobs():
  clearTables()
  addNewUsers()
  login1 = ["Login", "Dominos", "Dominos@2", "1"]
  exit = ["Exit", "Exit", "Exit"]
  
  set_keyboard_input(login1 + exit)
  main.main()
  output = get_display_output()
  assert "\nYou have applied for 0 job(s).\n" in output

def test_delete_job_notifications():
  clearTables()
  addNewUsers()
  addNewUsers()
  
  newJobPost("pizza", "", "", "", "", 1)
  login1 = ["Login", "Popeyes", "Popeyes@2"]
  login2 = ["Login", "Dominos", "Dominos@2"]
  apply1 = ["1", "6", "1", "12/12/2022", "01/13/2023", ""]
  exit1 = ["Exit", "Exit", "Exit"]
  exit2 = ["Exit", "Exit"]
  deleteJob = ["1", "5", "1"]

  set_keyboard_input(login1 + apply1 + exit1 + login2 + deleteJob + exit2 + login1 + exit2)
  main.main()
  output = get_display_output()
  #assert [] == output
  assert "1. The following job post that you applied to was deleted: pizza" in output

#Notify students about creating a profile
def test_user_who_have_notCreate_profile():
  clearTables()
  addNewUsers()
  login1 = ["Login", "Dominos", "Dominos@2"]
  exit = ["Exit"]
  exit2 = ["Exit", "Exit"]

  set_keyboard_input(login1 + exit + login1 + exit2)
  main.main()
  output = get_display_output()
  assert "2. Dont forget to create a profile!" in output and "1. Dont forget to create a profile!" in output

#Notify new students
def test_new_user_welcome():
  clearTables()
  addNewUsers()
  login1 = ["Login", "Dominos", "Dominos@2"]
  exit = ["Exit", "Exit"]

  set_keyboard_input(login1 + exit)
  main.main()
  output = get_display_output()
  assert "1. Mohammed Haque (Dominos) has joined InCollege!" in output

#Notify new jobs
def test_new_user_Jobs():
  clearTables()
  addNewUsers()
  addNewUsers()
  newJobPost("pizza", "", "", "", "", 1)
  login1 = ["Login", "Dominos", "Dominos@2"]
  exit = ["Exit", "Exit"]

  set_keyboard_input(login1 + exit)
  main.main()
  output = get_display_output()
  assert "3. A new job has been posted!" in output
