from Bot import InternetSpeedTwitterBot

PROMISSED_UP=140
PROMISSED_DOWN=40

bot=InternetSpeedTwitterBot()
(up,down)=bot.get_internet_speed()

if down<PROMISSED_DOWN or up<PROMISSED_UP:
    bot.tweet_at_provider(PROMISSED_UP,PROMISSED_DOWN)