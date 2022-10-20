import sqlite3
import random
import os
#This file verifies the existance of the databases needed for the application
def tables(connection = sqlite3.connect("inCollege.db")):
  #No cookie should be on this device right now
  if os.path.exists("cookie"):
    os.remove("cookie")  
  #User Login info
  connection.execute("""CREATE TABLE IF NOT EXISTS UserLogin 
  (id INTEGER PRIMARY KEY, 
  username TEXT UNIQUE, 
  password TEXT);""")

  #Actively logged in users info, dropped when restarted and then added.  Only one that has this happen
  connection.execute("""DROP TABLE IF EXISTS ActiveUsers""")
  connection.execute("""CREATE TABLE IF NOT EXISTS ActiveUsers
  (id INTEGER PRIMARY KEY, 
  cookie TEXT UNIQUE, 
  FOREIGN KEY(id) REFERENCES UserLogin(id));""")
  
  #User data info
  connection.execute("""CREATE TABLE IF NOT EXISTS UserData 
  (id INTEGER UNIQUE, 
  firstName TEXT, 
  lastName TEXT UNIQUE, 
  language TEXT DEFAULT 'ENGLISH', 
  major TEXT, 
  college TEXT, 
  FOREIGN KEY(id) REFERENCES UserLogin(id));""")

  #User settings info
  connection.execute("""CREATE TABLE IF NOT EXISTS UserSettings 
  (id INTEGER UNIQUE, 
  emailNotif INTEGER DEFAULT 1 NOT NULL,
  smsNotif INTEGER DEFAULT 1 NOT NULL, 
  targetAds INTEGER DEFAULT 1 NOT NULL, 
  language TEXT DEFAULT 'en-us' NOT NULL, 
  FOREIGN KEY(id) REFERENCES UserLogin(id));""")

  #Contact information 
  connection.execute("""CREATE TABLE IF NOT EXISTS Contacts
  (id INTEGER UNIQUE, 
  firstName TEXT, 
  lastName TEXT, 
  email TEXT UNIQUE, 
  phone TEXT UNIQUE, 
  FOREIGN KEY(id) REFERENCES UserLogin(id));""")#Should only have ID if there is an account connected to contact

  #Friend Network info
  connection.execute("""CREATE TABLE IF NOT EXISTS FriendNetwork
  (id INTEGER UNIQUE, 
  friendIds TEXT DEFAULT '' NOT NULL, --Each friend ID should be seperated by a comma
  FOREIGN KEY(id) REFERENCES UserLogin(id));""")#Each friend ID should be seperated by a comma

  #Friend requst info
  connection.execute("""CREATE TABLE IF NOT EXISTS FriendRequest 
  (sendId INTEGER, 
  recieveId INTEGER, 
  FOREIGN KEY(sendId) REFERENCES UserLogin(id),
  FOREIGN KEY(recieveId) REFERENCES UserLogin(id));""")

  #Job board info
  connection.execute("""CREATE TABLE IF NOT EXISTS JobBoard 
  (position TEXT NOT NULL, 
  description TEXT NOT NULL, 
  employer TEXT NOT NULL, 
  location TEXT NOT NULL, 
  salary TEXT NOT NULL,
  poster TEXT NOT NULL);""")
  
  connection.commit()


def customCommand(cmd,connection = sqlite3.connect("inCollege.db")):#executes custom command
  if(cmd[0:6].upper()=='SELECT'):
    return connection.execute(cmd).fetchall()
  connection.execute(cmd)
  connection.commit()

def getRecordCount(table="UserLogin",connection = sqlite3.connect("inCollege.db")):#Returns number of records in specified table, default is number of users
  return connection.execute("SELECT COUNT(*) FROM "+table+";").fetchone()[0]

def allRecords(table,connection = sqlite3.connect("inCollege.db")):#Returns all records in a list of tuples
  return connection.execute("SELECT * FROM "+table+";").fetchall()

def exist(table,col,val,connection = sqlite3.connect("inCollege.db")):#Returns true if val is in list of values in col
  return (val) in connection.execute("SELECT "+col+" FROM "+table+";").fetchall()

def newAccount(username,password,firstName,lastName,major,college,email,phone,connection = sqlite3.connect("inCollege.db")):
  #Saves Login Info
  connection.execute("INSERT INTO UserLogin (username,password) VALUES ('{0}','{1}');".format(username,password))
  #Retrieves UserId
  userId = connection.execute("SELECT id FROM UserLogin WHERE username = '{0}';".format(username)).fetchone()[0]
  #Saves User Data
  connection.execute("INSERT INTO UserData (id,firstName,lastName,major,college) VALUES ({0},'{1}','{2}','{3}','{4}')".format(userId,firstName,lastName,major,college))
  #Creates and defaults user Settings
  connection.execute("INSERT INTO UserSettings (id) VALUES ({0})".format(userId))
  #Makes sure contact information exists
  if(exist(table="Contacts",col="email",val=email)):
    connection.update("UPDATE Contacts SET id = {0}, phone = '{1}' WHERE email = '{2}'".format(userId,phone,email))
  elif(exist(table="Contacts",col="phone",val=phone)):
    connection.update("UPDATE Contacts SET id = {0}, email = '{1}' WHERE phone = '{2}'".format(userId,email,phone))
  else:
    connection.execute("INSERT INTO Contacts (id,firstName,lastName,email,phone) VALUES ({0},'{1}','{2}','{3}','{4}')".format(userId,firstName,lastName,email,phone))
  #Creates friend records
  connection.execute("INSERT INTO FriendNetwork (id) VALUES ({0});".format(userId))
  connection.commit()

