from database import customCommand, newAccount,getRecordCount,tables,addContact
import builtins
  
    
def addNewUsers(i=-1):#Adds users one at a time.  if no user is specified it goes in order from list
  users = [["Dominos", "Dominos@2", "Mohammed", "Haque", "dom@dom.com", "000-000-0000"],
["Popeyes", "Popeyes@2", "David", "Hamilton", "pop@pop.com", "111-111-1111"],
["Pizzahut", "Pizzahut@2", "John", "Ha", "piz@piz.com", "222-222-2222"],
["Starbucks", "Starbucks@2", "Arthur", "Gusmao De Almeida", "star@star.com", "333-333-3333"],
["Dunkins", "Dunkins@2", "Raymond", "Gillies", "dunk@dunk.com", "444-444-4444"],
["Tacobell", "Tacobell@2", "Mo", "Haq", "taco@taco.com", "555-555-5555"],
["Wendys", "Wendys@2", "David", "H", "wen@wen.com", "666-666-6666"],
["Pollotrop", "Pollotrop@2", "Jacob", "Hawk", "pol@pol.com", "777-777-7777"],
["McDonalds", "McDonalds@2", "Lucas", "Firmino", "mc@mc.com", "888-888-8888"],
["BurgerKing", "BurgerKing@2", "Santi", "Pinkman", "burg@burg.com", "999-999-9999"]]
  if(i==-1):
    i=getRecordCount()
  a,b,c,d,e,f=users[i]
  newAccount(a,b,c,d,e,f)

def addContacts(i=-1):
  users = [["Mohammed", "Haque", "dom@dom.com", "100-000-0000"],
["David", "Hamilton", "pop@pop.com", "211-111-1111"],
["John", "Ha", "piz@piz.com", "322-222-2222"],
["Arthur", "Gusmao De Almeida", "star@star.com", "433-333-3333"],
["Raymond", "Gillies", "dunk@dunk.com", "544-444-4444"],
["Mo", "Haque", "taco@taco.com", "655-555-5555"],
["David", "H", "wen@wen.com", "766-666-6666"],
["Jacob", "Hawk", "pol@pol.com", "776-777-7777"],
["Lucas", "Firmino", "mc@mc.com", "889-888-8888"],
["Santi", "Pinkman", "burg@burg.com", "990-999-9999"]]
  if(i==-1):
    i=getRecordCount("Contacts")
  a,b,c,d=users[i]
  addContact(a,b,c,d)
  

def clearTable(table):#Input table name to drop table and then it is rebuilt
  customCommand("DROP TABLE IF EXISTS {0};".format(table))
  tables()
  
def clearTables():#Clears and renews all tables
  customCommand("DROP TABLE IF EXISTS UserLogin;")
  customCommand("DROP TABLE IF EXISTS ActiveUsers;")
  customCommand("DROP TABLE IF EXISTS UserData;")
  customCommand("DROP TABLE IF EXISTS UserSettings;")
  customCommand("DROP TABLE IF EXISTS Contacts;")
  customCommand("DROP TABLE IF EXISTS FriendNetwork;")
  customCommand("DROP TABLE IF EXISTS FriendRequest;")
  customCommand("DROP TABLE IF EXISTS JobBoard;")
  customCommand("DROP TABLE IF EXISTS Profiles;")
  customCommand("DROP TABLE IF EXISTS JobExperience;")
  customCommand("DROP TABLE IF EXISTS Education;")
  tables()
'''
*Retrieved: https://gist.github.com/mauricioaniche/671fb553a81df9e6b29434b7e6e53491
*Tutorial: https://www.youtube.com/watch?v=tBAj2FqgIwg
*Used for pytest inputs and outputs
'''

input_values = []
print_values = []


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs