# Created by Jack McKinstry & Michael Munhbold for HackCU 8

# keys.py is private, not tracked in repo, contains secret tokens
from keys import *
from imageOverlay import *
from imageOverlayFormat import *
from gitOverlay import *

import tweepy
import pyimgur

import json
import requests
import time

# sign into api with account information
client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

tweetIDsResponded = list()

print('Starting Riddikulus Bot...')
run = True

### only run the loop and look for tweets to respond to once per minute
while(run):
    # 1500192103485218816 is @riddikulusbot's twitter ID
    ### parse data
    res = json.loads(client.get_users_mentions(id='1500192103485218816').content)
    
    ### for tweets in mentioned:
    for x in range(0, res['meta']['result_count']):
        print(x)
        tweetID = (res['data'][x]['id']) # tweet ID
        tweetMessage = (res['data'][x]['text']) # message in tweet
        tweetResp = client.get_tweet(id=res['data'][x]['id'],expansions='author_id')
        tweet = json.loads(tweetResp.content)
        authorUsername = (tweet['includes']['users'][0]['username']) # author of tweet
        
        print(tweetID)
        print(tweetMessage)
        print (authorUsername)

        if tweetIDsResponded.__contains__(tweetID):
            print('hi')

        run = False # TODO remove

        ### check list to see if tweet ID is unique
        ### if tweet is unique, not in list:
            ### check for spell in message
            ### if no spell, tweet muggle reply and link to spells to cast
            ### if spell, download user's profile picture and continue
            ### place profile picture on appropriate gif for spell
            ### upload image to imgur
            # path = "wizardRobot.jpg" # TODO, change this image path
            # im = pyimgur.Imgur(imgur_client_id) TODO
            # uploaded_image = im.upload_image(path, title="NAME + SPELL NAME") TODO
            # print(uploaded_image.link) TODO


            ### respond to tweet with appropriate image
            # tweet_text = "@ USERNAME + SPELL NAME"
            # img_link = uploaded_image.link
            # img_link = img_link.replace('https://i.', '')
            # img_link = img_link.replace('.png', '')
            # tweet_text += " " + img_link

            #client.create_tweet(text=tweet_text)
            
            # print(tweet_text + " --- tweeted!")

            ### append ID to list of tweets responded to, so it isn't responded to multiple times
            # tweetIDsResponded.append("ID HERE")
    ### sleep for 60 seconds before repeating loop, twitter caps us at 500k requests per month, each mention request = 10
    # time.sleep(6000) # TODO reduce to 60 