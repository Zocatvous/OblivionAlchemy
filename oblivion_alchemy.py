import pandas as pd
from plant import PlantFactory
from potion import PotionFactory
from player import Player
pd.set_option('display.max_rows',500)



def construct_df(path_to_csv):
	ing_df = pd.read_csv(path_to_csv, delimiter='|')
	#process all casing to snake
	for col in ing_df.columns:
		ing_df[col] = ing_df[col].apply(lambda x: str(x).lower().replace(" ", "_"))
	return ing_df

#TODO we need to roll a "playerobject" into the required inputs for this - lets work on that tonight?
class AlchemyFactory:
	def __init__(self,player:Player):
		#print('- Oblivion Alchemy in Python -')
		self.base_mag_df = construct_df('./effect_base_mag.csv')
		self.plant_factory = PlantFactory()
		# self.potion_factory = Potion
		#lists
		self.duration_only_effects_list = []
		self.magnitude_only_effects_list = []
		self.negative_effects_list = []
		self.positive_effects_list = []
		#constants- may need something else for this to refresh state on things
		self.effective_alchemy_level = player.alchemy_level+0.4*(player.luck_level-50)
		#self.base_mag = ((self.effective_alchemy_level() + self.gen_ins_fac()*25)/(Effect_Base_Cost/10 * 4)) ** (1/2.28)

	def find_common_effects_between_plants(self,df):
		effects = df[['Effect 1', 'Effect 2', 'Effect 3', 'Effect 4']].values.flatten()
		effect_counts = pd.Series(effects).value_counts()
		common_effects = effect_counts[effect_counts >= 2].index.tolist()
		return set(common_effects)

	def retrieve_base_mag_for_effect(self,effect):
		pass

	def get_unique_effects(self):
		ing_df = self.ingredients
		effect_columns = [col for col in ing_df.columns if col != 'Flower Name']
		unique_effects = set()
		for col in effect_columns:
			unique_effects.update(ing_df[col].dropna().unique())
		unique_effects = {effect.strip() for effect in unique_effects if isinstance(effect, str)}
		# pprint.pprint(unique_effects)
		print(type(unique_effects))
		return list(unique_effects)

	def check_for_magnitude_only_effects(self, effects):
		pass
	def check_for_duration_only_effects(self, effects):
		pass

	def get_polarity_from_effects(self, effects):
		if not isinstance(effects, (list,set)):
			raise ValueError('effects must be a set or a list')
		positive_effect_df = self.base_mag_df[self.base_mag_df['effect'].isin(effects) & (self.base_mag_df['polarity'] == 'positive')]
		return not positive_effect_df.empty

	#need these sort of "helper functions" to sort out the particulars to get the numbers right	
	def generate_instrument_factor(self,effect_type,instrument):
		valid_eff = ['normal','duration_only','magnitude_only']
		valid_ins =  ['calcinator','ret_dur_fac','ret_mag_fac', 'alembic']
		if effect_type not in valid_eff:
			raise Exception(f'effect_type must be one of {valid_eff}')
		if ins not in valid_ins:
			raise Exception(f"insturment argument must be in {valid_ins}")
		if effect_type == 'normal' and instrument == 'calc':
			return 0.35
		elif effect_type == 'duration_only' and instrument == 'calcinator':
			return 0.25
		elif effect_type == 'magnitude_only' and instrument == 'calcinator':
			return 0.3
		elif effect_type == 'normal' and instrument == 'ret_dur_fac':
			return 1
		elif effect_type == 'duration_only' and instrument == 'ret_dur_fac':
			return 0.35
		elif effect_type == 'duration_only' and instrument == 'ret_dur_fac':
			raise Exception('Cannot compute Retort Duration Factor for magnitude_only effect_type')
		elif effect_type == ('normal' or 'magnitude_only') and instrument == 'ret_mag_fac':
			return 0.5
		elif effect_type == 'duration_only' and instrument == 'ret_mag_fac':
			raise Exception('Cannot compute Retort Magnitude Factor for duration_only effect_type')
		elif effect_type == 'normal' and instrument == 'alembic':
			return 2
		elif effect_type == 'duration_only' and instrument == 'alembic':
			return 2
		elif effect_type == 'magnitude_only' and instrument == 'alembic':
			#^Always 0 in practice, because the only Magnitude-Only effect is a positive one.
			#really dont get this...
			return 0

	def get_instrument_strength(self,instrument_level):
		if instrument_level == "novice":
			return 0.1
		elif instrument_level == "apprentice":
			return 0.25
		elif instrument_level == "journeyman":
			return 0.5
		elif instrument_level == "expert":
			return 0.75
		elif instrument_level == "master":
			return 1
		else:
			raise Exception(f"Incorrect Insturment Level Given you asked for {thing} must be one of the class instance arguments")


	def generate_magnitude(self, common_effects):
		if not common_effects:
			raise ValueError('common_effects cannot be an empty list')
		print(common_effects)

		positive_effect = self.get_polarity_from_effects(common_effects)
		magnitude_only = self.check_for_magnitude_only_effects(common_effects)
		duration_only = self.check_for_duration_only_effects(common_effects)

		calcinator = player.calcinator_level if player.calcinator_level is not None else False
		alembic = player.alembic_level if player.alembic_level is not None else False
		pestlemortar = player.pestlemortar_level if player.pestlemortar_level is not None else False
		retort = player.retort_level if player.retort_level is not None else False
		try:
			if positive_effect is False:
				if alembic is False:
					print('alembic is FALSE and its a NEGATIVE EFFECT')
					print('1 + 0.35*Calcinator_Strength')
					return 1 + 0.35*self.get_instrument_strength(player.calcinator_level)
				else:
					print('alembic is TRUE and its a NEGATIVE EFFECT')
					print('(1 + 0.35*Calcinator_Strength)*(1 + 0.35*Calcinator_Strength - 2*Alembic_Strength)')
					return (1 + 0.35*self.get_instrument_strength(player.calcinator_level)) * (1 + 0.35*self.get_instrument_strength(player.calcinator_level) - 2 * self.get_instrument_strength(player.alembic_level)) 
			else: 
				if duration_only:
					print('its a POSITIVE effect thats DURATION_ONLY')
					return 1
				elif magnitude_only:
					if (calcinator and retort):
						print('its a Positve EFFECT with Magnitude ONLY and you have CALC and RETORT')
						print('1 + 0.15*Calcinator_Strength*Retort_Strength')
						return 1 + 0.15 * self.get_instrument_strength(player.calcinator_level) * self.get_instrument_strength(player)
					else (calcinator ^ retort):
						print('its a POSITIVE EFFECT and you only have one of Calc or Retort')
						print('1 + 0.35*Calcinator_Strength + 0.5*Retort_Strength')
						return 1 + 0.35 * self.get_instrument_strength(player.calcinator_level) * 0.5 * self.get_instrument_strength(player.retort_level)
				else:
					if (calcinator and retort):
						print('its a POSITIVE EFFECT and you have a Calc AND Retort')
						print('1 + 1.4*Calcinator_Strength + 0.5*Retort_Strength')
						return 1 + 1.4 * self.get_instrument_strength(player.calcinator_level) + 0.5 * self.get_instrument_strength(player.retort_level)
					elif (calcinator ^ retort):
						print('its a POSITIVE EFFECT and you have a Calc/Retort')
						print('1 + 0.35*Calcinator_Strength + 0.5*Retort_Strength')
						return 1 + 0.35 * self.get_instrument_strength(player.calcinator_level) + 0.5 * self.get_instrument_strength(player.retort_level)
		except Exception as e:
			raise Exception(f'Something went wrong calculating effect magnitude because {e}')


	def generate_duration(self):
		positive_effect = self.get_polarity_from_effects(common_effects)
		magnitude_only = self.check_for_magnitude_only_effects(common_effects)
		duration_only = self.check_for_duration_only_effects(common_effects)


	def calculate_alch_strength(alchemy_level):
		if 1 <= alchemy_level <= 24:
			return 0.1
		elif 25 <= alchemy_level <= 49:
			return 0.25
		elif 50 <= alchemy_level <= 74:
			return 0.5
		elif 75 <= alchemy_level <= 99:
			return 0.75
		elif alchemy_level == 100:
			return 1
		else:
			raise Exception(f"Incorrect Alchemy Level Given: {alchemy_level}. Must be a number between 1 and 100.")


	def calc_base_mag_for_effect(self,eff_name):
		base_mag = ((self.effective_alchemy_level() + self.gen_ins_fac()*25)/(self.get/10 * 4)) ** (1/2.28)
		return base_mag

	def get_magicka_cost(self):
		return self.effective_alchemy_level + self.calculate_ins_str('pestlemortar_level')*25 

		Magnitude = Base_Mag * (1 + Calc_Fac*Calcinator_Strength + Ret_Mag_Fac*Retort_Strength- Alem_Fac*Alembic_Strength)
		Duration = Base_Dur * (1 + Calc_Fac*Calcinator_Strength + Ret_Dur_Fac*Retort_Strength- Alem_Fac*Alembic_Strength)

	def generate_potion_from_common_effects(self, common_effects):
		magicka_cost = self.effective_alchemy_lvl + self.calculate_strength()*25
		magnitude = Base_Mag * (1 + Calc_Fac)


		#any potion with even a single positive effect will make a potion
		#any potion with exclusively negative effects will produce a poison.




#x = AlchemyFactory().get_effects_from_ingredients(['Sweetcake','Apple'])
player=Player()
Alchemy = AlchemyFactory(player=player)
plant_df = Alchemy.plant_factory.get_plants('corn','carrot','mandrake_root')
effects = Alchemy.find_common_effects_between_plants(plant_df)

1_positive_effects = ['resist_paralysis']
2_positive_effects = ['resist_fire','resist_frost']
3_positive_effects = ['resist_fire','resist_frost','fortify_willpower']
4_positive_effects = ['fire_shield','frost_shield','fortify_luck','fortify_magicka']

duration_only_positive_effects = ['night-eye']
duration_only_negative_effects = ['paralyze']

1_positive_1_neg_effects = ['resist_fire','paralyze']
3_positive_1_neg_effects = ['resist_fire','resist_frost','fortify_willpower','fire_damage']




Alchemy.generate_magnitude(effects)