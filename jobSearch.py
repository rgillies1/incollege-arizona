from importantLinks import importantLinks
from usefulLinks import usefulLinks
from database import getRecordCount, newJobPost, getJobBoard, getOthersJobs, getUsersApplication, apply, removeJobPost, getPostersJobs, removeJobApplication, saveJobs, getSavedJobs, removeSavedJobs


def jobSearch():  #Job search page
    table = "JobBoard"
    print(
        "~~~~Job Board~~~~\n\n1. Job Board \n2. Post a job \n3. UsefulLinks \n4. ImportantLinks \n5. Delete a Job \n6. Apply for Job \n7. Applied Jobs \n8. Available Jobs \n9. Manage Saved Job  \nType \"Exit\" to go back\n"
    )

    applications = getUsersApplication()
    if (applications != None):
        for app in applications:
            if (app[-1]):
                print(
                    "The job posting '{0}' has been removed.  Your application has therefore been deleted"
                    .format(app[0]))
                removeJobApplication(app[1])
    option = input("\nPlease select an option from the list above: ")
    titleList = []
    descriptionList = []
    employerList = []
    locationList = []
    salaryList = []
    jobBoard = getJobBoard()
    if (jobBoard != []):
        for i in jobBoard:
            a, b, c, d, e = i
            b = b.strip()
            c = c.strip()
            d = d.strip()
            e = e.strip()
            titleList.append(a)
            descriptionList.append(b)
            employerList.append(c)
            locationList.append(d)
            salaryList.append(e)

    if option == "2":  #Add new posting
        if getRecordCount(table) >= 10:
            print("ERROR: Job board full, please try again later")
            jobSearch()
        else:
            jobTitle = input("Enter job title: ")
            jobDescription = input("Enter job description: ")
            jobEmployer = input("Enter job employer: ")
            jobLocation = input("Enter job location: ")
            jobSalary = input("Enter job's salary: ")
            try:  #I think this works
                newJobPost(jobTitle, jobDescription, jobEmployer, jobLocation,
                           jobSalary)
            except:
                print("Something went wrong! Please try again later")
            jobSearch()

    elif option == "1":  #Display all posts
        if getRecordCount(table) != 0:
            i = 0
            for i in range(len(titleList)):
                print(str(1 + i) + ". " + titleList[i])
            jobOption = input("Select one of the jobs to view its details or 'Exit' to exit: ")
            if(jobOption.isdigit()):
                    if(int(jobOption)<1 or int(jobOption)>len(titleList)):
                        jobOption="nope"
            while(not jobOption.isdigit() and jobOption !='Exit'):
                print("ERROR, invalid input.\n")
                jobOption = input("Select one of the jobs to view its details or 'Exit' to exit: ")
                if(jobOption.isdigit()):
                    if(int(jobOption)<1 or int(jobOption)>len(titleList)):
                        jobOption="nope"
            if (jobOption == "Exit"):
                jobSearch()
            else:
                jobOption=int(jobOption)
                print("\nJob Title: " + titleList[jobOption - 1] + "\n")
                print("Job Description: " + descriptionList[jobOption - 1] +
                      "\n")
                print("Job Employer: " + employerList[jobOption - 1] + "\n")
                print("Job Location: " + locationList[jobOption - 1] + "\n")
                print("Job Salary: " + salaryList[jobOption - 1] + "\n")
                jobSearch()
        else:
            print("\nJob board empty")
            jobSearch()

    elif option == "Exit":  #Exit
        pass
    elif option == "3":  #Usful Links
        usefulLinks()
        jobSearch()
    elif option == "4":  #Important Links
        importantLinks()
        jobSearch()
    elif option == "5":  #Delete Jobs
        deleteJob()
        jobSearch()
    elif option == "6":  #Apply to job
        applyJob()
        jobSearch()
    elif option == "7":  #view jobs you already applied to
        value = getUsersApplication()
        titles = []
        for i in value:
            titles.append(i[0])
        if(titles==[]):
            print("You have applied to no jobs")
        else:
            print("\nYou have applied for the following jobs:")
            for j in range(len(titles)):
                print("\t"+str(1 + j) + ". " + titles[j])
        print("")
        jobSearch()
        # option = input("Enter anything to exit:")
        # if option == "":
        #     jobSearch()
        # else:
        #     jobSearch()
    elif option == "8":  #View jobs you can still apply to
        otherJobs = getOthersJobs()
        appliedJobs = getUsersApplication()
        titles = []
        jobIds = []
        appliedJobsIds = []
        count = 1
        for j in otherJobs:
            titles.append(j[0])  #Title name for job
            jobIds.append(j[-1])  #Job post ID
        for j in appliedJobs:
            appliedJobsIds.append(j[1])  #Applied job post ID
        for j in range(len(jobIds)):
            done = 0
            if not appliedJobsIds:  #checks if user has applied to any jobs
                pass
            else:
                for i in range(len(appliedJobsIds)):       
                    if appliedJobsIds[i] == jobIds[j]: 
                        done = 1  
                        break
            if done == 0:    #checks if job was marked as applied      
              print(str(count) + ". " + titles[j])  # prints the jobs available
              count += 1
        option = input("Enter anything to exit:")
        if option == "":
            jobSearch()
        else:
            jobSearch()
    elif option == "9":#Save job
        savedJobs()
        jobSearch()
      
