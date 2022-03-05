# Created by Jack McKinstry & Michael Munhbold for HackCU 8

from keys import *
import tweepy

import requests

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

msg = "Hello, HackCU 8!"
print(msg)

#mediaID1 = mediaID = client.media_upload("media1.png")

textToTweet = input("Type tweet to send out: ")

client.create_tweet(text=textToTweet)

print(textToTweet + " --- sent!")