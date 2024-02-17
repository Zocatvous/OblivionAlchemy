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
'cure_poison':'cure',
'cure_disease':'cure'
'cure_paralysis':'cure'
'fortify_magicka':'fortify_magicka',
'fortify_intelligence':'fortify',
'fortify_strength':'fortify',
'fortify_speed':'fortify'
'fortify_agility':'fortify',
'fortify_health':'fortify',
'fortify_speed':'fortify',
'fortify_luck':'fortify',
'fortify_personality':'fortify',
'fortify_fatigue':'fortify',
'fortify_endurance':'fortify',
'burden':'burden',
'frost_damage':'frost',
'shock_damage':'shock',
'fire_damage':'fire',
'shield':'shield',
'resist_disease':'resist_element',
'resist_frost':'resist_element',
'resist_fire':'resist_element',
'resist_shock':'resist_element',
'frost_shield':'frost_shield',
'shock_shield':'shock_shield',
'fire_shield':'fire_shield',
'silence':'silence',
'reflect_damage':'reflect_damage',
'reflect_spell':'reflect_spell',
'invisibility':'invisibility',
'restore_fatigue':'restore',
'restore_magicka':'restore',
'restore_health':'restore',
'restore_strength':'restore',
'restore_willpower':'restore',
'restore_intelligence':'restore',
'restore_agility':'restore'
'restore_endurance':'restore'
'restore_luck':'restore',
'burden':'burden',
'water_breathing':'water_breathing',
'water_walking':'water_walking',
'silence':'silence',
'night-eye':'night_eye',
'damage_agility':'damage_attribute',
'damage_endurance':'damage_attribute',
'damage_fatigue':'damage_attribute',
'damage_strength':'damage_attribute',
'damage_magicka':'damage_attribute',
'damage_willpower':'damage_attribute',
'damage_health':'damage_attribute',
'damage_luck':'damage_attribute',
'damage_intelligence':'damage_attribute',
'damage_personality':'damage_attribute',
'damage_speed':'damage_attribute',
'detect_life':'detect_life',
'chameleon':'chameleon',
'paralyze':'paralyze',
'light':'light',
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
	plt_effect_1 = f'{utils.get(ctx.guild.emojis, name=emoji_map[plt[1]])} {plt[1]}'
	plt_effect_2 = f'{utils.get(ctx.guild.emojis, name=emoji_map[plt[2]])} {plt[2]}'
	plt_effect_3 = f'{utils.get(ctx.guild.emojis, name=emoji_map[plt[3]])} {plt[3]}'
	plt_effect_4 = f'{utils.get(ctx.guild.emojis, name=emoji_map[plt[4]])} {plt[4]}'

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




