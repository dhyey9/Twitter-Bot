import tweepy
import time
import random

auth = tweepy.OAuthHandler('QABhnoN7v30mZwxgaU9BScWop','Ohy8s6FSheegH3iPplU9e6VqdIXCdWTAQaXLcUXgJoMYkXE7JE')  #add api secrets from developer account
auth.set_access_token('1230696752493121536-tqs6WKix0kX4AqGb8cuuRMe0jNRGxm','lbmYT15sd8HzFNWXyS34iA69UudrzMpuRU99JlLFlPHoX') #add tokens from developer account

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

print(user.screen_name) #print if successfully logged in

username=input('Please Enter Username of the twitter account you want to auto like and retweet:')
number = input('Enter the number of posts you want to like and retweet:')
#'BillGates'
tweets1 = tweepy.Cursor(api.user_timeline, id=username).items(number) #change the id with the id you want to like and tweet

def autobot():
	for tweet in tweets1:
		if not tweet.favorited:
			try:
				print('Liked The Tweet of {}'.format(username))
				tweet.favorite()
				x = random.randint(5,60)
				print("Another action will start after %d seconds" %x) 
				time.sleep(x)
			except tweepy.TweepyError as e:
				print(e.reason)
		if not tweet.retweeted:
			try:
				print('Retweeted the Tweet of {}'.format(username))
				tweet.retweet()
				x = random.randint(5,60)
				print("Another action will start after %d seconds" %x) 
				time.sleep(x)
			except tweepy.TweepyError as e:
				print(e.reason)
autobot()