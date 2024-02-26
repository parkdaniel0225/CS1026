# Compsci 1026A Assignment #3
# Daniel Park

def compute_tweets(tweets, keywords) -> str:
    zone = []
    # Storing keywords and values into dictionary
    try:
        keyFile = open(keywords, 'r', encoding='utf-8')
        string = keyFile.read()
        dictionary = {}
        for line in string.split('\n'):
            splitted = line.split(',')
            try:
                dictionary[splitted[0].strip()] = int(splitted[1].strip())
            except:
                pass
        # Storing Values
        valueDict = {'eastHappiness': 0, 'pacificHappiness': 0, 'mountHappiness': 0, 'centHappiness': 0,
                     'eastTweetCount': 0, 'pacificTweetCount': 0, 'mountTweetCount': 0, 'centTweetCount': 0,
                     'eastScore': 0, 'pacificScore': 0, 'mountScore': 0, 'centScore': 0, 'eastTweetCountKey': 0,
                     'pacificTweetCountKey': 0, 'mountTweetCountKey': 0, 'centTweetCountKey': 0}

        tweetsFile = open(tweets, 'r', encoding='utf-8')

        for line in tweetsFile:
            line = line.lower()
            line = line.rstrip('\n')
            splitLine = line.split()

            latStrip1 = splitLine[0].rstrip(',')
            latStrip2 = latStrip1.lstrip('[')
            latitude = float(latStrip2)

            longStrip = splitLine[1].rstrip(']')
            longitude = float(longStrip)

            # Assigning timezones
            if (24.660845 <= latitude <= 49.189787) and (-67.444574 >= longitude >= -87.518395):
                valueDict['eastTweetCount'] += 1
                for element in splitLine:
                    if element in dictionary:
                        num = dictionary[element]
                        valueDict['eastTweetCountKey'] += 1
                        valueDict['eastScore'] += num

                if valueDict['eastTweetCountKey'] > 0:
                    valueDict['eastHappiness'] = round(valueDict['eastScore'] / valueDict['eastTweetCountKey'], 2)

            if (24.660845 <= latitude <= 49.189787) and (-87.518395 >= longitude >= -101.998892):
                valueDict['centTweetCount'] += 1
                for element in splitLine:
                    if element in dictionary:
                        num = dictionary[element]
                        valueDict['centTweetCountKey'] += 1
                        valueDict['centScore'] += num

                if valueDict['centTweetCountKey'] > 0:
                    valueDict['centHappiness'] = round(valueDict['centScore'] / valueDict['centTweetCountKey'], 2)

            if (24.660845 <= latitude <= 49.189787) and (-101.998892 >= longitude >= -115.236428):
                valueDict['mountTweetCount'] += 1
                for element in splitLine:
                    if element in dictionary:
                        num = dictionary[element]
                        valueDict['mountTweetCountKey'] += 1
                        valueDict['mountScore'] += num

                if valueDict['mountTweetCountKey'] > 0:
                    valueDict['mountHappiness'] = round(valueDict['mountScore'] / valueDict['mountTweetCountKey'], 2)

            if (24.660845 <= latitude <= 49.189787) and (-115.236428 >= longitude >= -125.242264):
                valueDict['pacificTweetCount'] += 1
                for element in splitLine:
                    if element in dictionary:
                        num = dictionary[element]
                        valueDict['pacificTweetCountKey'] += 1
                        valueDict['pacificScore'] += num

                if valueDict['pacificTweetCountKey'] > 0:
                    valueDict['pacificHappiness'] = round(valueDict['pacificScore'] / valueDict['pacificTweetCountKey'], 2)
        tweetsFile.close()

        # Printing final results
        return f"""
Eastern has a happiness score of {valueDict['eastHappiness']}, has {valueDict['eastTweetCountKey']} tweets with keywords and {valueDict['eastTweetCount']} total tweets.
Central has a happiness score of {valueDict['centHappiness']}, has {valueDict['centTweetCountKey']} tweets with keywords and {valueDict['centTweetCount']} total tweets.
Mountain has a happiness score of {valueDict['mountHappiness']}, has {valueDict['mountTweetCountKey']} tweets with keywords and {valueDict['mountTweetCount']} total tweets.
Pacific has a happiness score of {valueDict['pacificHappiness']}, has {valueDict['pacificTweetCountKey']} tweets with keywords and {valueDict['pacificTweetCount']} total tweets.
            """

    except IOError:
        print(f"Error: {tweets} does not exist.")
        print(zone)
