import discord
from discord.ext import commands
from discord import Intents

from dotenv import load_dotenv
import os

intents = Intents.default()
intents.messages = True
intents.guilds = True


# Load environment variables from .env file
load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')

# Create a bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Event listener for when the bot has switched from offline to online.
@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
	# Prevent bot from responding to its own messages
	if message.author == bot.user:
		return

	# A simple command that responds when someone types "hello"
	if message.content.lower() == 'hello':
		await message.channel.send('Hello!')


# A simple command that responds with 'Hello!' when someone types '!hello'
# @bot.command()
# async def hello(ctx):
#	 await ctx.send('Hello!')

# Replace 'YOUR_BOT_TOKEN_HERE' with your bot's token
bot.run(bot_token)



