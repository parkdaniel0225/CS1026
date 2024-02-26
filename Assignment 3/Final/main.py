from sentiment_analysis import compute_tweets

results = compute_tweets(input("Please enter the file name and extension of the tweetfile: "), input("Please enter the file name and extension of the keyfile: "))
print(results)
