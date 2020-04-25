import tweepy
import my_dictionaryUtil
import my_DataManager 
import my_fileManager
import my_processTweets 
import time

class information():
    configed_fileNameForlastProcessedId = ''
    lastProcessedId = 0
    maxTweetsTobeReceived = 0
    consumerKey = ''
    consumerSecret = ''
    accesskey = ''
    accessSecret = ''
    authHandler = tweepy.OAuthHandler
    api = tweepy.API
    AccountNames = []
    mentionsManager = my_DataManager.datamanager
    def __init__(self):
         self.configed_fileNameForlastProcessedId = my_fileManager.GetConfigurationValue("configurations.txt","File_name")
         self.lastProcessedId = lastProcessedId = my_fileManager.GetLastProcessedId(self.configed_fileNameForlastProcessedId)
         self.maxTweetsTobeReceived = int(my_fileManager.GetConfigurationValue("configurations.txt","MAXIMUM_TWEETS_TOBERECIEVEDINONE_REST"))
         self.consumerKey = my_fileManager.GetConfigurationValue("configurations.txt","CONSUMER_KEY")
         self.consumerSecret = my_fileManager.GetConfigurationValue("configurations.txt","CONSUMER_SECRET")
         self.accesskey = my_fileManager.GetConfigurationValue("configurations.txt","ACCESS_KEY")
         self.accessSecret = my_fileManager.GetConfigurationValue("configurations.txt","ACCESS_SECRET")
         self.authHandler =  tweepy.OAuthHandler(self.consumerKey,self.consumerSecret)
         self.authHandler.set_access_token(self.accesskey,self.accessSecret)
         self.api = tweepy.API(self.authHandler)
         self.AccountNames =  my_fileManager.GetConfigurationValueList("configurations.txt","AccountName")
         self.mentionsManager = my_DataManager.datamanager('notifications')

    def GetFreshTweetsAndProcessThem(self):
        mentions = self.api.mentions_timeline(self.lastProcessedId)
        self.lastProcessedId = self.mentionsManager.update(self.lastProcessedId,mentions)
        my_processTweets.processtweetsforusers(self.AccountNames,self.mentionsManager,
                                                                            callbackafterprocessingsetoftweet,
                                                                            self.api,#pass the twitter handle
                                                                            self.lastProcessedId)  #pass the lastID of the tweet whcih need to be updated  after processing.

        my_processTweets.CleanUpPreviousTweets(self.AccountNames,self.mentionsManager,
                                                                            callbackafterCleaningsetoftweet)



        
def initializations():
    twitterBot = information()   #create my main object
    return twitterBot


def main():
    twitterBot = initializations()
    while(True):
        twitterBot.GetFreshTweetsAndProcessThem()
        time.sleep(60 * 1)
"""

def main():
    configed_fileNameForlastProcessedId = my_fileManager.GetConfigurationValue("configurations.txt","File_name")
    if (configed_fileNameForlastProcessedId is not None):
         lastProcessedId = my_fileManager.GetLastProcessedId(configed_fileNameForlastProcessedId)
         maxTweetsTobeReceived = int(my_fileManager.GetConfigurationValue("configurations.txt","MAXIMUM_TWEETS_TOBERECIEVEDINONE_REST"))
         #Authentication with Twitter for my App hosted on Twitter.com 
         CONSUMER_KEY = my_fileManager.GetConfigurationValue("configurations.txt","CONSUMER_KEY")
         CONSUMER_SECRET = my_fileManager.GetConfigurationValue("configurations.txt","CONSUMER_SECRET")
         ACCESS_KEY =  my_fileManager.GetConfigurationValue("configurations.txt","ACCESS_KEY")
         ACCESS_SECRET = my_fileManager.GetConfigurationValue("configurations.txt","ACCESS_SECRET")
         auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
         auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
         api = tweepy.API(auth)
         
         #get list of user to which I need to respond to 
         AccountNames = my_fileManager.GetConfigurationValueList("configurations.txt","AccountName")
         mentionsManager = my_DataManager.datamanager('notifications')
         publicTweetsManager = my_DataManager.datamanager('publicTweets')
         
         #public_tweets = api.home_timeline()  #Can be used for processing tweet on my homeline
         #mentions = api.mentions_timeline()     #use to get all tweets mentioning me from all times
         mentions = api.mentions_timeline(lastProcessedId)
         
         lastProcessedId = mentionsManager.update(lastProcessedId,mentions) 
         #publicTweetsManager.update(public_tweets)
         
         my_processTweets.processtweetsforusers(AccountNames,mentionsManager,
                                                                            callbackafterprocessingsetoftweet,
                                                                            api,#pass the twitter handle
                                                                            lastProcessedId)  #pass the lastID of the tweet whcih need to be updated  after processing.

         my_processTweets.CleanUpPreviousTweets(AccountNames,mentionsManager,
                                                                            callbackafterCleaningsetoftweet)

"""

def callbackafterCleaningsetoftweet():
    print ("Done cleaning up the processed tweets..")

def callbackafterprocessingsetoftweet(lastProcessedId):
    print ("Done processing tweets..")
     #Can now update the lastProcessedId so that next time I get fresh new tweets 
    configed_fileNameForlastProcessedId = my_fileManager.GetConfigurationValue("configurations.txt","File_name")
    if (configed_fileNameForlastProcessedId is not None):
        my_fileManager.UpdateLastProcessedId(configed_fileNameForlastProcessedId, lastProcessedId)

if __name__ == "__main__":
    main()

