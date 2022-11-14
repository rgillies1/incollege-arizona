from database import getProfile, sendNotification


def P_Notifications(userID):
  profile = getProfile(userID)
  if (profile == (None, None)):
    sendNotification("Dont forget to create a profile!", 6)


#def New_User_Alert():
#if (config.current_user != config.user):
#print("**************Notification******************")
#print("{0} just joined InCollege!".format(config.user))
