from typing import Union, List
import pandas as pd
import random

def construct_df(path_to_csv):
	ing_df = pd.read_csv(path_to_csv)
	#process all casing to snake
	for col in ing_df.columns:
		ing_df[col] = ing_df[col].apply(lambda x: str(x).lower().replace(" ", "_"))
	return ing_df

class PlantFactory:
	def __init__(self):
		self.plant_df =construct_df('./resources/csv/processed_flower_effects.csv')

	def _convert_to_snake_case(self):
		for column in self.plant_df.columns:
			self.plant_df[column] = self.plant_df[column].str.lower().str.replace(' ', '_').str.replace(r'(?<!^)(?=[A-Z])', '_', regex=True)
		self.plant_df.to_csv('./processed_flower_effects.csv', index=False)

	def _pretty_string(self, plant_string):
		return plant_string.replace('_', ' ').title()

	def get_plants(self, *plant_names: str):
		plant_names_list = list(plant_names)  

		if len(plant_names_list) == 1 and isinstance(plant_names_list[0], str):
			result_df = self.plant_df[self.plant_df['Flower Name'] == plant_names_list[0]]
			if result_df.empty:
				raise NameError(f'No plant named ({plant_names_list[0]})')
		else:
			result_df = pd.DataFrame(columns=self.plant_df.columns)
			for name in plant_names_list:
				pltdf = self.plant_df[self.plant_df['Flower Name'] == name]
				if pltdf.empty:
					raise NameError(f'No plant named ({name})')
				result_df = pd.concat([result_df, pltdf])
		return result_df

	def get_random_plant(self):
		plant=self.plant_df.sample(n=1).iloc[0]
		pretty_name = self.pretty_string(plant[0])
		for col in plant.index:
			plant[col] = self._pretty_string(str(plant[col]))
		return plant

	
# print(x.get_random_plant())
# print(x.get_plants('carrot','corn','mandrake_root'))