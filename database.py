import sqlite3
import random
import os


#This file verifies the existance of the databases needed for the application
def tables(connection=sqlite3.connect("inCollege.db")):
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
  savedJobs TEXT DEFAULT ' ' NOT NULL,
  --major TEXT, 
  --college TEXT, 
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
    connection.execute(
        """CREATE TABLE IF NOT EXISTS Contacts
    (id INTEGER UNIQUE, 
    firstName TEXT, 
    lastName TEXT, 
    email TEXT UNIQUE, 
    phone TEXT UNIQUE, 
    FOREIGN KEY(id) REFERENCES UserLogin(id));"""
    )  #Should only have ID if there is an account connected to contact

    #Friend Network info
    connection.execute("""CREATE TABLE IF NOT EXISTS FriendNetwork
    (id INTEGER UNIQUE, 
    friendIds TEXT DEFAULT '' NOT NULL, --Each friend ID should be seperated by a comma
    FOREIGN KEY(id) REFERENCES UserLogin(id));"""
                       )  #Each friend ID should be seperated by a comma

    #Friend requst info
    connection.execute("""CREATE TABLE IF NOT EXISTS FriendRequest 
    (sendId INTEGER, 
    recieveId INTEGER, 
    FOREIGN KEY(sendId) REFERENCES UserLogin(id),
    FOREIGN KEY(recieveId) REFERENCES UserLogin(id));""")

    #Job board info
    connection.execute("""CREATE TABLE IF NOT EXISTS JobBoard 
    (jobPostId INTEGER PRIMARY KEY, --A unique value for each job listing
    position TEXT NOT NULL, 
    description TEXT NOT NULL, 
    employer TEXT NOT NULL, 
    location TEXT NOT NULL, 
    salary TEXT NOT NULL,
    posterName TEXT NOT NULL, --Name/Title
    posterId INTEGER NOT NULL, --UserId of Poster
    FOREIGN KEY(posterId) REFERENCES UserLogin(id));""")

    #Application
    connection.execute("""CREATE TABLE IF NOT EXISTS Applications
    (id INTEGER,
    position TEXT NOT NULL,
    jobPostId INTEGER,
    startDate TEXT,
    gradDate TEXT,
    application TEXT,
    toBeDeleted INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(id) REFERENCES UserLogin(id),
    FOREIGN KEY(jobPostId) REFERENCES JobBoard(jobPostId));""")

    #Profiles for each user - john is working on this
    connection.execute("""CREATE TABLE IF NOT EXISTS Profiles
  (id INTEGER UNIQUE, 
  title TEXT, 
  about TEXT, 
  --experience TEXT,
  --education TEXT, 
  FOREIGN KEY(id) REFERENCES UserLogin(id));""")

    #Job Experience, tied into profiles
    connection.execute(
        """CREATE TABLE IF NOT EXISTS JobExperience
    (id INTEGER,
    jobNum INTEGER,
    jobTitle TEXT, 
    employer TEXT, 
    startDate TEXT,
    endDate TEXT,
    location TEXT,
    description TEXT,
    FOREIGN KEY(id) REFERENCES UserLogin(id));"""
    )  #ID not unique, they can have upto 3 entries added into this

    #Education, tied into Profile
    connection.execute(
        """CREATE TABLE IF NOT EXISTS Education
  (id INTEGER UNIQUE, 
  university TEXT, 
  major TEXT, 
  degree TEXT,
  years INTEGER, 
  FOREIGN KEY(id) REFERENCES UserLogin(id));"""
    )  #Currently only one college can be tied to each account so ID stays unique
    connection.commit()


def customCommand(
    cmd, connection=sqlite3.connect("inCollege.db")):  #executes custom command
    if (cmd[0:6].upper() == 'SELECT'):
        return connection.execute(cmd).fetchall()
    connection.execute(cmd)
    connection.commit()


def getRecordCount(
    table="UserLogin",
    connection=sqlite3.connect("inCollege.db")
):  #Returns number of records in specified table, default is number of users
    return connection.execute("SELECT COUNT(*) FROM " + table +
                              ";").fetchone()[0]


def allRecords(table, connection=sqlite3.connect("inCollege.db")
               ):  #Returns all records in a list of tuples
    return connection.execute("SELECT * FROM " + table + ";").fetchall()


def exist(table, col, val, connection=sqlite3.connect("inCollege.db")
          ):  #Returns true if val is in list of values in col
    return (val) in connection.execute("SELECT " + col + " FROM " + table +
                                       ";").fetchall()


