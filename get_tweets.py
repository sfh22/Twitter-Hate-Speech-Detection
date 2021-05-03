import tweepy
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "8RAcNLC2By5touODBTfUJnaSg"
# api secret key
api_secret_key = "ep2kZAi0n4cD3Fw0fFnr9eqGcqftmvn7yFaVls3hv8OHrXKlUm"
# access token
access_token = "1210030934382325760-dznsIdiemc2agWTYD1XHIvwdtnae1d"
# access token secret
access_token_secret = "rJSF0D1Q1LP7kQENxQLwmadTAqDQwONBnYnqXrQLVRLLc"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, lang="ar", count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            #'created_at': tweet.created_at,
            tweets_list.append({
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
