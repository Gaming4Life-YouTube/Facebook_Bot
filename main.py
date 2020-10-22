"""
Facebook bot main
"""

from facebook_bot import facebook_bot
import json

config_json = "/Users/derekcalabro/Desktop/Python_Projects/Facebook_Bot/config.json"

if __name__ == "__main__":
    with open(config_json) as file:
        config = json.load(file)

    driver = config["driver"]
    url = config["url"]
    username = config["username"]
    password = config["password"]

    fb = facebook_bot(driver, url, username, password)
    fb.post_on_wall("I am a bot.")