#def newAccount(username,password,firstName,lastName,major,college,email,phone,connection = sqlite3.connect("inCollege.db")):
def newAccount(username,
               password,
               firstName,
               lastName,
               email,
               phone,
               connection=sqlite3.connect("inCollege.db")):
    #Saves Login Info
    connection.execute(
        "INSERT INTO UserLogin (username,password) VALUES ('{0}','{1}');".
        format(username, password))
    #Retrieves UserId
    userId = connection.execute(
        "SELECT id FROM UserLogin WHERE username = '{0}';".format(
            username)).fetchone()[0]
    #Saves User Data
    connection.execute(
        "INSERT INTO UserData (id,firstName,lastName) VALUES ({0},'{1}','{2}')"
        .format(userId, firstName, lastName))
    #Creates and defaults user Settings
    connection.execute(
        "INSERT INTO UserSettings (id) VALUES ({0})".format(userId))
    #Makes sure contact information exists
    if (exist(table="Contacts", col="email", val=email)):
        connection.update(
            "UPDATE Contacts SET id = {0}, phone = '{1}' WHERE email = '{2}'".
            format(userId, phone, email))
    elif (exist(table="Contacts", col="phone", val=phone)):
        connection.update(
            "UPDATE Contacts SET id = {0}, email = '{1}' WHERE phone = '{2}'".
            format(userId, email, phone))
    else:
        connection.execute(
            "INSERT INTO Contacts (id,firstName,lastName,email,phone) VALUES ({0},'{1}','{2}','{3}','{4}')"
            .format(userId, firstName, lastName, email, phone))
    #Creates friend records
    connection.execute(
        "INSERT INTO FriendNetwork (id) VALUES ({0});".format(userId))
    #Creates Profile Page record
    connection.execute(
        "INSERT INTO Profiles (id) VALUES ({0});".format(userId))
    #Creates Education record for Profiles
    connection.execute(
        "INSERT INTO Education (id) VALUES ({0});".format(userId))

    connection.commit()


def authLogin(
    username, password, connection=sqlite3.connect("inCollege.db")
):  #Authenticates User and creates Cookie for future authentication
    p = connection.execute(
        "SELECT password FROM UserLogin WHERE username = '{0}'".format(
            username)).fetchone()
    if (p == None):
        return 0
    if (password == p[0]):
        userId = connection.execute(
            "SELECT id FROM UserLogin WHERE username = '{0}';".format(
                username)).fetchone()[0]

        if (connection.execute(
                "SELECT * FROM ActiveUsers WHERE id = {0};".format(
                    userId)).fetchall() != []):  #User is logged on already
            return -1
        cookieHash = random.getrandbits(128)  #Gets a random hash
        connection.execute(
            "INSERT INTO ActiveUsers (id,cookie) VALUES ({0},'{1}');".format(
                userId, cookieHash))  #Puts random hash in db
        cookie = open("cookie", "w")
        cookie.write(str(cookieHash))
        cookie.close()
        connection.commit()
        return 1
    return 0


def authUser(
    cookie=0,
    connection=sqlite3.connect("inCollege.db")
):  #Authenticates Logged In User, returns userId if cookie corresponds to hash
    try:
        cookieFile = False
        if (
                cookie == 0
        ):  #User cookie, reason not checking for path because we may not be checking for current cookie
            cookie = open("cookie", "r").read()
            cookieFile = True
        userId = connection.execute(
            "SELECT id FROM ActiveUsers WHERE cookie = '{0}'".format(
                cookie)).fetchone()[0]
        if (userId == None):
            print("Authentication failed")
            if (
                    cookieFile
            ):  #If cookie file exists but doesn't authenticate, remove file
                os.remove("cookie")
            return (False, None)
        return (True, userId)
    except:
        print("Authentication failed")
        return (False, None)


def logout(userId=-1,
           connection=sqlite3.connect(
               "inCollege.db")):  #Logs user out and clears active user cookie
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):  #Not authenticated
        pass
    cookie = open("cookie", "r").read()
    connection.execute(
        "DELETE FROM ActiveUsers WHERE cookie = '{0}';".format(cookie))
    if os.path.exists("cookie"):
        os.remove("cookie")
    connection.commit()


