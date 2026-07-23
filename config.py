# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

# Login feature, if you want then True , if you don't want then False
LOGIN_SYSTEM = bool(os.environ.get('LOGIN_SYSTEM', True)) # True or False

if LOGIN_SYSTEM == False:
    # if login system is False then fill your tg account session below 
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQHo8UQAoi6B_L3vvqLFw35KxFAqnpOSk8uyWsGu9VFGIHUfa65NxUxnc_a9P0hIm4BA4s0RWTpdZvXXEmFw143tbcFOZYa9-NMFl_PCvLPemi2qgfsHDMeqbrqHec18WYxlPdDKO0CFqrnijpevbWY6Eb0N1k90s0sgfE7XBwPIQSembgxvLu0WkDYAtrp-OMTLJC8EtacBOGdZs16kK7ZYqEIFO5BcWPm9K7nQcvG7daMjepSvzz22MmI9OXO_ybtVyWiE4x-2RJ4n8iwXFLE4waUVvuDgt-Z1ZNfRYwJ-LWF_5SP-tlvnPLmQ-UxpElUFfT_wGZ_ZPCwm5ymbM3_0zzvwtQAAAAIDNhVWAA")
else:
    STRING_SESSION = None

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8980439596:AAHwA5C75UR7ccr0kg9D_RiSIyAQubPDgPI")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "33092002"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2a700ced620e33cc4bc5eb932a5d3bb5")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8643810646"))

# Your Channel Id In Which Bot Upload Downloaded Video/File/Message etc.
# And Make Your Bot Admin In this channel with full rights.
# if you don't want to upload in channel then leave it blank don't fill anything.
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# Increase time as much as possible to avoid floodwait, spamming and tg account ban issues.
WAITING_TIME = int(os.environ.get("WAITING_TIME", "10")) # time in seconds

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