def authLogin(username,password,connection = sqlite3.connect("inCollege.db")):#Authenticates User and creates Cookie for future authentication
  if(password == connection.execute("SELECT password FROM UserLogin WHERE username = '{0}'".format(username)).fetchone()[0]):
    userId = connection.execute("SELECT id FROM UserLogin WHERE username = '{0}';".format(username)).fetchone()[0]
    
    if(connection.execute("SELECT * FROM ActiveUsers WHERE id = {0};".format(userId)).fetchall()!=[]):#User is logged on already
      return -1
    cookieHash = random.getrandbits(128)#Gets a random hash
    connection.execute("INSERT INTO ActiveUsers (id,cookie) VALUES ({0},'{1}');".format(userId,cookieHash))#Puts random hash in db
    cookie = open("cookie", "w")
    cookie.write(str(cookieHash))
    cookie.close()
    connection.commit()
    return 1
  return 0
  
def authUser(cookie=0,connection = sqlite3.connect("inCollege.db")):#Authenticates Logged In User, returns userId if cookie corresponds to hash
  try:
    cookieFile=False
    if(cookie==0):#User cookie, reason not checking for path because we may not be checking for current cookie 
      cookie=open("cookie","r").read()
      cookieFile=True
    userId=connection.execute("SELECT id FROM ActiveUsers WHERE cookie = '{0}'".format(cookie)).fetchone()[0]
    if(userId==None):
      print("Authentication failed")
      if(cookieFile):#If cookie file exists but doesn't authenticate, remove file
        os.remove("cookie")  
      return (False,None)
    return (True,userId)
  except:
    print("Authentication failed")
    return (False,None)

def logout(userId=-1, connection = sqlite3.connect("inCollege.db")):#Logs user out and clears active user cookie
  if(userId==-1):
    userId=authUser()[1]
  if(userId==None):#Not authenticated
    pass
  cookie=open("cookie","r").read()
  connection.execute("DELETE FROM ActiveUsers WHERE cookie = '{0}';".format(cookie))
  if os.path.exists("cookie"):
    os.remove("cookie")  
  connection.commit()


def updateUser(table,col,val,userId=-1,connection = sqlite3.connect("inCollege.db")):#Update user values with provided userId
  if(userId==-1):#UserId not Provided
    userId=authUser()[1]
  if(userId==None):#Not authenticated
    pass
  if(type(val)==type("")):#Are we updating a text value or int value
    connection.execute("UPDATE {0} SET {1} = '{2}' WHERE id = {3}".format(table,col,val,userId))
  else:
    connection.execute("UPDATE {0} SET {1} = {2} WHERE id = {3}".format(table,col,val,userId))
  connection.commit()

def findUser(lastName="%",university="%",major="%",connection = sqlite3.connect("inCollege.db")):#Find user in UserData
  return connection.execute("SELECT id, firstName, lastName FROM UserData WHERE lastName LIKE '{0}' AND college LIKE '{1}' AND major LIKE '{2}';".format(lastName,university,major)).fetchall()#'%' is wildcard in SQL

def findContact(firstName="%",lastName="%",connection = sqlite3.connect("inCollege.db")):#Find contact in Contacts
  return connection.execute("SELECT id, firstName, lastName FROM ContactList WHERE lastName = '{0}' AND firstName = '{1}';".format(lastName,firstName)).fetchone()


def addContact(firstName,lastName,phone,email,connection = sqlite3.connect("inCollege.db")):#Adds mew contact to Contacts
  connection.execute("INSERT INTO Contacts (firstName,lastName,email,phone) VALUES ('{0}','{1}','{2}','{3}')".format(firstName,lastName,email,phone))
  connection.commit()

def newJobPost(jobTitle,jobDescription,jobEmployer,jobLocation,jobSalary,userId=-1,connection = sqlite3.connect("inCollege.db")):#Posts new job
  if(userId==-1):
    userId=authUser()[1]
  if(userId==None):
    pass
  name = connection.execute("SELECT firstName,lastName FROM UserData WHERE id = {0};".format(userId)).fetchone()
  fullName = name[0]+" "+name[1]
  connection.execute("INSERT INTO JobBoard (position,description,employer,location,salary,poster) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}');".format(jobTitle,jobDescription,jobEmployer,jobLocation,jobSalary,fullName))
  connection.commit()