def updateUser(table,
               col,
               val,
               userId=-1,
               connection=sqlite3.connect("inCollege.db")
               ):  #Update user values with provided userId
    if (userId == -1):  #UserId not Provided
        userId = authUser()[1]
    if (userId == None):  #Not authenticated
        pass
    if (type(val) == type("")):  #Are we updating a text value or int value
        connection.execute("UPDATE {0} SET {1} = '{2}' WHERE id = {3}".format(
            table, col, val, userId))
    else:
        connection.execute("UPDATE {0} SET {1} = {2} WHERE id = {3}".format(
            table, col, val, userId))
    connection.commit()


def findUser(
    lastName="%",
    university="%",
    major="%",
    connection=sqlite3.connect("inCollege.db")):  #Find user in UserData
    if (lastName != "%"):
        return connection.execute(
            "SELECT id,firstName,lastName FROM userData WHERE lastName LIKE '%{0}%';"
            .format(lastName)).fetchall()
    return connection.execute(
        "SELECT UserData.id, UserData.firstName, UserData.lastName FROM UserData JOIN Education ON UserData.id = Education.id WHERE Education.university LIKE '{0}' AND Education.major LIKE '{1}';"
        .format(university, major)).fetchall()  #'%' is wildcard in SQL


def findContact(
    firstName="%",
    lastName="%",
    connection=sqlite3.connect("inCollege.db")):  #Find contact in Contacts
    return connection.execute(
        "SELECT id, firstName, lastName FROM Contacts WHERE lastName = '{0}' AND firstName = '{1}';"
        .format(lastName, firstName)).fetchone()


def addContact(
    firstName,
    lastName,
    phone,
    email,
    connection=sqlite3.connect("inCollege.db")):  #Adds mew contact to Contacts
    connection.execute(
        "INSERT INTO Contacts (firstName,lastName,email,phone) VALUES ('{0}','{1}','{2}','{3}')"
        .format(firstName, lastName, email, phone))
    connection.commit()


def newJobPost(jobTitle,
               jobDescription,
               jobEmployer,
               jobLocation,
               jobSalary,
               userId=-1,
               connection=sqlite3.connect("inCollege.db")):  #Posts new job
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    name = connection.execute(
        "SELECT firstName,lastName FROM UserData WHERE id = {0};".format(
            userId)).fetchone()
    fullName = name[0] + " " + name[1]
    connection.execute(
        "INSERT INTO JobBoard (position,description,employer,location,salary,posterName, posterId) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}',{6});"
        .format(jobTitle, jobDescription, jobEmployer, jobLocation, jobSalary,
                fullName, userId))
    connection.commit()
    print(connection.execute("SELECT * FROM JobBoard").fetchall())


def newFriendRequest(
    friendId,
    userId=-1,
    connection=sqlite3.connect("inCollege.db")):  #New friend request
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None or userId == friendId):
        pass
    requestCheck1 = connection.execute(
        "SELECT sendId,recieveId FROM FriendRequest WHERE sendId = {0} AND recieveId = {1};"
        .format(userId, friendId)).fetchone()
    requestCheck2 = connection.execute(
        "SELECT sendId,recieveId FROM FriendRequest WHERE sendId = {0} AND recieveId = {1};"
        .format(friendId, userId)).fetchone()

    friendIdStr = str(friendId)
    friendCheck = connection.execute(
        "SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(
            userId)).fetchone()[0]
    if (friendCheck == None):
        friendCheck = True
    elif ((friendIdStr in friendCheck
           )):  #CHECK TO SEE IF friendId is substring in friendCheck
        print("You are already friends")
        friendCheck = False
    else:
        friendCheck = True
    #print(requestCheck1,requestCheck2,friendCheck,friendIdStr)
    if (requestCheck1 == None and friendCheck and requestCheck2 == None
        ):  #if there is no existing request and they aren't already friends
        connection.execute(
            "INSERT INTO FriendRequest (sendId,recieveId) VALUES ({0},{1});".
            format(userId, friendId))
    connection.commit()


def getFriendRequests(
    userId=-1,
    connection=sqlite3.connect("inCollege.db")):  #returns all friend requests
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    friendRequestList = connection.execute(
        "SELECT sendId FROM FriendRequest WHERE recieveId = {0};".format(
            userId)).fetchall()  #Retrieves all friendIds
    #print(friendRequestList)
    if (friendRequestList == None):
        return []
    for i in range(
            0, len(friendRequestList)
    ):  #makes each value integer and gets corresponding username
        friendUser = connection.execute(
            "SELECT username FROM UserLogin WHERE id = {0};".format(
                friendRequestList[i][0])).fetchone()[0]
        friendRequestList[i] = (friendUser, friendRequestList[i][0])
    return friendRequestList


