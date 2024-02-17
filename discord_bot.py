import discord
from discord.ext import commands
from discord import Intents, utils
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


emojimap = {
'cure':utils.get(ctx.guild.emojis, name='cure'),
'fortify_magicka':utils.get(ctx.guild.emojis, name='fortify_magicka'),
'fortify_intelligence':utils.get(ctx.guild.emojis, name='fortify'),
'fortify_strength':utils.get(ctx.guild.emojis, name='fortify'),
'fortify_agility':utils.get(ctx.guild.emojis, name='fortify'),
'fortify_health':utils.get(ctx.guild.emojis, name='fortify'),
'fortify_luck':utils.get(ctx.guild.emojis, name='fortify'),
'fortify_personality':utils.get(ctx.guild.emojis, name='fortify'),
'fortify_fatigue':utils.get(ctx.guild.emojis, name='fortify'),
'fortify_endurance':utils.get(ctx.guild.emojis, name='fortify'),
'burden':utils.get(ctx.guild.emojis, name='burden'),
'frost_damage':utils.get(ctx.guild.emojis, name='frost'),
'shock_damage':utils.get(ctx.guild.emojis, name='shock'),
'fire_damage':utils.get(ctx.guild.emojis, name='fire'),
'resist_frost':utils.get(ctx.guild.emojis, name='resist_element'),
'resist_fire':utils.get(ctx.guild.emojis, name='resist_element'),
'resist_shock':utils.get(ctx.guild.emojis, name='resist_element'),
'frost_shield':utils.get(ctx.guild.emojis, name='frost_shield'),
'shock_shield':utils.get(ctx.guild.emojis, name='shock_shield'),
'fire_shield':utils.get(ctx.guild.emojis, name='fire_shield'),
'silence':utils.get(ctx.guild.emojis, name='silence'),
'reflect_damage':utils.get(ctx.guild.emojis, name='reflect_damage'),
'reflect_spell':utils.get(ctx.guild.emojis, name='reflect_spell'),
'invisibility':utils.get(ctx.guild.emojis, name='invisibility'),
'restore_fatigue':utils.get(ctx.guild.emojis, name='restore'),
'restore_magicka':utils.get(ctx.guild.emojis, name='restore'),
'restore_health':utils.get(ctx.guild.emojis, name='restore'),
'restore_strength':utils.get(ctx.guild.emojis, name='restore'),
}

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
	# if message.content == 'pick':
	# try
	emojis = ctx.guild.emojis
	plant_factory = PlantFactory()
	plt = plant_factory.get_random_plant()
	print(f'plant0:{plt[0]} plant1:{plt[1]} plant2:{plt[2]} plant3:{plt[3]} plant4:{plt[4]}')
	plt_name = plt[0]
	print(utils.get(ctx.guild.emojis, name='cure'))
	plt_effect_1 = f'{emojimap[plt[1]]} {plt[1]}'
	plt_effect_2 = f'{utils.get(ctx.guild.emojis, name=plt[2])} {plt[2]}'
	plt_effect_3 = f'{utils.get(ctx.guild.emojis, name=plt[3])} {plt[3]}'
	plt_effect_4 = f'{utils.get(ctx.guild.emojis, name=plt[4])} {plt[4]}'

	embed = discord.Embed(
		title=f'{plt_name}',
		description='Need to put text here about the flower desciption - maybe more if you roll well',  # Description or the main text content
		color=discord.Color.green()  # Color of the side strip of the embed
	)
	embed.set_image(url='https://en.uesp.net/wiki/File:OB-icon-ingredient-Arrowroot.png')
	# embed.add_field(name=plt_effect_1, value='Restore Strength', inline=False)
	# embed.add_field(name=plt_effect_2, value='Water Breathing', inline=False)
	# embed.add_field(name=plt_effect_3, value='Silence', inline=False)
	# embed.add_field(name=plt_effect_4, value='Light', inline=False)

	# embed.add_field(name=plt_effect_1, inline=False)
	# embed.add_field(name=plt_effect_2, inline=False)
	# embed.add_field(name=plt_effect_3, inline=False)
	# embed.add_field(name=plt_effect_4, inline=False)


	effects_list = [f"{plt_effect_1}",f"{plt_effect_2}",f"{plt_effect_3}",	f"{plt_effect_4}"]
	effects_str = '\n'.join(effects_list)
	embed.add_field(name="Effects", value=effects_str, inline=False)
	await ctx.send(embed=embed)
	# except Exception as e:
	# 	print(e)
	# 	pass
		#await message.channel.send(embed=embed)

# client.run(bot_token)
bot.run(bot_token)




