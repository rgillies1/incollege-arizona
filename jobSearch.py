from importantLinks import importantLinks
from usefulLinks import usefulLinks
from database import getRecordCount, newJobPost, getJobBoard, getOthersJobs, getUsersApplication, apply, removeJobPost, getPostersJobs, removeJobApplication, getAppliedJobs, getJobsTitles

def jobSearch():  #Job search page
    table = "JobBoard"
    print(
        "~~~~Job Board~~~~\n\n1. Job Board \n2. Post a job \n3. UsefulLinks \n4. ImportantLinks \n5. Delete a Job \n6. Apply for Job \n7. Applied Jobs \n9. Back\n"
    )
    
    applications  = getUsersApplication()
    toBeDeletedIds = []
    toBeDeletedTruth = []
    if(applications != None):
        for app in applications:
            if(app[-1]):
                toBeDeletedIds.append(app[1])
    if(len(toBeDeletedIds)>0):
        print("ALERT, Job post that will have a name displayed tomorrow because David is tired has been deleted")
        #for i in toBeDeletedIds:
        #    removeJobApplication(i)
    option = int(input("Please select an option from the list above: "))
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

    if option == 2:  #Add new posting
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

    elif option == 1:  #Display all posts
        if getRecordCount(table) != 0:
            i = 0
            for i in range(len(titleList)):
                print(str(1 + i) + ". " + titleList[i])
            print("9. Back")
            jobOption = int(
                input("Select one of the jobs to view its details: "))
            if (jobOption == 9):
                jobSearch()
            else:
                print("\nJob Title: " + titleList[jobOption - 1] + "\n")
                print("Job Description: " + descriptionList[jobOption - 1] + "\n")
                print("Job Employer: " + employerList[jobOption - 1] + "\n")
                print("Job Location: " + locationList[jobOption - 1] + "\n")
                print("Job Salary: " + salaryList[jobOption - 1] + "\n")
        else:
            print("\nJob board empty")
            jobSearch()

    elif option == 9:  #Exit
        pass
    elif option == 3:  #Usful Links
        usefulLinks()
        jobSearch()
    elif option == 4:  #Important Links
        importantLinks()
        jobSearch()
    elif option == 5:
        deleteJob()
        jobSearch()
    elif option == 6:
         applyJob()
         jobSearch()
    elif option == 7:
        applied = []
      
        value = getAppliedJobs() #[(1, 2, 3, etc)]
        for j in value:
          print(str(1 + i) + ". " + value[i])


def applyJob():
    otherJobs = getOthersJobs()
    appliedJobs = getUsersApplication()
    titles = []
    jobIds = []
    appliedJobsIds = [] 
    for j in otherJobs: 
        titles.append(j[0])#Title name for job
        jobIds.append(j[-1])#Job post ID
    for j in appliedJobs:
        appliedJobsIds.append(j[1])#Job post ID
    for i in range(len(titles)):
        print(str(1 + i) + ". " + titles[i])
        
    jobOption = input("Select job you would like to apply to: ")
    if(jobIds[int(jobOption)-1] in appliedJobsIds):#You have already applied to this position
        print("ADD SOME LOGIC HERE ARTHUR")
    else:
        gradDate = input("Enter graduation date (mm/dd/yyyy): ")
        startDate = input("Enter date (mm/dd/yyyy) you can start working: ")
        textApp = input("Explain why you would be a good fit for this job: ")
        apply(jobIds[int(jobOption)-1], gradDate, startDate, textApp)
        
def deleteJob():
  jobBoard = getPostersJobs()
  print("")
  
  if(len(jobBoard) == 0):
    print("There are no Jobs")
    return None
  else:
    print("~List of Jobs~")
    jobIds = []
    for i in range(0, len(jobBoard)):
      jobIds.append(jobBoard[i][-1])#Appends list of job board Ids to a list
      print("\t" + str(i + 1) + ". " + jobBoard[i][0])

  remove = int (input("Pick which job you would like to romove. Input 0 to select none: "))
  removeJobPost(jobIds[remove-1])
  
    
