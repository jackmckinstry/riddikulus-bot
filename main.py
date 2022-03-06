# Created by Jack McKinstry & Michael Munhbold for HackCU 8

# keys.py is private, not tracked in repo, contains secret tokens
from keys import *

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

run = True # TODO remove when done, set to while(true)
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
        
        print("ID: " + tweetID)
        print("Message: " + tweetMessage)
        print ("Author: " + authorUsername)

        ### check list to see if tweet ID is unique
        if tweetIDsResponded.__contains__(tweetID):
            print("Already responded to this tweet")
        else:
            ### if tweet is unique, not in list:
            spell = ""

            ### check for spell in message
            if tweetMessage.lower().__contains__("accio"):
                spell = "accio"
            elif tweetMessage.lower().__contains__("alohomora"):
                spell = "alohomora"
            elif tweetMessage.lower().__contains__("avada kedavra"):
                spell = "avada kedavra"
            elif tweetMessage.lower().__contains__("expecto patronum"):
                spell = "expecto patronum"
            elif tweetMessage.lower().__contains__("expelliarmus"):
                spell = "expelliarmus"
            elif tweetMessage.lower().__contains__("lumos"):
                spell = "lumos"
            elif tweetMessage.lower().__contains__("obliviate"):
                spell = "obliviate"
            # extra space on this case so @riddikulusbot isn't considered casting this spell
            elif tweetMessage.lower().__contains__("riddikulus "):
                spell = "riddikulus"
            elif tweetMessage.lower().__contains__("sectum sempra"):
                spell = "sectum sempra"
            elif tweetMessage.lower().__contains__("wingardium leviosa"):
                spell = "wingardium leviosa"
            else:
                spell = "muggle"

            ### if no spell, tweet muggle reply and link to spells to cast
            if (spell == "muggle"):
                print("muggle")

                # TODO call function for muggle gif
            
            ### if spell detected, continue here
            else:
                print(spell)

                ### download user's profile picture
                # TODO 

                ### place profile picture on appropriate gif for spell
                # TODO # call image overlay method here with spell name

            ### upload image to imgur
            path = "wizardRobot.jpg" # TODO, change this image path
            im = pyimgur.Imgur(imgur_client_id)
            titleName = authorUsername + " casts " + spell + "!"
            uploaded_image = im.upload_image(path, title=titleName)
            print(uploaded_image.link)

            ### if muggle, custom tweet text
            if spell == "muggle":
                tweet_text = "@" + authorUsername + " Your tweet doesn't contain a spell you can cast, muggle! Check out the spells you can cast at the link in my bio."
            else:
                tweet_text = "@" + authorUsername + " casts " + spell + "!"
            
            ### respond to tweet with appropriate image
            img_link = uploaded_image.link
            img_link = img_link.replace('https://i.', '')
            img_link = img_link.replace('.png', '')
            tweet_text += " " + img_link

            # client.create_tweet(text=tweet_text) # TODO uncomment to make tweet
            
            print(tweet_text + " --- tweeted!")

            ### append ID to list of tweets responded to, so it isn't responded to multiple times
            tweetIDsResponded.append(tweetID)
            run = False # TODO remove
    ### sleep for 60 seconds before repeating loop, twitter caps us at 500k requests per month, each mention request = 10
    # time.sleep(60) # TODO uncommment this