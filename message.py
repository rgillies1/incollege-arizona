from database import sendMessage, getInbox, getFriends, deleteMessage, markAsRead, userRecords, isUserPlus


def messages():
  inbox = getInbox()
  valid_inputs = ["1", "2", "Exit"]
  selection = ""
  accType = isUserPlus() #returns False for Standard and True for Plus

  while selection != "Exit":
    print("\n============ Messaging ============")
    print("Select an option:")
    print("1. View messages")
    print("2. Send a message")
    print("Or type 'Exit' to go back to the previous menu.")
    selection = input("Select an option from above: ")
    while selection not in valid_inputs:
      selection = input("Invalid input! Select an option from above: ")

    if selection == "1":
      if len(inbox) == 0:
        print("\nYou have no messages at this time!\n")
        continue
      else:
        index = 0
        for userId, username, messageId, message, read in inbox:
          print("")
          index = index + 1
          if not read:
            print("{0}. Message from {1} (UNREAD):".format(index, username[0]))
          else:
            print("{0}. Message from {1}:".format(index, username[0]))
          print("\t"+message[0])

        selection = input(
          "Select a message to read, or type 'Exit' to go back: ")
        selection = int(selection) if selection.isdigit() else "Exit"
        print("")
        if selection != "Exit":
          if selection in range(1, len(inbox) + 1):
            selectedMessage = inbox[selection - 1]
            id = selectedMessage[0]
            username = selectedMessage[1][0]
            messageId = selectedMessage[2]
            message = selectedMessage[3][0]
            isRead = selectedMessage[4]
            print("Message from {0}:".format(username))
            print("\t"+message + '\n')

            if (not isRead):
              markAsRead(messageId)
              print("This message has been marked as read.")
              inbox = getInbox()

            print("Available actions for this message: ")
            print("1. Delete")
            print("2. Reply")
            selection = input(
              "Select an option from above, or type 'Exit' to go back: ")

            if (selection == "1"):
              deleteMessage(messageId)
              print("Message from {0} deleted!".format(username))
              inbox = getInbox()
            elif (selection == "2"):
              reply = input("Enter you message for {0}: ".format(username))
              sendMessage(id, reply)
              print("Message sent to {0}!".format(username))
            elif (selection == "Exit"):
              selection = ""
              continue
        else:
          selection = ""
          continue

    elif selection == "2":
      print("Send a message to...")
      print("1. A friend on my friend's list")
      print("2. Another InCollege User")

      selection = input("Select an option from above: ")
      print("")
      while selection not in valid_inputs:
        selection = input("Invalid input! Select an option from above: ")

      if (selection == "1"):
        friends = getFriends()
        if (len(friends) == 0):
          print("\nYou don't have any friends...\n")
          continue

        index = 0
        for username, _ in friends:
          index = index + 1
          print(str(index) + ". " + str(username))

        selection = input(
          "Select a user from above to send a message to, or type 'Exit': ")

        selection = int(selection) if selection.isdigit() else "Exit"

        if selection != "Exit":
          if selection in range(1, len(friends) + 1):
            receiver = friends[selection - 1]
            message = input("Enter you message for {0}: ".format(receiver[0]))

            sendMessage(receiver[1], message)
            print("Message sent to {0}!".format(receiver[0]))
        else:
          selection = ""
          continue

      elif (selection == "2"):
        if accType == 0:
          print("\nYou need a Plus Account to do this")
          pass
        else:
          allUsers = userRecords()
          index = 0
          for user in allUsers:
            index = index + 1
            print(str(index) + ". " + str(user[1]))
  
          selection = input(
            "Select a user from above to send a message to, or type 'Exit': ")
  
          selection = int(selection) if selection.isdigit() else "Exit"
  
          if selection in range(1, len(allUsers) + 1):
            receiver = allUsers[selection - 1]
            if receiver[1] not in getFriends(): 
              if accType == 0:
                print("\nI'm sorry, you are not friends with that person.\n")
              else:
                message = input("Enter you message for {0}: ".format(
                  receiver[1]))
                sendMessage(receiver[0], message)
                print("Message sent to {0}!".format(receiver[1]))
