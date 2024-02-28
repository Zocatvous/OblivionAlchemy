player=Player(name='Test50')
# no_calc_player = Player(calcinator_level=None)
Alchemy = AlchemyFactory(player=player)
plant_factory = PlantFactory()
plant_df = plant_factory.get_plants('corn', 'mandrake_root', 'carrot')
effects = Alchemy.get_common_effects_between_plants(plant_df)
list_of_magnitudes = [f'{effect} {Alchemy.generate_magnitude(effect,verbose=True)} points' for effect in effects]
print(list_of_magnitudes)


print(f'generate mag for {effects} @ lvl:{player.alchemy} alchemy with\n pestle:{player.pestlemortar_level}\n calc:{player.calcinator_level}\n alembic:{player.alembic_level}\n retort:{player.retort_level}')

for effect in effects:
	print(f'generate mag for {effects} @ lvl:{player.character.alchemy} alchemy with\n pestle:{player.pestlemortar_level}\n calc:{player.calcinator_level}\n alembic:{player.alembic_level}\n retort:{player.retort_level}')
	input(f'{effect} for {Alchemy.generate_magnitude(effect)}')