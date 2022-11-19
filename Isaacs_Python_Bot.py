
# First things first I downloaded and installed the package tweepy. Additionally, I got all my API keys from Developer Twitter and assigned variables to them in a seperate script called "keys"

# I then import required packages


import tweepy
import keys

# Use the OAuthHandler instance method for API authentication and setting a access token

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)

# Create a method to write tweet and allow for image upload using the PNG's image path 

def tweet(api: tweepy.API, message: str, image_path = None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted Successfully!')

# Create the API, write the tweet, and specify the image path for the png you're uploading 

if __name__ == '__main__':
    api = api()
    tweet(api, 'Time is money. This is why Isaac tweets using his python bot', '/Users/IsaacAbreham/Downloads/money.png')

# Too see this tweet follow @i8productions on twitter
