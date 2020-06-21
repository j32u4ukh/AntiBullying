import json

import tweepy
from tweepy import OAuthHandler  # 處理帳號密碼相關問題

from Xu3.config import Config

config_path = r"D:\Programing\AntiOnlineBullying.txt"
with open(config_path, "r") as f:
    content = f.read()
    # dict_keys(['app', 'app_key', 'app_secret', 'oauth_token', 'oauth_secret'])
    config = Config(json.loads(content))
    # print(config)

oauth = OAuthHandler(consumer_key=config.app_key,
                     consumer_secret=config.app_secret)
oauth.set_access_token(key=config.oauth_token,
                       secret=config.oauth_secret)

bot = tweepy.API(oauth)

# 發推文
bot.update_status("Hello  world, 僕はロボットじゃないよ。")
print("Tweet successed.")
