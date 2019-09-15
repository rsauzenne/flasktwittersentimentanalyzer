from flask import render_template, request, jsonify
from app import app
import random
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})
