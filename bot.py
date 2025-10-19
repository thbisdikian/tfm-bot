import asyncio
import discord
import os
import logging
from dotenv import load_dotenv
from discord.ext import commands
from hello_cog import HelloCog
from game_recognizer import GameRecognizer


intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('!hello'):
#         await message.channel.send('Hello! How can I assist you today?')

async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')],
        format='%(asctime)s:%(levelname)s:%(name)s: %(message)s'
    )
    await bot.add_cog(HelloCog(bot))
    await bot.add_cog(GameRecognizer(bot))
    token = os.getenv('TFM_BOT_DISCORD_TOKEN')
    await bot.start(token)

asyncio.run(main())
