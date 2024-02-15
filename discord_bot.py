import discord
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv
import os



from plant import PlantFactory


load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')


# try:
intents = Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.guild_messages = True  # Enable guild messages

bot = commands.Bot(command_prefix='!', intents=intents)
#client = discord.Client(intents=intents)


# @client.event
# async def on_ready():
# 	try:
# 		print(f'{client.user.name} Online')
# 	except Exception as e:
# 		print(f'ISSUE: {e}')

# @client.event
# async def on_message(message):
# 	# Prevent bot from responding to its own messages
# 	if message.author == client.user:
# 		return

# 	# A simple command that responds when someone types "hello"
# 	if message.content.lower() == 'hello':
# 		await message.channel.send(f'Hello! {client.user}')

@bot.command(aliases=['hello'])
async def greet(ctx):
	await ctx.send("Hello!")


@bot.command(aliases=['pick'])
async def pick_random_plant(ctx):
	# if message.content == 'pick':
	try:
		plant_factory = PlantFactory()
		plt = plant_factory.get_random_plant()
		plt_name = plt[0]

		embed = discord.Embed(
			title=f'{plt.name}',
			description='Need to put text here about the flower desciption - maybe more if you roll well',  # Description or the main text content
			color=discord.Color.blue()  # Color of the side strip of the embed
		)
		embed.set_image(url='https://en.uesp.net/wiki/File:OB-icon-ingredient-Arrowroot.png')
		embed.add_field(name='Effect 1', value='Restore Strength', inline=False)
		embed.add_field(name='Effect 2', value='Water Breathing', inline=False)
		embed.add_field(name='Effect 3', value='Silence', inline=False)
		embed.add_field(name='Effect 4', value='Light', inline=False)
		await ctx.send(embed=embed)
	except Exception as e:
		print(e)
		pass
		#await message.channel.send(embed=embed)

# client.run(bot_token)
bot.run(bot_token)




