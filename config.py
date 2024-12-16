from operator import add
import os
import logging


# import dotenv
# dotenv.load_dotenv()



from logging.handlers import RotatingFileHandler

#force user to join your backup channel leave 0 if you don't need.
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002398866124"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002123546604"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002496140741"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002252421276"))


#bot stats
BOT_STATS_TEXT = os.environ.get("BOTS_STATS_TEXT","<b>BOT UPTIME </b>\n{uptime}")
#send custom message when user interact with bot
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "ꜱᴏʀʀʏ ʙᴜᴛ ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴀᴅᴍɪɴꜱ ꜰʀᴏᴍ <b>ɪɴꜰᴏʜᴜʙ ɴᴇᴛᴡᴏʀᴋꜱ</b> ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ.\n\nᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴀᴅᴍɪɴꜱ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍʏ ꜰʀɪᴇɴᴅ - @infohubsupport_robot")

#your bot token here from https://telegram.me/BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7463305761:AAFb3tDY_cxcM75jiDO3Rn91lEvRA6mQNfo") 
#your api id from https://my.telegram.org/apps
APP_ID = int(os.environ.get("APP_ID", "21145186"))
#your api hash from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH", "daa53f4216112ad22b8a8f6299936a46")
#your channel_id from https://t.me/MissRose_bot by forwarding dummy message to rose and applying command `/id` in reply to that message
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002465123057"))
#your id of telegram can be found by https://t.me/MissRose_bot with '/id' command
OWNER_ID = int(os.environ.get("OWNER_ID", "6011680723"))
#port set to default 8080
PORT = os.environ.get("PORT", "6666")
#your database url mongodb only You can use mongo atlas free cloud database
DB_URL = os.environ.get("DB_URL", "mongodb+srv://infohubstore06:CUXzlOmJvWITtrxn@gamingthree.i5ogs.mongodb.net/?retryWrites=true&w=majority")
#your database name
DB_NAME = os.environ.get("DB_NAME", "gamingthree")

#for creating telegram thread for bot to improve performance of the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#your start default command message.
START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ ᴛʜᴇʀᴇ {mention}!!🌚\n\nɪ ᴀᴍ ᴅᴇꜱɪɢɴᴇᴅ ᴛᴏ ꜱʜᴀʀᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋꜱ!! 🪄\n\nɪ ᴡᴏʀᴋ ᴡɪᴛʜɪɴ ɪɴꜰᴏʜᴜʙ ɴᴇᴛᴡᴏʀᴋꜱ ᴏɴʟʏ ᴀɴᴅ ʏᴏᴜ ᴀʀᴇ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴜꜱᴇ ᴍᴇ! 🎀")
#your telegram tag without @
OWNER_TAG = os.environ.get("OWNER_TAG", "the_universal_being")
#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "600"))


#Shortner (token system) 
"""
some token verification sites
https://dashboard.shareus.io/
"""

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "TRUE") == "TRUE" else False 
# only shareus service known rightnow rest you can test on your own
SHORTLINK_API_URL = os.environ.get("SHORTLINK_API_URL", "instantlinks.co")
# SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "beb3b795a226177f3af7c937a2f01d5d7d4f4cf0")
#use this key if not working ☠️ (jokin!!)
SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "068bfe93b5ef479dcaed34b6f879049c438932c8")
#add your custom time in secs for shortlink expiration.
# 24hr = 86400
# 12hr = 43200
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "43200")) # Add time in seconds
#put TRUE if you want shortner in every link generated by the bot.
U_S_E_P = True if (True if os.environ.get('U_S_E_P', "TRUE") == "TRUE" else False) and (USE_SHORTLINK) else False
#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID","https://t.me/infohub_updates/34")





#Payment to remove the token system
#put TRUE if you want this feature
USE_PAYMENT = True if (True if os.environ.get("USE_PAYMENT", "False") == "TRUE" else False) and (USE_SHORTLINK) else False
#UPI ID
UPI_ID = os.environ.get("UPI_ID", "rajsom8877@okaxis")
#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://envs.sh/wLE.jpg")
#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/{OWNER_TAG}")
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "20 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "84 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "135 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "250 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "500 rs")



#force message for joining the channel
FORCE_MSG = os.environ.get("FORCE_MSG", "ʜᴇʟʟᴏ ᴛʜᴇʀᴇ {mention}!!👋\n\n<b>ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴇꜱ, ʏᴏᴜ ᴀʀᴇ ʀᴇQᴜᴇꜱᴛᴇᴅ ᴛᴏ ꜱᴜᴘᴘᴏʀᴛ ᴜꜱ ʙʏ ᴊᴏɪɴɪɴɢ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ɢʀᴏᴜᴘꜱ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ:</b>")
#custom caption 
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ᴘʀᴇꜱᴇɴᴛᴇᴅ ʙʏ - @Bookslibraryofficial\n\n• ꜱᴜʙꜱᴄʀɪʙᴇ ᴏᴜʀ ʏᴏᴜᴛᴜʙᴇ - youtube.com/@pagesandvoices</b>")
#protected content so that no files can be sent from the bot to anyone. recommended False
# TRUE for yes FALSE if no
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "FALSE") == "TRUE" else False
#used if you dont need buttons on database channel.
# True for yes False if no
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "TRUE") == "TRUE" else False
#you can add admin inside the bot(bug right now will fix later)

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6011680723 5178714818 6792991359 1173488851 5524805517 5749718252 7085687198").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")




#no need to add anything from now on

ADMINS.append(OWNER_ID)


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
