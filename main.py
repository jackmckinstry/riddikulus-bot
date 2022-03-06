# Created by Jack McKinstry & Michael Munhbold for HackCU 8
# collection of potential gifs to use: https://imgur.com/gallery/1hmdv


# keys.py is private, not tracked in repo, contains secret tokens
from keys import *
from imageOverlay import *
import tweepy
import pyimgur
import requests
import time

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

tweetIDsResponded = list()

print('Starting Riddikulus Bot...')

### only run the loop and look for tweets to respond to once per minute
while(True):
    # 1500192103485218816 is @riddikulusbot's twitter ID
    print(client.get_users_mentions(id='1500192103485218816').content)

    ### parse data

    ### for tweets in mentioned:
        ### check list to see if tweet ID is unique
        # tweetIDsResponded.__contains__("ID HERE") # ensure that haven't responded to tweet already 
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
    time.sleep(60) 