def savedJobs():
    print("\n~~~~Saved Jobs~~~~\n")
    sJobs = getSavedJobs()
    opt = 0 
    if(sJobs== None):
        print("You have no jobs saved")
        valid = ["1","Exit"]
        opt = input("Type 1 to save a job, or 'Exit' to exit: ")
        while opt not in valid:
            opt = input("Invalid input, please type 1 to save a job, or 'Exit' to exit: ")
    else:
        for i in range(len(sJobs)):
            print("\t"+str(i+1)+". "+sJobs[i][1])
        print("")
        valid = ["1","2","Exit"]
        opt = input("Type '1' to save a new job, or '2' to remove a saved job, or 'Exit' to exit: ")
        while opt not in valid:
            opt = input("Invalid input, please type '1' to save a job, or '2' to remove a saved job, or 'Exit' to exit: ")
    if(opt=='1'):
        print("")
        otherJobs = getOthersJobs()
        appliedJobs = getUsersApplication()
        titles = []
        jobIds = []
        appliedJobsIds = []
        count = 1
        for j in otherJobs:
            titles.append(j[0])  #Title name for job
            jobIds.append(j[-1])  #Job post ID
        for j in appliedJobs:
            appliedJobsIds.append(j[1])  #Applied job post ID
        for j in range(len(jobIds)):
            done = 0
            if not appliedJobsIds:  #checks if user has applied to any jobs
                pass
            else:
                for i in range(len(appliedJobsIds)):       
                    if appliedJobsIds[i] == jobIds[j]: 
                        done = 1  
                        break
            if done == 0:    #checks if job was marked as applied      
              print(str(count) + ". " + titles[j])  # prints the jobs available
              count += 1
        if(len(jobIds)==0):
            print("There are no jobs availible for you to save at this time.")
            return None
        saveJ = int(input("Select the job you want to save for later or enter '0' to exit: "))
        if (saveJ == 0):
            savedJobs()
        else:
            saveJobs(otherJobs[saveJ - 1][-1])
            savedJobs()
    elif(opt=='2'):
        removeJ = int(input("Select the job you want to remove or enter '0' to exit: "))
        if(removeJ == 0):
            savedJobs()
        else:
            removeSavedJobs(sJobs[removeJ-1][0])
            savedJobs()
          
def applyJob():
    otherJobs = getOthersJobs()
    appliedJobs = getUsersApplication()
    titles = []
    jobIds = []
    appliedJobsIds = []
    for j in otherJobs:
        titles.append(j[0])  #Title name for job
        jobIds.append(j[-1])  #Job post ID
    for j in appliedJobs:
        appliedJobsIds.append(j[1])  #Job post ID
    for i in range(len(titles)):
        print(str(1 + i) + ". " + titles[i])

    jobOption = input(
        "Select job from the list above that you would like to apply to or enter \"Exit\" to go back: "
    )
    if jobOption == "Exit":  #exit
        return None
    elif (jobIds[int(jobOption) - 1]
          in appliedJobsIds):  #You have already applied to this position
        print("You have already applied for this position")
        applyJob()

    else:
        gradDate = input("Enter graduation date (mm/dd/yyyy): ")
        startDate = input("Enter date (mm/dd/yyyy) you can start working: ")
        textApp = input("Explain why you would be a good fit for this job: ")
        apply(jobIds[int(jobOption) - 1], gradDate, startDate, textApp)
        applyJob()

def deleteJob():
    jobBoard = getPostersJobs()
    print("")

    if (len(jobBoard) == 0):
        print("There are no Jobs")
        return None
    else:
        print("~List of Jobs~")
        jobIds = []
        for i in range(0, len(jobBoard)):
            jobIds.append(
                jobBoard[i][-1])  #Appends list of job board Ids to a list
            print("\t" + str(i + 1) + ". " + jobBoard[i][0])

    remove = int(
        input(
            "Pick which job you would like to romove. Input 0 to select none: "
        ))
    if(remove == 0):
        return None
    removeJobPost(jobIds[remove - 1])
