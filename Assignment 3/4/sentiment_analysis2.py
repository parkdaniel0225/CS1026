def compute_tweets(tweetfile, keywordfile):
    # opening files
    try:
        rawtweet = open(tweetfile + ".txt", "r")
        rawkeywords = open(keywordfile + ".txt", "r")
    except IOError:
        return []

    eastscore = 0
    centralscore = 0
    mountscore = 0
    pacificscore = 0

    eastcount = 0
    centralcount = 0
    mountcount = 0
    pacificcount = 0

    eastkeycount = 0
    centralkeycount = 0
    mountkeycount = 0
    pacifickeycount = 0

    # adding keywords to a dictionary with their associated values
    keyword = rawkeywords.readline()
    dictionary = {}
    while keyword != "":
        i = 0
        tempname = ""
        tempval = ""
        while i < len(keyword):
            if keyword[i].isalpha():
                tempname = tempname + keyword[i]
            elif keyword[i].isnumeric():
                tempval = tempval + keyword[i]
            i += 1
        dictionary[tempname] = tempval
        keyword = rawkeywords.readline()

    tweetline = rawtweet.readline()
    while tweetline != "":

        # isolating the raw tweet and taking its coordinates
        i = 0
        spaces = 0
        loc1 = ""
        loc2 = ""
        tweet = ""
        while i < len(tweetline):
            if tweetline[i] == " ":
                spaces += 1
            if spaces > 4:
                # new variable for storing the tweet
                tweet = tweet + tweetline[i]
            if spaces < 1:
                if tweetline[i].isnumeric() or tweetline[i] == "." or tweetline[i] == "-":
                    loc1 = loc1 + tweetline[i]
            elif spaces == 1:
                if tweetline[i].isnumeric() or tweetline[i] == "." or tweetline[i] == "-":
                    loc2 = loc2 + tweetline[i]
            i += 1
        location = [float(loc1), float(loc2)]

        # placing the tweet into a list + lowercasing
        temp = ""
        words = []
        i = 0
        while i < len(tweet):
            tweet.lstrip(" ")
            if tweet[i] != " ":
                temp = temp + tweet[i]
            elif tweet[i] == " ":
                words.append(temp.lower())
                temp = ""
            i+=1

        # stripping punctuation from the words in the tweet
        i = 0
        j = 0
        temp = ""
        while i < len(words):
            j = 0
            while j < len(words[i]):
                if not words[i][j].isalpha():
                    words[i] = words[i].replace(words[i][j], "")
                    j = 0
                j+=1
            i+=1


        # tweet is isolated in a list
        # dictionary contains keywords and their values
        # location is a list of the coordinates

        # calculate sentiment
        i = 0
        score = 0
        istweetkey = False
        while i < len(words):
            if words[i] in dictionary:
                score = score + int(dictionary.get(words[i]))
                istweetkey = True
            i+=1

        # find location
        zone = 0

        if -67.444574 > location[1] > -87.518395:
            # eastern
            zone = 1
        elif -87.518395 > location[1] > -101.998892:
            # central
            zone = 2
        elif -101.998892 > location[1] > -115.236428:
            # mountain
            zone = 3
        elif -115.236428 > location[1] > -125.242264:
            # pacific
            zone = 4
        else:
            # outside location
            zone = 0

        # tally the number of tweets
        if zone == 0:
            print()
        elif zone == 1:
            eastscore = eastscore + score
            if istweetkey == True:
                eastkeycount += 1
            eastcount += 1
        elif zone == 2:
            centralscore = centralscore + score
            if istweetkey == True:
                centralkeycount += 1
            centralcount += 1
        elif zone == 3:
            mountscore = mountscore + score
            if istweetkey == True:
                mountkeycount += 1
            mountcount += 1
        else:
            pacificscore = pacificscore + score
            if istweetkey == True:
                pacifickeycount += 1
            pacificcount += 1
        tweetline = rawtweet.readline()

    # create tuples
    if eastcount != 0:
        eastern = [eastscore/eastcount, eastkeycount, eastcount]
    else:
        eastern = [0, eastkeycount, eastcount]
    if centralcount != 0:
        central = [centralscore/centralcount, centralkeycount, centralcount]
    else:
        central = [0, centralkeycount, centralcount]
    if mountcount != 0:
        mountain = [mountscore/mountcount, mountkeycount, mountcount]
    else:
        mountain = [0, mountkeycount, mountcount]
    if pacificcount != 0:
        pacific = [pacificscore/pacificcount, pacifickeycount, pacificcount]
    else:
        pacific = [0, pacifickeycount, pacificcount]

    # return list
    return [eastern, central, mountain, pacific]

