from insta_bot import *

# constants
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
URL = "https://www.instagram.com/?hl=en"
INSTAGRAM_USERNAME = "YOUR INSTAGRAM USERNAME"
INSTAGRAM_PASS = "YOUR INSTRGRAM PASSWORD"
TARGATE_ACCOUNT_LINK = "INSTAGRM ACCOUNT LINK WHOSE FOLLOWERS YOU WANT TO TARGATE"
# "https://www.instagram.com/chefsteps/"

# creating object form class
insta_obj = InstaFollowerBot(CHROME_DRIVER_PATH, URL)
insta_obj.login(INSTAGRAM_USERNAME, INSTAGRAM_PASS)
insta_obj.find_followers(TARGATE_ACCOUNT_LINK)
insta_obj.follow()
