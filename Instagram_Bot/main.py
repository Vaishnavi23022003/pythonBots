from insta_bot import InstaFollower

LOGIN_ID="-=============----"
LOGIN_PASS="==================="
SIMILAR_ACC="avengers"

bot=InstaFollower(LOGIN_ID,LOGIN_PASS,SIMILAR_ACC)
bot.login()
bot.find_followers()
bot.follow()
