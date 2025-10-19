from discord.ext import commands

class HelloCog(commands.Cog):
    """A simple hello world cog."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello_command(self, ctx):
        """Responds with a greeting message."""
        await ctx.send('Cog says hello from command!')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Cog says hello from listener!')