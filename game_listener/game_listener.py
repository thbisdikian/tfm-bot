import logging
import re
from discord.ext import commands
from data_manager import sql_manager
from data_manager.models.games import Games


class GameListener(commands.Cog):
    """Listener that recognizes new games"""

    def __init__(self, bot):
        self.bot = bot
        self.sql_manager = sql_manager.get_instance()
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if id := self.get_game_id(message):
            await message.channel.send(f"New game detected with ID: {id}")
            logging.info(f"[GameListener.on_message]: New game detected with ID: {id}, adding to db")
            self.sql_manager.add_game(
                Games(
                    id=id, 
                    created=message.created_at,
                    done=False
                ))
    
    def get_game_id(self, message):
        """Gets the game ID from the message if it is a game link"""
        game_pattern = r"https://terraforming-mars\.herokuapp\.com/game\?id=([A-Za-z0-9]+)"
        match = re.search(game_pattern, message.content)
        if match:
            return match.group(1)
        return None
