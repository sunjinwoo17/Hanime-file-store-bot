from bot import Bot
import pyrogram.utils

# Set the minimum channel ID
pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

# Run the bot
if __name__ == "__main__":
    Bot().run()
