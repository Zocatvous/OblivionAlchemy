from typing import Union, List
import pandas as pd

def construct_df(path_to_csv):
	ing_df = pd.read_csv(path_to_csv)
	#process all casing to snake
	for col in ing_df.columns:
		ing_df[col] = ing_df[col].apply(lambda x: str(x).lower().replace(" ", "_"))
	return ing_df

class PlantFactory:
	def __init__(self):
		self.plant_df =construct_df('./processed_flower_effects.csv')

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

# x = PlantFactory()
# print(x.get_plants('carrot','corn','mandrake_root'))