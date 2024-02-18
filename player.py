import uuid


class Player:
	def __init__(self, *player_name=f'TEST_PLAYER_{uuid.uuid4()}',
		alembic_level='novice',
		calcinator_level='novice',
		pestlemortar_level='novice',
		retort_level='novice',
		luck_level=30,
		alchemy_level=1,
		survival_level=1):

		self.alembic_level=alembic_level
		self.calcinator_level=calcinator_level
		self.pestlemortar_level=pestlemortar_level
		self.retort_level=retort_level
		self.alchemy_level=alchemy_level
		self.luck_level=luck_level
		self.suvival=survival_level

		self.health_level = None
		self.active_effects = None

	@property
	def fatigue(self):
		return self._fatigue

	@property
	def health(self):
		return self._health
	
	@property
	def magicka(self):
		return self._magicka
