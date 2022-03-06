# Created by Jack McKinstry & Michael Munhbold for HackCU 8
# collection of potential gifs to use: https://imgur.com/gallery/1hmdv


# keys.py is private, not tracked in repo, contains secret tokens
from keys import *
import tweepy
import pyimgur
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

path = "wizardRobot.jpg" # TODO, change this path

im = pyimgur.Imgur(imgur_client_id)
uploaded_image = im.upload_image(path, title="first tweet test sending image")
print(uploaded_image.link)

tweet_text = input("Type tweet to send out: ")
img_link = uploaded_image.link
img_link = img_link.replace('https://i.', '')
img_link = img_link.replace('.png', '')
tweet_text += " " + img_link

client.create_tweet(text=tweet_text)

print(tweet_text + " --- sent!")