from bot import Bot
from pyrogram import utils

# Ensure this modification is actually required
utils.MIN_CHANNEL_ID = -1009147483647

if __name__ == "__main__":
    Bot().run()
