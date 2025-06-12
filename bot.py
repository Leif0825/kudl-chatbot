import os
import discord
from discord.ext import commands

TOKEN = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

if __name__ == '__main__':
    if not TOKEN:
        raise ValueError('DISCORD_TOKEN environment variable not set.')
    bot.run(TOKEN)
