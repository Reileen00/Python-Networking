import tweepy

all_keys=open('twitterkeys','r').read().splitlines()
api_key=all_keys[0]
api_key_secret=all_keys[1]
access_token=all_keys[2]
access_token_secret=all_keys[3]

authenticator=tweepy.OAuthHandler(api_key,api_key_secret)
authenticator.set_access_token(access_token,access_token_secret)

api=tweepy.API(authenticator,wait_on_rate_limit=True)

api.create_friendship('florianedov')
api.update_status("I am currently going fkin insane aah!!!!!")
api.update_profile(description="")
user=api.get_user("Sheep")
for follower in user.followers():
  print(f"{follower.name} follows {user.name}")

tweets_home=api.home_timeline(count=10)
for tweet in tweets_home:
  if tweet.author.name!="Sheep":
    if not tweet.favorited:
      api.create_favorite(tweet.id)

tweet_user=api.user_timeline(user_id=user.id)
for tweet in tweets_user:
  if not tweet.favorited:
    api.create_favorite(tweet.id)

tweets=tweepy.Cursor(api.search, q="brains",lang="en").items(10)
print([tweet.text for tweet in tweets])