def removeFriendRequest(sendId,
                        recieveId=-1,
                        connection=sqlite3.connect("inCollege.db")
                        ):  #Removes specified friend request
    if (recieveId == -1):
        recieveId = authUser()[1]
    if (recieveId == None):
        pass
    connection.execute(
        "DELETE FROM FriendRequest WHERE sendId = {0} AND recieveId = {1};".
        format(sendId, recieveId))
    connection.commit()


def addFriend(friendId,
              userId=-1,
              connection=sqlite3.connect("inCollege.db")):  #Adds new friend
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    myFriends = connection.execute(
        "SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(
            userId)).fetchone()[0]
    friendFriends = connection.execute(
        "SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(
            friendId)).fetchone()[0]
    if (myFriends == ""):
        myFriends = str(friendId)
    else:
        myFriends += "," + str(friendId)
    if (friendFriends == ""):
        friendFriends = str(userId)
    else:
        friendFriends += "," + str(userId)
    connection.execute(
        "UPDATE FriendNetwork SET friendIds = '{0}' WHERE id = {1};".format(
            myFriends, userId))
    connection.execute(
        "UPDATE FriendNetwork SET friendIds = '{0}' WHERE id = {1};".format(
            friendFriends, friendId))
    connection.commit()


def getFriends(
    userId=-1,
    connection=sqlite3.connect("inCollege.db")):  #Returns user's friends
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    friendList = connection.execute(
        "SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(
            userId)).fetchone()[0]  #Retrieves all friendIds
    if (friendList == ""):
        return []
    friendList = friendList.split(",")  #Splits into list
    for i in range(
            0, len(friendList)
    ):  #makes each value integer and gets corresponding username
        friendUser = connection.execute(
            "SELECT username FROM UserLogin WHERE id = {0};".format(
                friendList[i])).fetchone()[0]
        friendList[i] = (friendUser, int(friendList[i]))
    return friendList


def removeFriend(
    friendId,
    userId=-1,
    connection=sqlite3.connect("inCollege.db")):  #Removes specified friend
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    myFriends = connection.execute(
        "SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(
            userId)).fetchone()[0]
    friendFriends = connection.execute(
        "SELECT friendIds FROM FriendNetwork WHERE id = {0};".format(
            friendId)).fetchone()[0]
    if (myFriends.find(str(friendId) + ",") >
            -1):  #Removes friendId from myFriends
        myFriends = myFriends.replace(str(friendId) + ",", "")
    else:
        myFriends = myFriends.replace(str(friendId), "")

    if (friendFriends.find(str(userId) + ",") >
            -1):  #removes userId from friendsFriends
        friendFriends = friendFriends.replace(str(userId) + ",", "")
    else:
        friendFriends = friendFriends.replace(str(userId), "")
    connection.execute(
        "UPDATE FriendNetwork SET friendIds = '{0}' WHERE id = {1};".format(
            myFriends, userId))
    connection.execute(
        "UPDATE FriendNetwork SET friendIds = '{0}' WHERE id = {1};".format(
            friendFriends, friendId))
    connection.commit()


def getUserFirstLastName(userId=-1,
                         connection=sqlite3.connect("inCollege.db")
                         ):  #Returns username, firstname, lastname
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    return connection.execute(
        "SELECT UserLogin.username, UserData.firstName, UserData.lastName FROM UserData JOIN UserLogin ON UserLogin.id = UserData.id WHERE UserData.id = {0};"
        .format(userId)).fetchall()[0]


def getJobExperience(userId=-1,
                     connection=sqlite3.connect(
                         "inCollege.db")):  #Returns all job experience data
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    return connection.execute(
        "SELECT jobNum,jobTitle, employer, startDate, endDate, location, description FROM JobExperience WHERE id = {0} ORDER BY jobNum ASC;"
        .format(userId)).fetchall(
        )  #Fetch all because there can be up to 3 entries


def getEducation(
    userId=-1,
    connection=sqlite3.connect("inCollege.db")):  #Returns all education data
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    return connection.execute(
        "SELECT university, major, degree, years FROM Education WHERE id = {0};"
        .format(userId)).fetchall()[0]


