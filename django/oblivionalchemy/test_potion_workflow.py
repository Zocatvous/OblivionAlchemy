player=Player(name='Test50')
# no_calc_player = Player(calcinator_level=None)
Alchemy = AlchemyFactory(player=player)
plant_factory = PlantFactory()
plant_df = plant_factory.get_plants('corn', 'mandrake_root', 'carrot')
effects = Alchemy.get_common_effects_between_plants(plant_df)
list_of_magnitudes = [f'{effect} {Alchemy.generate_magnitude(effect,verbose=True)} points' for effect in effects]
print(list_of_magnitudes)


#NEED TO MANUALLY GO THROUGH A CALCULATION FOR A BASIC CHARACTER



import math

BASE_COST = 2
level = 10
for RET_LEVEL in [('Novice', 0.1), ('Apprentice',0.25), ('Journeyman',0.5),('Expert', 0.75),('Master',1)]:	
	for CALC_LEVEL in [('Novice', 0.1), ('Apprentice',0.25), ('Journeyman',0.5),('Expert', 0.75),('Master',1)]:	
		for PM_LEVEL in [('Novice', 0.1), ('Apprentice',0.25), ('Journeyman',0.5),('Expert', 0.75),('Master',1)]:
			for level in range(10,100):
				for luck in range(50,100):
					EFFECTIVE_ALCHEMY = level + 0.4 * (luck - 50)
					base_mag = round(math.pow(((EFFECTIVE_ALCHEMY + PM_LEVEL[1] * 25) / (4 * BASE_COST / 10)), (1/2.28)))
					FINAL_MAGNITUDE = round(base_mag*(1 +	1.4 * CALC_LEVEL[1] + 0.5 * RET_LEVEL[1]))
					print(f'(RET:{RET_LEVEL[0]}) (CALC:{CALC_LEVEL[0]}) (PM:{PM_LEVEL[0]}) ({luck})Luck ({level})Alchemy({level}) Restore Fatigue {FINAL_MAGNITUDE} points')

FINAL_MAGNITUDE = base_mag * (
				1 +
				1.4 * CALC_LEVEL +
				0.5 * RET_LEVEL -
				alem_fac * alem_str)




print(f'generate mag for {effects} @ lvl:{player.alchemy} alchemy with\n pestle:{player.pestlemortar_level}\n calc:{player.calcinator_level}\n alembic:{player.alembic_level}\n retort:{player.retort_level}')

for effect in effects:
	print(f'generate mag for {effects} @ lvl:{player.character.alchemy} alchemy with\n pestle:{player.pestlemortar_level}\n calc:{player.calcinator_level}\n alembic:{player.alembic_level}\n retort:{player.retort_level}')
	input(f'{effect} for {Alchemy.generate_magnitude(effect)}')