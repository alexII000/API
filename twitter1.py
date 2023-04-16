import tweepy
import keys 

client = tweepy.Client(bearer_token=keys.bearer_token)

# response = client.get_user(username='elonmusk')

# print(response)

response=client.get_users_followers(id=44196397)

a, b, c, d = response

for x in a:
    print(x)

query = 'ADHD at my jhob -is:retweet -has:media'

response = client.search_recent_tweets(query=query, max_results=100)
print(response)