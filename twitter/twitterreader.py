import twitter
import json
import ConfigParser

## this code uses this API https://pypi.python.org/pypi/twitter
## install, e.g doing pip install twitter

 
# Need tokens from Twitter
# 1. Join : https://dev.twitter.com 
# 2. Get token: https://dev.twitter.com/oauth/overview
# 3. Select Just want to access the API from your own account *Tokens from dev.twitter.com*
# 4. Follow rest of instructions

# This code expects an external file_with_tokens that contains tokens values. It should be formatted like this:

#[twitter]
#CONSUMER_KEY=zlkcBxHMY0RIGRbTcNzz2kHEM
#CONSUMER_SECRET=YTcpnJdGKGuv9dfXCMGZTrL56t17Yj7tlboVuBmVkk1O9R2VvV
#TOKEN=704834572052115456-XOXFvD2zEOlWrfcEqDkfBVaCrAegdk3
#TOKEN_SECRET=G7BiAVngbXGfgBoHJbvEa96pLTewNofH51ZLZeZ8CgtzF
   
   
file_with_tokens='tokenstwitter.properties'   

config=ConfigParser.RawConfigParser()
config.read(file_with_tokens)

CONSUMER_KEY=config.get('twitter','CONSUMER_KEY') 
CONSUMER_SECRET=config.get('twitter','CONSUMER_SECRET') 
TOKEN=config.get('twitter','TOKEN') 
TOKEN_SECRET=config.get('twitter','TOKEN_SECRET') 
   

auth=twitter.oauth.OAuth(TOKEN,TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
t = twitter.Twitter(auth=auth)

## search all tweets with an @word 
word="@opengeospatial"
t2 = t.search.tweets(q="@opengeospatial",count=2)
print ("print Two last tweets containing the text "+ word)
print (json.dumps(t2, indent=4, sort_keys=True))

## Get the 10 most recent tweets form a twitter account and save them in a json file
account='berdez'
tweets_filename='tweets.json'

recent_tweets = t.statuses.user_timeline(screen_name=account,count=10)
tweets_in_json= json.dumps(recent_tweets, indent=4, sort_keys=True)

f=open(tweets_filename,'w')
f.write(tweets_in_json)
f.close()

print ("File "+tweets_filename+" was successfully create with the latest tweets from: " +account)




