from unittest import mock
from database import getRecordCount,addFriend
from jobSearch import jobSearch
from testing_base import get_display_output, set_keyboard_input, clearTables, addNewUsers
import main

def test_message_standard_user():
  clearTables()
  addNewUsers()
  addNewUsers()
  addNewUsers()
  addFriend(1,2)
  login1 = ["Login", "Dominos", "Dominos@2", "9"]
  failedMessage1 = ["2","2","2"]#Try to send message to non-friend, should output "I'm sorry, you are not friends with this person"
  trueMessage2 = ["2","1","1","message sent"]#Send message to friend
  exit = ["Exit", "Exit","Exit"]
  

  set_keyboard_input(login1 + failedMessage1 + trueMessage2 + exit)
  output = get_display_output()
  main.main()
  assert output.count("I'm sorry, you are not friends with this person") == 1
  assert output.count("\n\nYou have 1 new message(s)! Selection option 9 to view them.") == 0
  assert getRecordCount("Messages") == 1

def test_plus_user():
  login = ["Login", "Popeyes", "Popeyes@2", "9"]
  trueMessage1 = ["1","1","2","reply"]#reply to message
  deleteMessage = ["1","1","1"]#delete message from friend
  trueMessage2 = ["2","2","2","message sent"]#Send message to non friend
  exit = ["Exit", "Exit", "Exit"]#exit
  set_keyboard_input(login + trueMessage1 + deleteMessage + trueMessage2 + exit)
  output = get_display_output()
  main.main()
  assert output.count("I'm sorry, you are not friends with this person") == 0
  assert output.count("\n\nYou have 1 new message(s)! Selection option 9 to view them.") == 1
  assert getRecordCount("Messages") == 2