#!/usr/bin/env python
# vim: set fileencoding=utf-8
import tweepy
import random,time
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# array of items to search for
tweetTo = ['search item one', 'search item two']

#

# open file for reading and writing.
dbRfile = open("sent.txt","r")
dbAfile = open("sent.txt","a")
#list of specific strings we want to check for in Tweets
if __name__ == '__main__':

    for s in tweetTo:
            sn = s.user.screen_name
            # add username to persistant file to avoid spamming the same person
            dbAfile.write(s.user.screen_name + '\n')
            # post and pause for a while so the bot isn't blocked.
            if s.user.screen_name not in dbRfile:
                m = "@%s  Message you want to tweet" % (sn)
                s = api.update_status(m, s.id)
                time.sleep(random.randrange(600,1000,1))

    # auto follow back
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()

    dbAfile.close()
    dbRfile.close()
