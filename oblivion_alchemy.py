import pandas as pd

import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '.settings')
django.setup()

from plant import PlantFactory
from potion import PotionFactory, PotionInstance
from player import Player
from action_mask import ActionMask
pd.set_option('display.max_rows',500)



def construct_df(path_to_csv):
	ing_df = pd.read_csv(path_to_csv, delimiter='|')
	#process all casing to snake
	for col in ing_df.columns:
		ing_df[col] = ing_df[col].apply(lambda x: str(x).lower().replace(" ", "_"))
	return ing_df

class AlchemyFactory:
	def __init__(self,player:Player):
		#print('- Oblivion Alchemy in Python -')
		self.base_mag_df = construct_df('./resources/csv/effect_base_mag.csv')
		self.plant_factory = PlantFactory()
		# self.potion_factory = Potion
		#lists
		self.duration_only_effects_list = []
		self.magnitude_only_effects_list = []
		self.negative_effects_list = []
		self.positive_effects_list = []
		#constants- may need something else for this to refresh state on things
		self.effective_alchemy_level = player.alchemy+0.4*(player.luck-50)


	def find_common_effects_between_plants(self,df):
		effects = df[['Effect 1', 'Effect 2', 'Effect 3', 'Effect 4']].applymap(lambda x: x.strip().replace('\xa0', '')).values.flatten()
		effect_counts = pd.Series(effects).value_counts()
		common_effects = effect_counts[effect_counts >= 2].index.tolist()
		return common_effects

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
		return self.base_mag_df.loc[self.base_mag_df['effect'] == effect, 'magnitude_only'].iloc[0]

	def check_for_duration_only_effects(self, effects):
		return self.base_mag_df.loc[self.base_mag_df['effect'] == effect, 'duration_only'].iloc[0]

	def get_base_cost_for_effect(self, effect):
		matching_row = self.base_mag_df[self.base_mag_df['effect'] == effect]
		return matching_row['base_cost'].iloc[0]

	def get_polarity_from_effects(self, effects):
		if not isinstance(effects, (list,set)):
			raise ValueError('effects must be a set or a list')
		positive_effect_df = self.base_mag_df[self.base_mag_df['effect'].isin(effects) & (self.base_mag_df['polarity'] == 'positive')]
		value = not positive_effect_df.empty
		return value

#THE ONLY MAGNITUDE ONLY EFFECT IS DISPEL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	#need these sort of "helper functions" to sort out the particulars to get the numbers right	
	def get_instrument_factor(self, effect, instrument):
		duration_only = self.check_for_duration_only_effects(effect)
		magnitude_only = self.check_for_magnitude_only_effects(effect)

		if duration_only:
			if instrument == 'calcinator': return 0.25
			elif instrument == 'alembic': return 2
			elif instrument == 'retort_mag': return 1
			elif instrument == 'retort_dur': return 0.35

		elif magnitude_only:
			if instrument == 'calcinator': return 0.3
			elif instrument == 'alembic': return 2
			elif instrument == 'retort_mag': return 0.5
			elif instrument == 'retort_dur': raise ValueError('this shouldnt happen')

		else:
			print('neither magnitude_only nor duration_only')
			if instrument == 'calcinator': return 0.35
			elif instrument == 'alembic': return 2
			elif instrument == 'retort_mag': return 0.5
			elif instrument == 'retort_dur': return 1


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



