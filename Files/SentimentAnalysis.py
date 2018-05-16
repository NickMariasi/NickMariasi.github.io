import praw
from datetime import date
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

topSubmission = ('topSubmissions from {}.txt'.format(date.today()))
bottomSubmission = ('bottomSubmissions from {}.txt'.format(date.today()))
top = 'top.txt'
bottom = 'bottom.txt'

f = open(topSubmission, "w")
iamaTally = 0
todayilearnedTally = 0
funnyTally = 0
scienceTally = 0
worldnewsTally = 0
outoftheloopTally = 0
frugalTally = 0
youshouldknowTally = 0
soccerTally = 0
trumpTally = 0
WTFTally = 0


def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    return("{:-<40} {}".format(sentence, str(snt)))

f.write("This is the results for the Vader sentiment analysis for the TOP 10 SUBREDDITS\n")

for submission in reddit.subreddit('iama').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    f.write(scored_submissions)
    f.write("\n")

f.write("\n \n \n")
for submission in reddit.subreddit('funny').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    f.write(scored_submissions)
    f.write("\n")
f.write("\n \n \n")
for submission in reddit.subreddit('todayilearned').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    f.write(scored_submissions)
    f.write("\n")
f.write("\n \n \n")
for submission in reddit.subreddit('science').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    f.write(scored_submissions)
    f.write("\n")
f.write("\n \n \n")
for submission in reddit.subreddit('worldnews').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    f.write(scored_submissions)
    f.write("\n")
f.write("\n \n \n")

f.write("This is the TEXTBLOB analysis of the TOP 10 SUBREDDITS\n")

for submission in reddit.subreddit('iama').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    f.write(final_sentiment)
    iamaTally = iamaTally + sentiment.sentiment.polarity
    f.write("\n")
f.write("IAMA\n")
f.write("Computed Value:    ")
f.write(str(iamaTally))
f.write("\n \n \n ")


for submission in reddit.subreddit('funny').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    f.write(final_sentiment)
    funnyTally = funnyTally + sentiment.sentiment.polarity
    f.write("\n")
f.write("Funny\n")
f.write("Computed Value:    ")
f.write(str(funnyTally))
f.write("\n \n \n ")

for submission in reddit.subreddit('todayilearned').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    f.write(final_sentiment)
    todayilearnedTally = sentiment.sentiment.polarity + todayilearnedTally
    f.write("\n")
f.write("Today I Learned\n")
f.write("Computed Value:    ")
f.write(str(todayilearnedTally))
f.write("\n \n \n ")

for submission in reddit.subreddit('science').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    f.write(final_sentiment)
    scienceTally = scienceTally + sentiment.sentiment.polarity
    f.write("\n")
f.write("Science\n")
f.write("Computed Value:    ")
f.write(str(scienceTally))
f.write("\n \n \n ")


for submission in reddit.subreddit('worldnews').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    f.write(final_sentiment)
    worldnewsTally = worldnewsTally + sentiment.sentiment.polarity
    f.write("\n")
f.write("World News\n")
f.write("Computed Value:    ")
f.write(str(worldnewsTally))
f.write("\n \n \n ")






file = open(bottomSubmission, "w")
file.write("This is the results for the Vader sentiment analysis for the BOTTOM 10 subreddits\n")

for submission in reddit.subreddit('outoftheloop').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    file.write(scored_submissions)
    file.write("\n")
file.write("\n \n \n")
for submission in reddit.subreddit('youshouldknow').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    file.write(scored_submissions)
    file.write("\n")
file.write("\n \n \n")
for submission in reddit.subreddit('frugal').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    file.write(scored_submissions)
    file.write("\n")
file.write("\n \n \n")
for submission in reddit.subreddit('soccer').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    file.write(scored_submissions)
    file.write("\n")
file.write("\n \n \n")

for submission in reddit.subreddit('trump').hot(limit=10):
    print(submission.title)
    scored_submissions = print_sentiment_scores(submission.title)
    file.write(scored_submissions)
    file.write("\n")
file.write("\n \n \n")

file.write("This is the Sentiment analysis results of the BOTTOM 10 subreddits using TEXTBLOB\n")

for submission in reddit.subreddit('outoftheloop').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    file.write(final_sentiment)
    outoftheloopTally = outoftheloopTally + sentiment.sentiment.polarity
    file.write("\n")
file.write("OutOfTheLoop\n")
file.write("Computed Value:    ")
file.write(str(outoftheloopTally))
file.write("\n \n \n ")

for submission in reddit.subreddit('youshouldknow').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    file.write(final_sentiment)
    youshouldknowTally = youshouldknowTally + sentiment.sentiment.polarity
    file.write("\n")
file.write("YouShouldKnow\n")
file.write("Computed Value:    ")
file.write(str(youshouldknowTally))
file.write("\n \n \n ")

for submission in reddit.subreddit('frugal').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    file.write(final_sentiment)
    frugalTally = frugalTally + sentiment.sentiment.polarity
    file.write("\n")
file.write("Frugal\n")
file.write("Computed Value:    ")
file.write(str(frugalTally))
file.write("\n \n \n ")

for submission in reddit.subreddit('soccer').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    file.write(final_sentiment)
    soccerTally = soccerTally + sentiment.sentiment.polarity
    file.write("\n")
file.write("Soccer\n")
file.write("Computed Value:    ")
file.write(str(soccerTally))
file.write("\n \n \n ")

for submission in reddit.subreddit('trump').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    file.write(final_sentiment)
    trumpTally = trumpTally + sentiment.sentiment.polarity
    file.write("\n")
file.write("Trump\n")
file.write("Computed Value:    ")
file.write(str(trumpTally))
file.write("\n \n \n ")

for submission in reddit.subreddit('nocontext').hot(limit=10):
    print(submission.title)
    statement = submission.title
    sentiment = TextBlob(statement)
    final_sentiment = str(sentiment.sentiment.polarity)
    file.write(final_sentiment)
    WTFTally = WTFTally + sentiment.sentiment.polarity
    file.write("\n")
file.write("nocontext\n")
file.write("Computed Value:    ")
file.write(str(WTFTally))
file.write("\n \n \n ")

j = open('top.txt', "w")
for submission in reddit.subreddit('iama').hot(limit=10):
    print(submission.title)
    j.write(submission.title)
    file.write("\n")

for submission in reddit.subreddit('funny').hot(limit=10):
    print(submission.title)
    j.write(submission.title)
    file.write("\n")

for submission in reddit.subreddit('todayilearned').hot(limit=10):
    print(submission.title)
    j.write(submission.title)
    file.write("\n")

for submission in reddit.subreddit('science').hot(limit=10):
    print(submission.title)
    j.write(submission.title)
    file.write("\n")

for submission in reddit.subreddit('worldnews').hot(limit=10):
    print(submission.title)
    j.write(submission.title)
    file.write("\n")

k = open('bottom.txt', "w")
for submission in reddit.subreddit('outoftheloop').hot(limit=10):
    print(submission.title)
    k.write(submission.title)
    file.write("\n")

for submission in reddit.subreddit('youshouldknow').hot(limit=10):
    print(submission.title)
    k.write(submission.title)
    file.write("\n")

for submission in reddit.subreddit('frugal').hot(limit=10):
    print(submission.title)
    k.write(submission.title)
    file.write("\n")

for submission in reddit.subreddit('soccer').hot(limit=10):
    print(submission.title)
    k.write(submission.title)
    file.write("\n")

for submission in reddit.subreddit('trump').hot(limit=10):
    print(submission.title)
    k.write(submission.title)
    file.write("\n")