def newFriendRequest(friendId,userId=-1,connection = sqlite3.connect("inCollege.db")):#New friend request
  if(userId==-1):
    userId=authUser()[1]
  if(userId==None or userId==friendId):
    pass
  requestCheck1 = connection.execute("SELECT sendId,recieveId FROM FriendRequest WHERE sendId = {0} AND recieveId = {1};".format(userId,friendId)).fetchone()
  requestCheck2 = connection.execute("SELECT sendId,recieveId FROM FriendRequest WHERE sendId = {0} AND recieveId = {1};".format(friendId,userId)).fetchone()
  
  friendIdStr=str(friendId)
  friendCheck = connection.execute("SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(userId)).fetchone()[0]
  if(friendCheck==None):
    friendCheck=True
  elif((friendIdStr in friendCheck)):#CHECK TO SEE IF friendId is substring in friendCheck
    print("You are already friends")
    friendCheck=False
  else:
    friendCheck=True
  #print(requestCheck1,requestCheck2,friendCheck,friendIdStr)
  if(requestCheck1 == None and friendCheck and requestCheck2 == None):#if there is no existing request and they aren't already friends
    connection.execute("INSERT INTO FriendRequest (sendId,recieveId) VALUES ({0},{1});".format(userId,friendId))
  connection.commit()

def getFriendRequests(userId=-1,connection = sqlite3.connect("inCollege.db")):#returns all friend requests
  if(userId==-1):
    userId=authUser()[1]
  if(userId == None):
    pass
  friendRequestList = connection.execute("SELECT sendId FROM FriendRequest WHERE recieveId = {0};".format(userId)).fetchall()#Retrieves all friendIds
  #print(friendRequestList)
  if(friendRequestList==None):
    return []
  for i in range(0,len(friendRequestList)):#makes each value integer and gets corresponding username
    friendUser = connection.execute("SELECT username FROM UserLogin WHERE id = {0};".format(friendRequestList[i][0])).fetchone()[0]
    friendRequestList[i]=(friendUser,friendRequestList[i][0])
  return friendRequestList

def removeFriendRequest(sendId,recieveId=-1,connection = sqlite3.connect("inCollege.db")):#Removes specified friend request
  if(recieveId==-1):
    recieveId=authUser()[1]
  if(recieveId==None):
    pass
  connection.execute("DELETE FROM FriendRequest WHERE sendId = {0} AND recieveId = {1};".format(sendId,recieveId))
  connection.commit()

def addFriend(friendId,userId=-1,connection = sqlite3.connect("inCollege.db")):#Adds new friend
  if(userId==-1):
    userId=authUser()[1]
  if(userId==None):
    pass
  myFriends = connection.execute("SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(userId)).fetchone()[0]
  friendFriends = connection.execute("SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(friendId)).fetchone()[0]
  if(myFriends == ""):
    myFriends=str(friendId)
  else:
    myFriends+=","+str(friendId)
  if(friendFriends == ""):
    friendFriends=str(userId)
  else:
    friendFriends+=","+str(userId)
  connection.execute("UPDATE FriendNetwork SET friendIds = '{0}' WHERE id = {1};".format(myFriends,userId))
  connection.execute("UPDATE FriendNetwork SET friendIds = '{0}' WHERE id = {1};".format(friendFriends,friendId))
  connection.commit()

def getFriends(userId=-1,connection = sqlite3.connect("inCollege.db")):#Returns user's friends
  if(userId==-1):
    userId=authUser()[1]
  if(userId == None):
    pass
  friendList = connection.execute("SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(userId)).fetchone()[0]#Retrieves all friendIds
  if(friendList==""):
    return []
  friendList=friendList.split(",")#Splits into list
  for i in range(0,len(friendList)):#makes each value integer and gets corresponding username
    friendUser = connection.execute("SELECT username FROM UserLogin WHERE id = {0};".format(friendList[i])).fetchone()[0]
    friendList[i]=(friendUser,int(friendList[i]))
  return friendList

def removeFriend(friendId,userId=-1,connection = sqlite3.connect("inCollege.db")):#Removes specified friend
  if(userId==-1):
    userId=authUser()[1]
  if(userId==None):
    pass
  myFriends = connection.execute("SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(userId)).fetchone()[0]
  friendFriends = connection.execute("SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(friendId)).fetchone()[0]
  if(myFriends.find(str(friendId)+",")>-1):#Removes friendId from myFriends 
    myFriends=myFriends.replace(str(friendId)+",","")
  else:
    myFriends=myFriends.replace(str(friendId),"")
    
  if(friendFriends.find(str(userId)+",")>-1):#removes userId from friendsFriends
    friendFriends=friendFriends.replace(str(userId)+",","")
  else:
    friendFriends=friendFriends.replace(str(userId),"")
  connection.execute("UPDATE FriendNetwork SET friendIds = '{0}' WHERE id = {1};".format(myFriends,userId))
  connection.execute("UPDATE FriendNetwork SET friendIds = '{0}' WHERE id = {1};".format(friendFriends,friendId))
  connection.commit()