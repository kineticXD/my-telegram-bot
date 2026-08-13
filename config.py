# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

# Login feature, if you want then True , if you don't want then False
LOGIN_SYSTEM = bool(os.environ.get('LOGIN_SYSTEM', True)) # True or False

if LOGIN_SYSTEM == False:
    # if login system is False then fill your tg account session below 
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQHo8UQATZ0pOYxnxpxHFvbSreFiwQ2tqZu0hEcBIP8QBqt2p5aJHEqeugxeMg0UfRWLcFWknST9CpZgtGL78VgiNnwGMzIwCrOfiKAqgKmCQKegEFJAhdZuMiuYVlcXNWuHyEDw6F1YzEpQHXhFLzDeEkTlc-FTjkeDK-oNOxACcq4qc6Xo1MJ8PBHE44gg-XN_71_slwFUkZsfvD4xhmXkySFySZcNmhvuSNcXTWYRo09RrB-8xIelqlJYNerMOo_4OWzbRxlC_MMSC81n8WlKcMtEZS-1erwrF_2nUHK9Wz6kCVaf0CdU1tfNPsT8eQwZKOuZEqnkOScl241Z2scuUvk2IAAAAAHWPr39AA")
else:
    STRING_SESSION = None

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8787813177:AAFZjXICQamDgcTTo71O1SsGffCP9EGwvzY")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "16227253"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d203da78c17fc21f866f2f302a62218b")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8643810646"))

# Your Channel Id In Which Bot Upload Downloaded Video/File/Message etc.
# And Make Your Bot Admin In this channel with full rights.
# if you don't want to upload in channel then leave it blank don't fill anything.
CHANNEL_ID = os.environ.get("CHANNEL_ID", "7889403389")

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://MRISLIVE:MRISLIVE@cluster0.oetvyih.mongodb.net/vjsavecontentbot?retryWrites=true&w=majority") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# Increase time as much as possible to avoid floodwait, spamming and tg account ban issues.
WAITING_TIME = int(os.environ.get("WAITING_TIME", "10")) # time in seconds

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