def getProfile(userId=-1,
               connection=sqlite3.connect(
                   "inCollege.db")):  #Returns all profile information
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    return connection.execute(
        "SELECT title, about FROM Profiles WHERE id = {0};".format(
            userId)).fetchall()[0]


#----------------------------------------------------------------------------------
def setJobExperience(
    jobNum=None,
    jobTitle=None,
    employer=None,
    startDate=None,
    endDate=None,
    location=None,
    description=None,
    userId=-1,
    connection=sqlite3.connect("inCollege.db")):  #sets all job experience data
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None
            or (jobNum == None and jobTitle == None and employer == None
                and startDate == None and endDate == None and location == None
                and description == None)):
        pass
    if (jobNum == -1):
        count = len(
            connection.execute(
                "SELECT * FROM JobExperience WHERE id = {0}".format(
                    userId)).fetchall())
        if (count >= 3):
            print("Only 3 Job Experiences can be recoreded at this time")
            return None
        elif (count >= 0):
            jobNum = count + 1
            connection.execute(
                "INSERT INTO JobExperience (id,jobNum) VALUES ({0},{1});".
                format(userId, jobNum))
        else:
            return None
    if (jobTitle != None):
        connection.execute(
            "UPDATE JobExperience SET jobTitle = '{0}' WHERE id = {1} AND jobNum = {2};"
            .format(jobTitle, userId, jobNum))

    if (employer != None):
        connection.execute(
            "UPDATE JobExperience SET employer = '{0}' WHERE id = {1} AND jobNum = {2};"
            .format(employer, userId, jobNum))

    if (startDate != None):
        connection.execute(
            "UPDATE JobExperience SET startDate = '{0}' WHERE id = {1} AND jobNum = {2};"
            .format(startDate, userId, jobNum))

    if (endDate != None):
        connection.execute(
            "UPDATE JobExperience SET endDate = '{0}' WHERE id = {1} AND jobNum = {2};"
            .format(endDate, userId, jobNum))

    if (location != None):
        connection.execute(
            "UPDATE JobExperience SET location = '{0}' WHERE id = {1} AND jobNum = {2};"
            .format(location, userId, jobNum))

    if (description != None):
        connection.execute(
            "UPDATE JobExperience SET description = '{0}' WHERE id = {1} AND jobNum = {2};"
            .format(description, userId, jobNum))
    connection.commit()
    # return connection.execute("SELECT jobNum, jobTitle, employer, startDate, endDate, location, description FROM JobExperience WHERE id = {0};".format(userId)).fetchall()#Fetch all because there can be up to 3 entries


def setEducation(
    university=None,
    major=None,
    degree=None,
    years=None,
    userId=-1,
    connection=sqlite3.connect("inCollege.db")):  #Sets education data
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None or (university == None and major == None
                           and degree == None and years == None)):
        pass
    if (university != None):
        connection.execute(
            "UPDATE Education SET university = '{0}' WHERE id = {1};".format(
                university, userId))
    if (major != None):
        connection.execute(
            "UPDATE Education SET major = '{0}' WHERE id = {1};".format(
                major, userId))
    if (degree != None):
        connection.execute(
            "UPDATE Education SET degree = '{0}' WHERE id = {1};".format(
                degree, userId))
    if (years != None):
        connection.execute(
            "UPDATE Education SET years = {0} WHERE id = {1};".format(
                years, userId))
    connection.commit()


def setProfile(
    title=None,
    about=None,
    userId=-1,
    connection=sqlite3.connect("inCollege.db")):  #setProfile title and about
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None or (title == None and about == None)):
        pass
    if (title != None):
        connection.execute(
            "UPDATE Profiles SET title = '{0}' WHERE id = {1};".format(
                title, userId))
    if (about != None):
        connection.execute(
            "UPDATE Profiles SET about = '{0}' WHERE id = {1};".format(
                about, userId))
    connection.commit()
    # return connection.execute("SELECT title, about FROM Profiles WHERE id = {0};".format(userId)).fetchall()[0]


#--------------------------------------------------------------------------------------------------------------------------------


def getJobBoard(
        connection=sqlite3.connect("inCollege.db")):  #Returns Titles/Position
    return connection.execute(
        "SELECT position,description,employer,location,salary FROM JobBoard;"
    ).fetchall()


