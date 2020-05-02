import tweepy
import json
import pandas as pd
# api keys and acess tokens are stored in a seperate file to make sure they don't get uploaded by mistake

file_path = "../twitter_keys.json"

with open(file_path, 'r') as file:
	content = file.read()
	twitter_keys = json.loads(content)

API_KEY  = twitter_keys['api_key']
API_SECRET_KEY = twitter_keys['api_secret_key']
ACCESS_TOKEN = twitter_keys['access_token']
ACCESS_TOKEN_SECRET = twitter_keys['access_token_secret']

# authentication using our keys
auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# get tweet ids from the archives
tweet_ids = pd.read_csv('twitter_archive_enhanced.csv')['tweet_id'].values.tolist() 


tweet_data = {}
failed_tweets = []
for tweet in tweet_ids:
	try:
		tweet_info = api.get_status(tweet, tweet_mode='extended')
		tweet_data[tweet] = tweet_info._json
		print("Success: got tweet with id: {}".format(tweet))
	except tweepy.TweepError as e:
		failed_tweets.append(tweet)
		print("Fail:  tweet with id {} was not retrieved".format(tweet))
with open('./tweets_extended.json', 'w') as outfile:
	# add tweet information to a json file
	json.dump(tweet_data,outfile,sort_keys=True)

with open('./deleted_tweets.json','w') as deleted_file:
	json.dump(failed_tweets,deleted_file,sort_keys=True)

