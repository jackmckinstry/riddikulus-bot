# Created by Jack McKinstry & Michael Munhbold for HackCU 8

# keys.py is private, not tracked in repo, contains secret tokens
from keys import *
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
    ### parse data
    res = json.loads(client.get_users_mentions(id=twitter_user_id).content)
    
    ### for tweets in mentioned:
    for x in range(0, res['meta']['result_count']):
        print(x)
        tweetID = (res['data'][x]['id']) # tweet ID
        tweetMessage = (res['data'][x]['text']) # message in tweet
        tweetResp = client.get_tweet(id=res['data'][x]['id'],expansions='author_id')
        tweet = json.loads(tweetResp.content)
        authorUsername = (tweet['includes']['users'][0]['username']) # author of tweet's twitter handle
        authorID = (tweet['includes']['users'][0]['id']) # UUID of author of tweet's twitter account
        
        print("Tweet ID: " + tweetID)
        print("Message: " + tweetMessage)
        print("Author: " + authorUsername)
        print("Author ID: " + authorID)

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
                produceGif("muggle")
            
            ### if spell detected, continue here
            else:
                print(spell)

                # get profile picture of user from Twitter
                userResp = client.get_user(id=authorID,user_fields=['profile_image_url'])
                userInfo = json.loads(userResp.content)
                print (userInfo['data']['profile_image_url']) # TODO remove
                profPic = userInfo['data']['profile_image_url']
                # make photo larger than original grabbed, higher quality
                profURL = profPic.replace('_normal.jpg', '_400x400.jpg')
                print(profURL)

                ### download user's profile picture, save image as pfp.png
                # TODO

                ### place profile picture on appropriate gif for spell
                ### call image overlay method here with spell name
                produceGif(spell)

                ### upload image to imgur
                path = "output.gif"
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
    ### sleep for 120 seconds before repeating loop, 
    ### twitter caps us at 500k tweets requests per month, and 100 calls per hour
    # time.sleep(120) # TODO uncommment this