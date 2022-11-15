from home import homePage
from database import tables, allRecords, customCommand, getOthersJobs,newJobPost
from testing_base import addNewUsers,clearTables

#tables()
def main():
    #clearTables()
    tables()  #Confirms database initialized and empties ActiveUsers
    #newJobPost("pizza", "", "", "", "", 1)
    #addNewUsers()
    #addNewUsers()
    #addNewUsers()
    #addNewUsers()
    # print(allRecords("JobBoard"))
    #print(customCommand("SELECT * FROM UserData"))
    #print(customCommand("SELECT * FROM UserLogin"))
    # print(getOthersJobs("2"))
    #print(customCommand("SELECT position,description,employer,location,salary FROM userLogin"))
    homePage()  #Calls Home Page and starts the process
    return 0

if __name__ == "__main__":
    main()
