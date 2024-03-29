import uuid
import os
import sys

from models import Character

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
# print(sys.path)

class Player:
	def __init__(self, name='Test10',
		alembic_level='novice',
		calcinator_level='novice',
		pestlemortar_level='novice',
		retort_level='novice'):

		self.character = Character(name=name)
		self.name=name
		self.alembic_level=alembic_level
		self.calcinator_level=calcinator_level
		self.pestlemortar_level=pestlemortar_level
		self.retort_level=retort_level

		self.active_effects = [None]

		self.hitpoints_used = 0
		self.fatigue_used = 0
		self.magicka_used = 0

	@property
	def current_fatigue(self):
		return self.character.max_fatigue - self.fatigue_used

	@property
	def current_health(self):
		return self.character.max_hitpoints - self.hitpoints_used
	
	@property
	def current_magicka(self):
		return self.character.max_magicka - self.magicka_used

	def __repr__(self):
		return f"<({self.name} HP:{self.current_health}/{self.character.max_hitpoints} MP:{self.current_magicka}/{self.character.max_magicka} FP:{self.current_fatigue}/{self.character.max_fatigue})>"

	def get_available_strikes_with_weapon(self):
		pass

	@property
	def max_carry_weight(self):
		return self._max_carry_weighT


	def drink_potion(*potions:str):
		potion_active_effects = []

	def _process_mask(*action_masks:list):
		for ac_mask in action_masks:
			#check_for_damage
			if ac_mask.damage:
				print(f'pow. {ac_mask.damage}')

	def generate_weapon_rating(self):
		pass

