#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# User that you want to immediately respond to
USERNAME = "realDonaldTrump"

# Read in Message that you want to tweet
filename=open("message.txt",'r')
message = ""
for line in filename.readlines():
    message += line
filename.close()

# Create client
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
    

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        if not "@"+USERNAME in status.text:
            client.update_status("@" + (USERNAME) + " "  + message, status.id_str)
    def on_error(self, status_code):
        if status_code == 420:
            return False

# Create Stream Listener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = client.auth, listener=myStreamListener)

# This is bad I know but for some reason it doesn't work unless it's like this
followAcc = []
followAcc.append(ID)
print(followAcc)

# Begin
myStream.filter(follow=followAcc)