def getPostersJobs(userId=-1,
                   connection=sqlite3.connect("inCollege.db")
                   ):  #Returns Titles/Position of the jobs you posted
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    return connection.execute(
        "SELECT position,description,employer,location,salary,jobPostId FROM JobBoard WHERE posterId = {0};"
        .format(userId)).fetchall()


def getOthersJobs(userId=-1,
                  connection=sqlite3.connect("inCollege.db")
                  ):  #Returns Titles/Position of the jobs other people posted
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    return connection.execute(
        "SELECT position,description,employer,location,salary,jobPostId FROM JobBoard WHERE posterId <> {0};"
        .format(userId)).fetchall()


def removeJobPost(jobPostId, connection=sqlite3.connect("inCollege.db")):#Removes job post, updates Applications to be deleted, and removes saved jobs
    connection.execute("UPDATE Applications SET toBeDeleted = 1 WHERE jobPostId = {0};".format(jobPostId))
    connection.execute(
        "DELETE FROM JobBoard WHERE jobPostId = {0};".format(jobPostId))
    connection.commit()

def removeJobApplication(jobPostId,userId = -1, connection=sqlite3.connect("inCollege.db")):
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    connection.execute(
        "DELETE FROM Applications WHERE jobPostId = {0} and id = {1};".format(jobPostId,userId))
    connection.commit()

def getUsersApplication(userId=-1, connection=sqlite3.connect("inCollege.db")):
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    return connection.execute(
        "SELECT  position, jobPostId, toBeDeleted FROM Applications WHERE id={0};".format(userId)).fetchall()


def apply(jobPostId,
          gradDate,
          startDate,
          textApp,
          userId=-1,
          connection=sqlite3.connect("inCollege.db")):
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    title = connection.execute("SELECT position FROM JobBoard WHERE jobPostId = {0}".format(jobPostId)).fetchall()[0][0]
    connection.execute(
        "INSERT INTO Applications (id, jobPostId, gradDate, startDate, application, position) VALUES ({0},{1},'{2}','{3}','{4}','{5}')"
        .format(userId, jobPostId, gradDate, startDate, textApp, title))
    connection.commit()

def getAppliedJobs(userId=-1, connection=sqlite3.connect("inCollege.db")):
    if (userId == -1):
        userId = authUser()[1]
    if (userId == None):
        pass
    return connection.execute(
        "SELECT Applications.jobPostId, JobBoard.position FROM Applications LEFT JOIN ON JobBoard.jobPostId = Applications.jobPostId WHERE Applications.id={0};".format(userId)).fetchall()

def getJobTitles(jobPostId, connection=sqlite3.connect("inCollege.db")):
    return connection.execute(
        "SELECT position FROM JobBoard WHERE jobPostId = {0};".format(jobPostId )).fetchall()[0]

def getSavedJobs(userId=-1, connection=sqlite3.connect("inCollege.db")):# Returns the saved jobs jobIds and position names in a list tuple
    jobs = connection.execute("SELECT savedJobs FROM UserData WHERE id = {0}").fetchall()
    jobIds = jobs.split(",")
    savedJobsIdsAndPositions = []
    for id in jobIds:
        posit = connection.execute("SELECT position FROM JobBoard WHERE id = {0}".format(id)).fetchall()[0][0]
        savedJobsIdsAndPositions.append((id,posit))
    return savedJobsIdsAndPositions
  
def saveJobs(jobPostId,userId=-1, connection=sqlite3.connect("inCollege.db")):
    jobs = connection.execute("SELECT savedJobs FROM UserData WHERE id = {0}".format(userId)).fetchall()[0]
    if jobPostId in jobs: 
        pass
    else:
        print(jobs,jobPostId)
        if jobs == "":
            jobs = str(jobPostId)
        else:
            jobs+=","+str(jobPostId)
        connection.execute("UPDATE UserData SET savedJobs = '{0}' WHERE id = {1};".format(jobs,userId))
        connection.commit()

def removeSavedJobs(jobPostId,userId=-1, connection=sqlite3.connect("inCollege.db")):
    jobs = connection.execute("SELECT savedJobs FROM UserData WHERE id = {0}").fetchall()
    if jobPostId in jobs: 
        if(str(jobPostId)+"," in jobs):
            jobs.replace(str(jobPostId)+",","")
        elif(str(jobPostId) in jobs):
            jobs.replace(str(jobPostId),"")
        connection.execute("UPDATE UserData SET savedJobs = '{0}' WHERE id = {1};".format(jobs,userId))
        connection.commit()
      