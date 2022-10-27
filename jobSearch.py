from importantLinks import importantLinks
from usefulLinks import usefulLinks
from database import allRecords, getRecordCount, newJobPost


def jobSearch():  #Job search page
    table = "JobBoard"
    print(
        "~~~~Job Board~~~~\n\n1. Job Board \n2. Post a job \n3. UsefulLinks \n4. ImportantLinks \n9. Back\n"
    )
    option = int(input("Please select an option from the list above: "))
    titleList = []
    descriptionList = []
    employerList = []
    locationList = []
    salaryList = []
    nameList = []
    jobBoard = allRecords(table)
    if (jobBoard != []):
        for i in jobBoard:
            a, b, c, d, e, f = i
            b = b.strip()
            c = c.strip()
            d = d.strip()
            e = e.strip()
            f = f.strip()
            titleList.append(a)
            descriptionList.append(b)
            employerList.append(c)
            locationList.append(d)
            salaryList.append(e)
            nameList.append(f)

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
