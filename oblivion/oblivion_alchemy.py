import pandas as pd
import pprint
from plant import PlantFactory
pd.set_option('display.max_rows',500)



def construct_df(path_to_csv):
	ing_df = pd.read_csv(path_to_csv)
	#process all casing to snake
	for col in ing_df.columns:
		ing_df[col] = ing_df[col].apply(lambda x: str(x).lower().replace(" ", "_"))
	return ing_df


class AlchemyFactory:
	def __init__(self, alembic_level='novice', calcinator_level='novice',pestlemortar_level='novice', retort_level='novice', luck_level=30, alchemy_level=1):
		print('- Oblivion Alchemy in Python -')
		# self.al = 1
		# self.ingredients = construct_df('./processed_flower_effects.csv')
		self.base_mag_df = construct_df('./effect_base_mag.csv')
		self.plant_factory = PlantFactory()
		#lists
		self.duration_only_effects_list = []
		self.magnitude_only_effects_list = []
		self.negative_effects_list = []
		self.positive_effects_list = []
		#constants- may need something else for this to refresh state on things
		self.effective_alchemy_level = alchemy_level+0.4*(luck_level-50)
		#self.base_mag = ((self.effective_alchemy_level() + self.gen_ins_fac()*25)/(Effect_Base_Cost/10 * 4)) ** (1/2.28)

	def find_common_effects_between_plants(self,df):
		effects = df[['Effect 1', 'Effect 2', 'Effect 3', 'Effect 4']].values.flatten()
		effect_counts = pd.Series(effects).value_counts()
		common_effects = effect_counts[effect_counts >= 2].index.tolist()
		return set(common_effects)

	def ingest_plants(self,plants:PlantFactory):
		pass

	def retrieve_base_mag_for_effect(self,effect):
		pass

	def get_unique_effects(self):
		ing_df = self.ingredients
		effect_columns = [col for col in ing_df.columns if col != 'Flower Name']
		unique_effects = set()
		for col in effect_columns:
			unique_effects.update(ing_df[col].dropna().unique())
		unique_effects = {effect.strip() for effect in unique_effects if isinstance(effect, str)}
		pprint.pprint(unique_effects)
		print(type(unique_effects))
		return list(unique_effects)

	def get_positive_or_negative_effect(self):
		return 'Nothing Here yet!'

	def get_effects_from_ingredient(self, ingredient_name):
		pass

	#need these sort of "helper functions" to sort out the particulars to get the numbers right	
	def gen_ins_fac(self,effect_type,ins):
		valid_eff = ['normal','duration_only','magnitude_only']
		valid_ins =  ['calc','ret_dur_fac','ret_mag_fac', 'alem']
		if effect_type not in valid_eff:
			raise Exception(f'effect_type must be one of {valid_eff}')
		if ins not in valid_ins:
			raise Exception(f"ins argument must be in {valid_ins}")
		if effect_type == 'normal' and ins == 'calc':
			return 0.35
		elif effect_type == 'duration_only' and ins == 'calc':
			return 0.25
		elif effect_type == 'magnitude_only' and ins == 'calc':
			return 0.3
		elif effect_type == 'normal' and ins == 'ret_dur_fac':
			return 1
		elif effect_type == 'duration_only' and ins == 'ret_dur_fac':
			return 0.35
		elif effect_type == 'duration_only' and ins == 'ret_dur_fac':
			raise Exception('Cannot compute Retort Duration Factor for magnitude_only effect_type')
		elif effect_type == ('normal' or 'magnitude_only') and ins == 'ret_mag_fac':
			return 0.5
		elif effect_type == 'duration_only' and ins == 'ret_mag_fac':
			raise Exception('Cannot compute Retort Magnitude Factor for duration_only effect_type')
		elif effect_type == 'normal' and ins == 'alem':
			return 2
		elif effect_type == 'duration_only' and ins == 'alem':
			return 2
		elif effect_type == 'magnitude_only' and ins == 'alem':
			#^Always 0 in practice, because the only Magnitude-Only effect is a positive one.
			#really dont get this...
			return 0

	def gen_magnitude(self,effect):
		effect_polarity = self.get_positive_or_negative_effect(effect)
		Base_Mag = 
		if effect_polarity == 'negative':
			Magnitude = Base_Mag * (1 + Calc_Fac*Calcinator_Strength + Ret_Mag_Fac*Retort_Strength - Alem_Fac*Alembic_Strength)
		else:
			Magnitude = 


	def get_duration(self):
		effect_polarity = self.get_positive_or_negative_effect()

	def calculate_instrument_str(self,ins_lvl):
		if ins_lvl == "novice":
			return 0.1
		elif ins_lvl == "apprentice":
			return 0.25
		elif ins_lvl == "journeyman":
			return 0.5
		elif ins_lvl == "expert":
			return 0.75
		elif ins_lvl == "master":
			return 1
		else:
			raise Exception(f"Incorrect Insturment Level Given you asked for {thing} must be one of the class instance arguments")

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

	def generate_potion(self):
		magicka_cost = self.effective_alchemy_lvl + self.calculate_strength()*25
		magnitude = Base_Mag * (1 + Calc_Fac)

		#any potion with even a single positive effect will make a potion
		#any potion with exclusively negative effects will produce a poison.




#x = AlchemyFactory().get_effects_from_ingredients(['Sweetcake','Apple'])
Alchemy = AlchemyFactory()
plant_df = Alchemy.plant_factory.get_plants('corn','carrot','mandrake_root')
print(Alchemy.find_common_effects_between_plants(plant_df))