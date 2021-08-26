# Authentication
import tweepy
consumerKey = "************************"
consumerSecret = "***************************************"
accessToken = "*****************************"
accessTokenSecret = "*****************"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth, sleep_on_rate_limit=False, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

