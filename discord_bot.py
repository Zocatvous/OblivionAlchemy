import discord
from discord.ext import commands
from discord import Intents, utils, ButtonStyle, Color, Embed
from discord.ui import Button, View
from dotenv import load_dotenv
import os
from plant import PlantFactory
from helper import emojimap, pretty_string

load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')

# try:
intents = Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.guild_messages = True  # Enable guild messages

bot = commands.Bot(command_prefix='!', intents=intents)

class PickPlantButton(View):
	def __init__(self, plant_factory):
		super().__init__(timeout=None)
		self.plant_factory = PlantFactory()

	@discord.ui.button(label="Pick Again!", style=ButtonStyle.green, custom_id="pick_plant")
	async def pick_plant(self, interaction: discord.Interaction, button: Button):
		plt = self.plant_factory.get_random_plant()
		plt_name = pretty_string(plt[0])
		plt_effects = [f'{discord.utils.get(interaction.guild.emojis, name=emojimap[plt[i]])} {pretty_string(plt[i])}' for i in range(1, 4)]
		effects_str = '\n'.join(plt_effects)
		print("IT WOOOOOOOOOOOOOOOOOOORKED")
		
		embed = Embed(title=plt_name, description='Need to put text here about the flower desciption - maybe more if you roll well', color=Color.green())
		embed.add_field(name="Effects", value=effects_str, inline=False)
		
		await ctx.send(content="Here's your random plant:", embed=embed, view=self)


@bot.command(aliases=['emojis'])
async def list_emojis(ctx):
	emojis = ctx.guild.emojis  # Gets a list of emojis from the guild where the command was called
	for emoji in emojis:
		await ctx.send(f"{emoji} -> {emoji.id}")  # Sends each emoji's representation and its ID

@bot.command(aliases=['hello'])
async def greet(ctx):
	await ctx.send("Hello!")

@bot.command(aliases=['pick'])
async def pick_random_plant(ctx):
	plant_factory = PlantFactory()
	player = None
	plt = plant_factory.get_random_plant()
	print(f'{plt[0]} {plt[1]} {plt[2]} {plt[3]} {plt[4]}')
	plt_name = pretty_string(plt[0])
	plt_effect_1 = f'{utils.get(ctx.guild.emojis, name=emojimap[plt[1]])} {pretty_string(plt[1])}'
	plt_effect_2 = f'{utils.get(ctx.guild.emojis, name=emojimap[plt[2]])} {pretty_string(plt[2])}'
	plt_effect_3 = f'{utils.get(ctx.guild.emojis, name=emojimap[plt[3]])} {pretty_string(plt[3])}'
	plt_effect_4 = f'{utils.get(ctx.guild.emojis, name=emojimap[plt[4]])} {pretty_string(plt[4])}'

	embed = discord.Embed(
		title=f'{plt_name}',
		description='Need to put text here about the flower desciption - maybe more if you roll well',  # Description or the main text content
		color=discord.Color.green()  # Color of the side strip of the embed
	)
	embed.set_image(url='https://en.uesp.net/wiki/File:OB-icon-ingredient-Arrowroot.png')

	effects_list = [f"{plt_effect_1}",f"{plt_effect_2}",f"{plt_effect_3}",f"{plt_effect_4}"]
	effects_str = '\n'.join(effects_list)
	embed.add_field(name="Effects", value=effects_str, inline=False)



	button=discord.ui.Button(label="Pick Again")
	view = discord.ui.View()
	view.add_item(button)


	await ctx.send(embed=embed, view=view)
	# except Exception as e:
	# 	print(e)
	# 	pass
		#await message.channel.send(embed=embed)

# client.run(bot_token)
bot.run(bot_token)




