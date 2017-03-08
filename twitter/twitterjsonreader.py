import json


tweets_filename='tweets.json'

with open(tweets_filename) as data_file:
   alldata = json.loads (data_file.read())
   for tweet in alldata:
      geo=str(tweet['geo'])
      if (geo=="None"):
         geo=""
      print (tweet['user']['name']+ " " +tweet['text']+" "+ geo)

