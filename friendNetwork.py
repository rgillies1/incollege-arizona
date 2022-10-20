from database import getFriendRequests, removeFriendRequest, getFriends, addFriend, removeFriend 

def friendNetwork(
):  #Friend Network Page, add and remove friend functionality here
    choice = -1
    while (choice != 4):
        openFriendRequests = getFriendRequests()
        friends = getFriends()
        print(
            "\n1. Look at friends \n2. Remove friend \n3. Look at friend requests \n4. Exit"
        )
        choice = int(input("Please choose from the list above: "))
        if (choice == 1 or choice == 2):
            print("")
            if (len(friends) == 0):
                print("You are a lonely loser")
                continue
            for i in range(0, len(friends)):
                print(str(i + 1) + ". " + friends[i][0])
            if (choice == 2 and len(friends)>0):#Remove friend and their are friends to remove
                remove = int(
                    input(
                        "Pick which friend you would like to remove.  Input 0 to select none: "
                    ))
                if (remove == 0 or remove > len(friends)):#Choice displayed doesn't exist
                    continue
                removeFriend(friends[remove-1][1])#Removes Friend
            elif(choice==2):
                print("No friends to remove")
        elif (choice == 3):
            print("\n")
            if (len(openFriendRequests) == 0):
                print("No requests at this time")
                continue
            for i in range(0, len(openFriendRequests)):
                print(str(i + 1) + ". " + openFriendRequests[i][0])
            request = int(
                input(
                    "Select a friend request to deal with. Input 0 to select none: "
                ))
            if (request > 0 and request - 1 < len(openFriendRequests)):
                addOrRemove = int(
                    input(
                        "Type 1 to accept friend request or 0 to decline friend request: "
                    ))
                if (addOrRemove):
                    addFriend(openFriendRequests[request - 1][1])
                removeFriendRequest(openFriendRequests[request - 1][1])
    