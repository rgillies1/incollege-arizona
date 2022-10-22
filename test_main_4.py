from unittest import mock
from testing_base import get_display_output, set_keyboard_input,clearTables
import main

def test_numOfAccts():
  clearTables()
  set_keyboard_input([
    ["Signup","Dominos", "Dominos@2", "Mohammed", "Haque", "dom@dom.com", "000-000-0000",
    "Signup","Popeyes", "Popeyes@2", "David", "Hamilton", "pop@pop.com", "111-111-1111",
    "Signup","Pizzahut", "Pizzahut@2", "John", "Ha", "piz@piz.com", "222-222-2222",
    "Signup","Starbucks", "Starbucks@2", "Arthur", "Gusmao De Almeida", "star@star.com", "333-333-3333",
    "Signup","Dunkins", "Dunkins@2", "Raymond", "Gillies", "dunk@dunk.com", "444-444-4444",
    "Signup","Tacobell", "Tacobell@2", "Mo", "Haque", "taco@taco.com", "555-555-5555",
    "Signup","Wendys", "Wendys@2", "David", "H", "wen@wen.com", "666-666-6666",
    "Signup","Pollotrop", "Pollotrop@2", "Jacob", "Hawk", "pol@pol.com", "777-777-7777",
    "Signup","McDonalds", "McDonalds@2", "Lucas", "Firmino", "mc@mc.com", "888-888-8888",
    "Signup","BurgerKing", "BurgerKing@2", "Santi", "Pinkman", "burg@burg.com", "999-999-9999",
    "Signup", "Exit"
    ]
    ])
  main.main()
  assert getRecordCount() == 10

