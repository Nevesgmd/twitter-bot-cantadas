import random
import tweepy
from time import sleep

api_key = 'YOUR API KEY HERE'
api_secret = 'YOUR API SECRET HERE'
access_token = 'YOUR ACCESS TOKEN HERE'
access_secret = 'YOUR ACCESS SECRET HERE'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def read_last_seen_id():
    with open('last_seen_id.txt', 'r') as f:
        return int(f.read().strip())


def store_last_seen_id(last_id):
    with open('last_seen_id.txt', 'w') as f:
        f.write(str(last_id))


# insert the pick-up lines here
pickup_lines = ['1', '2', '3']


while True:
    user_id = read_last_seen_id()
    user_mentions = api.mentions_timeline(user_id, tweet_mode='extended')
    try:
        store_last_seen_id(user_mentions[len(user_mentions) - 1].id)
    except IndexError:
        pass
    for mention in user_mentions:
        while True:
            print(f"Found: {mention.full_text} {mention.id}\n")
            try:
                api.update_status(f"@{mention.user.screen_name} "
                                  f"{pickup_lines[random.randint(0, len(pickup_lines) - 1)]}",
                                  mention.id)
            except tweepy.TweepError:
                print("Error. Trying again...")
                continue
            else:
                print("Replied.\n")
                break
        sleep(10)
    sleep(20)
