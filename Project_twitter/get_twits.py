import got3
def twitts(start_date,end_date,name):
    max_tweets = 10
    tweetCriteria = got3.manager.TweetCriteria().setSince(start_date).setUntil(end_date).setQuerySearch(
        name).setTopTweets(True).setLang('en').setMaxTweets(max_tweets)
    z = []
    for i in range(max_tweets):
        tweet = got3.manager.TweetManager.getTweets(tweetCriteria)[i]
        z.append(tweet.text)
    for i in z:
        print(i, '\n')
