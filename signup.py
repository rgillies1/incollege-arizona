from database import getRecordCount, exist, newAccount, getUserId
from ProfileNotification import P_Notifications



def validName(fName, lName):
  if (fName.lower() == 'null' or lName.lower() == 'null' or fName == ''
      or lName == ''):
    return (False, None, None)
  validNames = "abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' -"
  newLast = ""
  for c in lName:
    if (c not in validNames):
      return (False, None, None)
    if (c == "'"):
      newLast += "\'"
    else:
      newLast += c
  newFirst = ""
  for c in fName:
    if (c not in validNames):
      return (False, None, None)
    if (c == "'"):
      newFirst += "\'"
    else:
      newFirst += c
  return (True, newFirst, newLast)


def validPhone(num):  #Screw +1 exetensions
  if (len(num) == 10):  #5555555555 screw the plus 1
    validNums = ['0123456789' * 10]
  elif (len(num) == 12):  #555-555-5555 or 555 555 5555
    validNums = [
      '0123456789', '0123456789', '0123456789', ' -', '0123456789',
      '0123456789', '0123456789', ' -', '0123456789', '0123456789',
      '0123456789', '0123456789'
    ]
  else:
    return False
  for n in range(0, len(num)):
    if (num[n] not in validNums[n]):
      return False
  return True


def validEmail(email):
  valEm = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-.@'
  invLastLetter = '@._-'
  if (
      email[-1] in invLastLetter or len(email) < 6 or email.count('@') != 1
      or email.count('.') == 0 or email.find('@') - email.rfind('.') > 1
  ):  #some email rules.  last letter in email cannot be in invLastLetter.  Only one @ can be in an email and you need at least one '.'. shortest email I know of is 'a@b.co' Finally, the '@' must come before the last '.'
    return False
  for c in email:
    if (c not in valEm):
      return False
  return True


def checkPassword(password):  #Checks Password Requirements
  specialChar = ['$', '@', '#', '!', '%', '^', '&', '*']
  valid = True
  if len(password) < 8:
    print("Password must have at least 8 characters.")
    #signup()
    valid = False
  if len(password) > 12:
    print("Password must be less than 12 characters.")
    #signup()
    valid = False
  if not any(char.isdigit() for char in password):
    print("Password must contain a digit.")
    #signup()
    valid = False
  if not any(char.isupper() for char in password):
    print("Password must contain one upper.")
    #signup()
    valid = False
  if not any(char in specialChar for char in password):
    print("Password must contain a special character.")
    #signup()
    valid = False
  if valid:
    return valid


def signup(exit="n"):  #Signs up user
  table = "UserLogin"
  global language
  global major
  global university
  #usernameList = getUserInfo()[0]

  if (exit == "y"):  #Allows exit if they want to give up trying to sign up
    return None

  if getRecordCount() >= 10:  #maximum 10 accounts permitted
    print(
      "ERROR: All permitted accounts have been created, please come back later"
    )
    return None
  else:
    username = input("Enter a username: ")

    print(
      "\nBefore entering a password, make sure it is between 8 and 12 characters long. Must include at least one capital letter, at least one digit, and at least one special chracter('$', '@', '#', '!', '%', '^', '&', '*')!\n"
    )
    pwd1 = input("Enter a password: ")
    pwd2 = input("Confirm the password: ")

  if exist(table, "username",
           username):  #checks to see if values already exist in db
    print("ERROR: Username already exist!")
    exit = input("Would you like to exit(y/n):")
    return signup(exit)
  else:
    #Check if password are the same
    if pwd1 != pwd2:
      print("ERROR: Password does not match: ")
      exit = input("Would you like to exit(y/n):")
      return signup(exit)
    else:
      #if password and username meets the requirements we can append it to the file
      if checkPassword(pwd1) == True:
        # IN-15: also ask for first and last name
        valid = False
        while not valid:
          fname = input("\nEnter your first name: ")
          lname = input("Enter your last name: ")
          valid, fname, lname = validName(fname, lname)
          if (not valid):
            print(
              "Invalid input detected in either first name or last name.  If you believe this to be an error, please contact us through the information that is currently not provided."
            )
            exit = input("Would you like to exit?(y/n): ")
            if (exit == 'y'):
              return signup(exit)
        #major = input("Enter your major: ")
        #university = input("Enter your university: ")
        valid = False
        while not valid:
          email = input("\nEnter your email: ")
          valid = validEmail(email)
          if (not valid):
            print(
              "Invalid input detected in email provided.  If you believe this to be an error, please contact us through the information that is currently not provided."
            )
            exit = input("Would you like to exit?(y/n): ")
            if (exit == 'y'):
              return signup(exit)
        valid = False
        while not valid:
          phone = input(
            "\nEnter your phone number(Please Format Like ###-###-####): ")
          valid = validPhone(phone)
          if (not valid):
            print(
              "Invalid input detected in phone number provided.  If you believe this to be an error, please contact us through the information that is currently not provided."
            )
            exit = input("Would you like to exit?(y/n): ")
            if (exit == 'y'):
              return signup(exit)
        #newAccount(username,pwd1,fname,lname,major,university,email,phone)

        valid = False  #Plus/Standard acc
        while not valid:
          status = input(
            "\nSelect the type of account you would like to create\n1. Standard(free)\n2. Plus($10/month)\nType 1 or 2: "
          )
          if status == "1":
            accType = 0
            valid = True
          elif status == "2":
            accType = 1
            valid = True
          else:
            print("Invalid input")
            exit = input("Would you like to exit?(y/n): ")
            if (exit == 'y'):
              return signup(exit)

        newAccount(username, pwd1, fname, lname, email, phone, accType)
        userID = getUserId(username)
        P_Notifications(userID)
      else:
        print(
          "ERROR: Please ensure that the password follows all the requirements!"
        )
        exit = input("Would you like to exit(y/n):")
        return signup(exit)
