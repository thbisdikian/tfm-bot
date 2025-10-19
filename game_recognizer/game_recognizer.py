import re
from discord.ext import commands

class GameRecognizer(commands.Cog):
    """Listener that recognizes new games"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if id := self.get_game_id(message):
            await message.channel.send(f"New game detected with ID: {id}")
    
    def get_game_id(self, message):
        """Gets the game ID from the message if it is a game link"""
        game_pattern = r"https://terraforming-mars\.herokuapp\.com/game\?id=([A-Za-z0-9_-]+)"
        match = re.search(game_pattern, message.content)
        if match:
            return match.group(1)
        return None