#THIS NEEDS TO BE FOR A SINGLE EFFECT NOT MANY!!! each effect magnitude is delivered seperately
# THE DEFUALT CASE WHERE Base_Mag = [ (Effective_Alchemy + MortarPestle_Strength*25)/(Effect_Base_Cost/10 * 4) ] ^ (1/2.28)
# IS what should be happening in most cases. the other cases are for permutations of instrument combinations. 
	def generate_magnitude(self, effect, verbose=False):
		positive_effect = self.get_polarity_from_effects(effect)
		magnitude_only = self.check_for_magnitude_only_effects(effect)
		duration_only = self.check_for_duration_only_effects(effect)

		calcinator = player.calcinator_level if player.calcinator_level is not None else False
		alembic = player.alembic_level if player.alembic_level is not None else False
		pestlemortar = player.pestlemortar_level if player.pestlemortar_level is not None else False
		retort = player.retort_level if player.retort_level is not None else False

		#MASTER EQUATION DEFAULT CASE - Only when using Pestle and Calcinator???
		try:
			base_mag = (self.effective_alchemy + self.get_instrument_strength(player.pestlemortar_level)*25 / (4 * self.get_base_cost_for_effect(effect)/10)) ** (1/2.28)

			calc_fac = self.get_instrument_factor(effect, 'calcinator')
			calc_str = self.get_instrument_strength(player.calcinator_level)

			ret_mag_fac = self.get_instrument_factor(effect, 'retort_mag')
			ret_str = self.get_instrument_strength(player.retort_level)

			alem_fac = self.get_instrument_factor(effect, 'alembic')
			alem_str = self.get_instrument_strength(player.alembic_level)


			if magnitude_only:
				print(f'effect should be dispel:{effect}')
				base_mag = ((effective_alchemy + mortarpestle_strength * 25) / (self.get_base_cost_for_effect(effect) / 10)) ** (1/1.28)
			elif duration_only:
				return 1


			magnitude =  base_mag * (
	    		1 +
	    		calc_fac * calc_str +
	    		ret_mag_fac * ret_str -
	    		alem_fac * alemb_str)

			if verbose:
				print(f'effect {effect}')
				print(f'base_mag:{base_mag}\ncalc_fac{calc_fac}\ncalc_str:{calc_fac}\nret_mag_fac:{ret_mag_fac}\nret_str:{ret_str}\nalem_fac:{alem_fac}\nalem_str:{alem_str}\n')
				print(f'magnitude:{magnitude}')

			return magnitude

		except Exception as e:
			raise Exception(f'Something went wrong calculating effect magnitude because {e}')



	def generate_duration(self, effect):
		positive_effect = self.get_polarity_from_effects(effect)
		magnitude_only = self.check_for_magnitude_only_effects(effect)
		duration_only = self.check_for_duration_only_effects(effect)

		calcinator = player.calcinator_level if player.calcinator_level is not None else False
		alembic = player.alembic_level if player.alembic_level is not None else False
		pestlemortar = player.pestlemortar_level if player.pestlemortar_level is not None else False
		retort = player.retort_level if player.retort_level is not None else False

		try:
			if positive_effect:
				if calcinator and retort:
					print('positive_normal_effect with calc and retort')
					return 1 + 1.4 * self.get_instrument_strength(player.calcinator_level) + self.get_ins_fac() + self.get_instrument_strength(player.retort_level)
				elif (calcinator ^ retort):
					print('positive_normal_effect with one of calc or retort')
					return 1 + 0.35 * self.get_instrument_strength(player.calcinator_level) + self.get_instrument_strength(player.retort_level)
				else:
					print('base case positive_normal_effect with no calc or ret')
					return 4 * self.get_base_cost_for_effect(effect)

			elif magnitude_only:
				if calcinator and retort:
					print('magnitude_only with calc and retort')
					return 1 
				elif (calcinator ^ retort):
					print('magnitude_only with one of calc or retort')
					return 1
				else:
					raise ValueError(f'magnitude_only effect {effect} has no duration')
			elif duration_only:
				if alembic:
					print('duration_only with alembic')
					return (1 + 0.35 * self.get_instrument_strength(player.calcinator_level)) * (1 + 0.35 * self.get_instrument_strength(player.calcinator_level) - 2 * self.get_instrument_strength(player.alembic_level))
				else:
					print('duration_only without an alembic')
					return 1 + 0.25 * self.get_instrument_strength(player.calcinator_level) + 0.35 * self.get_instrument_strength(player.calcinator_level) - 2 * self.get_instrument_strength(player.alembic_level)
			else:
				if alembic:
					if calcinator and retort:
						return self.get_base_cost_for_effect(effect) * (1 + self.get_ins_fac())
				print('negative_normal_effect')
				return 

		except Exception as e:
			raise Exception(f'Something went wrong calculating effect duration because {e}')


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


	def base_mag_for_effect(self,effect_name):
		base_mag = ((self.effective_alchemy_level() + self.gen_ins_fac()*25)/(self.get/10 * 4)) ** (1/2.28)
		return base_mag

	def get_magicka_cost(self):
		return self.effective_alchemy_level + self.calculate_ins_str('pestlemortar_level')*25 

		Magnitude = Base_Mag * (1 + Calc_Fac*Calcinator_Strength + Ret_Mag_Fac*Retort_Strength- Alem_Fac*Alembic_Strength)
		Duration = Base_Dur * (1 + Calc_Fac*Calcinator_Strength + Ret_Dur_Fac*Retort_Strength- Alem_Fac*Alembic_Strength)

	def generate_potion_from_common_effects(self, common_effects):
		for effect in common_effects:
			magicka_cost = self.effective_alchemy_lvl + self.calculate_strength()*25
			magnitude = self.generate_magnitude(effect)
			duration = self.generate_duration(effect)







player=Player(name='Test10')
no_calc_player = Player(calcinator_level=None)
Alchemy = AlchemyFactory(player=player)
plant_df = Alchemy.plant_factory.get_plants('corn','carrot','mandrake_root')
effects = Alchemy.find_common_effects_between_plants(plant_df)
print(f'generate mag for {effects} @ lvl:{player.alchemy} alchemy with\n pestle:{player.pestlemortar_level}\n calc:{player.calcinator_level}\n alembic:{player.alembic_level}\n retort:{player.retort_level}')
for effect in effects:
	input(f'{effect} for {Alchemy.generate_magnitude(effect)}')

# 1_positive_effects = ['resist_paralysis']
# 2_positive_effects = ['resist_fire','resist_frost']
# 3_positive_effects = ['resist_fire','resist_frost','fortify_willpower']
# 4_positive_effects = ['fire_shield','frost_shield','fortify_luck','fortify_magicka']

# duration_only_positive_effects = ['night-eye']
# duration_only_negative_effects = ['paralyze']

# 1_positive_1_neg_effects = ['resist_fire','paralyze']
# 3_positive_1_neg_effects = ['resist_fire','resist_frost','fortify_willpower','fire_damage']


# giant_effects_list = [['resist_paralysis'],
# ['resist_fire','resist_frost'],
# ['resist_fire','resist_frost','fortify_willpower'],
# ['fire_shield','frost_shield','fortify_luck','fortify_magicka'],
# ['resist_fire','paralyze'],
# ['resist_fire','resist_frost','fortify_willpower','fire_damage'],
# ['shock_damage','frost_damage'],
# ['paralyze'],
# ['paralyze','shock_damage']
# ]

# for eff in giant_effects_list:
# 	val = Alchemy.generate_magnitude(eff)

