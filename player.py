import uuid
# import pandas as pd

class Player:
	def __init__(self, name='Test',
		alembic_level='novice',
		calcinator_level='novice',
		pestlemortar_level='novice',
		retort_level='novice',
		luck_level=30,
		alchemy_level=1,
		survival_level=1):
		self.name=name
		self.alembic_level=alembic_level
		self.calcinator_level=calcinator_level
		self.pestlemortar_level=pestlemortar_level
		self.retort_level=retort_level
		self.alchemy_level=alchemy_level
		self.luck_level=luck_level
		self.suvival=survival_level
		#self.attributes = pd.read_csv('./resources/csv/weapons.csv', delimiter='|')

		self.health_level = None
		self.active_effects = [None]

	def __repr__(self):
		return f"<({self.name})>"

	def get_available_strikes_with_weapon(self):
		pass

	@property
	def fatigue(self):
		return self._fatigue

	@property
	def health(self):
		return self._health
	
	@property
	def magicka(self):
		return self._magicka

	def drink_potion(*potions:str):
		potion_active_effects = []


	def generate_weapon_rating(self):
		pass

