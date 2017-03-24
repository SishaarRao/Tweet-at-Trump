#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

USERNAME = "Sishaar"
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
        print(status.text)
        if not "@"+USERNAME in status.text:
            client.update_status("@" + (USERNAME) + " "  + message, status.id_str)
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = client.auth, listener=myStreamListener)

followAcc = []
followAcc.append(ID)
print(followAcc)

myStream.filter(follow=followAcc)
#myStream.userstream(async=True)


