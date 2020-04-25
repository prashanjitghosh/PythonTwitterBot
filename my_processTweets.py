import my_DataManager

def processtweetsforusers(users, queuereceived,callback,twitterHandle,lastProcessedId):
    for user in users:
        if queuereceived.tweetsOfDifferentUsers.CheckKey(str(user)):
            usersTweetsTobeRespondedList = queuereceived.tweetsOfDifferentUsers[str(user)]
            numberoftweetsbythisuser = 0
            for key, value in usersTweetsTobeRespondedList.items():
                numberoftweetsbythisuser +=1
                print ("Tweet " + "ID=" + str(int(key)) +"   Tweet::--->" +value + "   From user:" + str(user) )
                #will repond back only if the tweet has a # in the message 
                #this value after after # will be the Command or the message the user wants to send us
                if '#' in str(value).lower():
                    HashtagReceived =  (str(value).lower()).split("#",1)[1]
                    print ("Will send replies back  to the hastag " + HashtagReceived + ' in the tweet')
                    twitterHandle.update_status('@' +str(user)+' Your hastag '+ HashtagReceived + ' is Acknowledged' , int(key))
    callback(lastProcessedId)

def CleanUpPreviousTweets( users, queuereceived,callback):
    for user in users:
        if queuereceived.tweetsOfDifferentUsers.CheckKey(str(user)):
            usersTweetsTobeRespondedList = queuereceived.tweetsOfDifferentUsers[str(user)]
            for key in list(usersTweetsTobeRespondedList):
                del usersTweetsTobeRespondedList[key]
    callback()
