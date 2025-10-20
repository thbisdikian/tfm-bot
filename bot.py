import asyncio
import discord
import os
import logging
from dotenv import load_dotenv
from discord.ext import commands

from game_listener import GameListener
import bot_config


intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

async def main():
    load_dotenv()
    config = bot_config.get_instance()

    handlers = []
    
    if config.file_logging_enabled:
        handlers.append(logging.FileHandler(filename=config.log_file_path, encoding='utf-8', mode='w'))
    if config.stream_logging_enabled:
        handlers.append(logging.StreamHandler())

    logging.basicConfig(
        level=logging._nameToLevel.get(config.log_level, logging.INFO),
        handlers=[*handlers],
        format='%(asctime)s:%(levelname)s:%(name)s: %(message)s'
    )
    await bot.add_cog(GameListener(bot))
    token = os.getenv('TFM_BOT_DISCORD_TOKEN')
    await bot.start(token)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
