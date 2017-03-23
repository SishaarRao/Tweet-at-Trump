#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


filename=open("message.txt",'r')
message = ""
for line in filename.readlines():
    message += line
filename.close()

try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    
    client = tweepy.API(auth)
    if not client.verify_credentials():
        raise tweepy.TweepError
    USERNAME = "Sishaar"
    USER = client.get_user(USERNAME)
    ID = USER.id_str
except tweepy.TweepError as e:
    print('ERROR : connection failed. Check your OAuth keys.')
else:
    print('Connected as @{}, you can start to tweet !'.format(client.me().screen_name))
    client_id = client.me().id
    

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        client.update_status(message, status.id_str)
        print(status)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = client.auth, listener=myStreamListener)

followAcc = []
followAcc.append((client.get_user("Sishaar")).id_str)
print(followAcc)


myStream.filter(follow=followAcc, async=True)
#myStream.userstream(async=True)


# For updating a status based on a textfile
    
#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()
#for line in f:
#    api.update_status(line)
