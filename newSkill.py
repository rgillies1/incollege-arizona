from importantLinks import importantLinks
from usefulLinks import usefulLinks
def newSkill():#New Skill Page, still under construction
    print(
        "1. Study Habits \n2. Creative Thinking \n3. Critical Thinking \n4. Work/School Life Balance \n5. Scheduling \n6. importantLinks \n7. return back to landing page"
    )
    option = -1
    validOptions=['1','2','3','4','5','6','Exit']
    while option not in validOptions:
      option = input("Please select a skill you would like to learn: ")
    

    if option == '1':
        print("This feature is under construction")
        newSkill()
    elif option == '2':
        print("This feature is under construction")
        newSkill()
    elif option == '3':
        print("This feature is under construction")
        newSkill()
    elif option == '4':
        print("This feature is under construction")
        newSkill()
    elif option == '5':
        print("This feature is under construction")
        newSkill()
    elif option == '6':
        importantLinks()
    elif option == 'Exit':
        pass
    else:
        print("Please enter in a number based on the skill you want to learn!")
        newSkill()
    pass
