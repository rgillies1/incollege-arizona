from unittest import mock
from database import getRecordCount,authLogin,getSavedJobs
from jobSearch import jobSearch
from testing_base import get_display_output, set_keyboard_input, clearTables, addNewUsers
import main

def test_number_of_jobs():
  clearTables()
  addNewUsers()
  login = ["Login", "Dominos", "Dominos@2", "1", "2"]
  job_1 = ["Intern", "you intern", "Big Inc", "Tampa Fl", "$15/hour"]
  job_2 = ["Cook", "you cook", "Cookers Inc", "Tampa Fl", "$12/hour"]
  job_3 = ["Cook", "you cook", "Munchers Inc", "Tampa Fl", "$11/hour"]
  job_4 = ["Software_Intern", "you intern", "Softtech Inc", "Tampa Fl", "$18/hour"]
  job_5 = ["Data_Intern", "you intern", "Data Inc", "Tampa Fl", "$20/hour"]
  job_6 = ["Software_Engineer1", "you intern", "Micro Inc", "Tampa Fl", "$60/hour"]
  job_7 = ["Chef", "you cook", "Hub Inc", "Tampa Fl", "$19/hour"]
  job_8 = ["IT_Ops", "you fix stuff", "USF_Tampa", "Tampa Fl", "$11/hour"]
  job_9 = ["Designer", "you Design", "BMW_USA", "Tampa Fl", "$60/hour"]
  job_10 = ["Intern", "you intern", "Salesforce", "Seatle WA", "$57/hour"]
  exit = ["Exit", "Exit", "Exit"]

  set_keyboard_input(login + job_1 + ["2"] + job_2 + ["2"] + job_3 + ["2"] + job_4 + ["2"] + job_5 + ["2"] + job_6 + ["2"] + job_7 + ["2"] + job_8 + ["2"] + job_9 + ["2"] + job_10 + ["2"] + exit)
  main.main()

  assert getRecordCount("JobBoard") == 10
  

def test_applyJob():
  addNewUsers()
  login = ["Login", "Popeyes", "Popeyes@2", "1", "6"]
  apply_1 = ["2", "12/04/22", "01/01/23", "Cuz you guys are hiring"]  
  apply_2 = ["3", "12/04/22", "01/01/23", "Cuz you guys are hiring"]
  apply_3 = ["4", "12/04/22", "01/01/23", "Cuz you guys are hiring"] 
  exit = ["Exit", "Exit", "Exit", "Exit"]
  set_keyboard_input(login + apply_1 + apply_2 + apply_3 + exit)
  main.main()
  assert getRecordCount("Applications") == 3

def test_applied_jobs():
  authLogin("Popeyes","Popeyes@2")
  set_keyboard_input(["7","Exit"])
  output = get_display_output()
  jobSearch()
  assumedOutput = ["~~~~Job Board~~~~\n\n1. Job Board \n2. Post a job \n3. UsefulLinks \n4. ImportantLinks \n5. Delete a Job \n6. Apply for Job \n7. Applied Jobs \n8. Available Jobs \n9. Manage Saved Job  \nType \"Exit\" to go back\n",
                  "\nPlease select an option from the list above: ",
                  "\nYou have applied for the following jobs:",
                  "\t1. Cook",
                  "\t2. Cook",
                  "\t3. Software_Intern",
                   "",
                  "~~~~Job Board~~~~\n\n1. Job Board \n2. Post a job \n3. UsefulLinks \n4. ImportantLinks \n5. Delete a Job \n6. Apply for Job \n7. Applied Jobs \n8. Available Jobs \n9. Manage Saved Job  \nType \"Exit\" to go back\n",
                  "\nPlease select an option from the list above: ",]
  assert assumedOutput == output
  
def test_delete_jobs():
  login = ["Login", "Dominos", "Dominos@2", "1"]
  delete_4_jobs = ["5","1","5","1","5","1","5","1"]
  delete_then_go_back = ["5","0"]
  exit = ["Exit", "Exit", "Exit"]
  set_keyboard_input(login+delete_4_jobs+delete_then_go_back+exit)
  main.main()
  assert getRecordCount("JobBoard") == 6 and getRecordCount("Applications") == 3 #Applications should not disappear until applicant logs in next

def test_delete_applications():
  login = ["Login", "Popeyes", "Popeyes@2", "1"]
  exit = ["Exit", "Exit", "Exit"]
  set_keyboard_input(login+exit)
  main.main()
  assert getRecordCount("Applications") == 0

def test_save_jobs():
  login = ["Login", "Popeyes", "Popeyes@2", "1", "9"]
  save_jobs = ["1","1","1","3"]
  exit = ["Exit","Exit","Exit","Exit"]
  set_keyboard_input(login+save_jobs+exit)
  main.main()
  assert getSavedJobs(2) == [('5',"Data_Intern"),('7',"Chef")]

def test_delete_saved_jobs():
  login = ["Login", "Popeyes", "Popeyes@2", "1", "9"]
  save_jobs = ["2","2"]
  exit = ["Exit","Exit","Exit","Exit"]
  set_keyboard_input(login+save_jobs+exit)
  main.main()
  assert getSavedJobs(2) == [('5',"Data_Intern")] 