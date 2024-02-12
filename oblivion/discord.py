import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# Event listener for when the bot has switched from offline to online.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# A simple command that responds with 'Hello!' when someone types '!hello'
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Replace 'YOUR_BOT_TOKEN_HERE' with your bot's token
bot.run(bot_token)



