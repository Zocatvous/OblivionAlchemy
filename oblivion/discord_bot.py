import discord
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')


# try:
intents = Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.guild_messages = True  # Enable guild messages


client = discord.Client(intents=intents)


@client.event
async def on_ready():
	try:
		print(f'Logged in as {client.user.name} checkidy check')
	except Exception as e:
		print(f'ISSUE: {e}')

@client.event
async def on_message(message):
	# Prevent bot from responding to its own messages
	if message.author == client.user:
		return

	# A simple command that responds when someone types "hello"
	if message.content.lower() == 'hello':
		await message.channel.send(f'Hello! {client.user}')


client.run(bot_token)




