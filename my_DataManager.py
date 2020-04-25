import my_dictionaryUtil 

class datamanager():
     tweetsOfDifferentUsers = my_dictionaryUtil.dictionary
     def __init__(self,type):
         self.type = type
         self.tweetsOfDifferentUsers = my_dictionaryUtil.dictionary()
             
     def update(self,lastProcessedId,item=None):
          #need to write a smart function here to check for duplicates and make a datastructe as expected 
          #As per the design.
          if (self.type == 'notifications') or (self.type == 'publicTweets'):
            
            for messagetexts in reversed(item): #first tweet first else we will get the last tweet first
                #Check if message is from a user who is already existing and have procesed some previos Tweets of him
                if self.tweetsOfDifferentUsers.CheckKey(messagetexts.user.screen_name):
                    #if this user was already added to the dictionary
                    dictOfTweestByThisUser = self.tweetsOfDifferentUsers[messagetexts.user.screen_name]
                    #Check if this message ID was already added to this user's tweet list if so no need to add to his list 
                    if dictOfTweestByThisUser.CheckKey(messagetexts.id):
                        continue
                    else:
                        #OK its a new Tweet by this user so add it to his tweet list 
                        dictOfTweestByThisUser.add(messagetexts.id,messagetexts.text)
                else:
                    #first tweet from this username so add his name as a Key to our dictionary
                    #Create a new dictionary item for the tweets of this user
                    dictOfTweestByThisUser = my_dictionaryUtil.dictionary()
                    dictOfTweestByThisUser.add(messagetexts.id,messagetexts.text)
                    self.tweetsOfDifferentUsers.add(messagetexts.user.screen_name,dictOfTweestByThisUser )
                   
          if len(item) == 0:   #if no Tweets was retrurned return the last Id of the Tweet itself
              return lastProcessedId
          else:
              #print ("The last received ID of tweet is ",messagetexts.id)
              return messagetexts.id