from player import Player
from potion import PotionFactory
import random

class AttackMask:
	def __init__(self, damage, target)

class CombatFactory:
	def __init__(self, *characters:Player)
		self.baddies = pd.read_csv('./resources/csv/baddies.csv')
		self.potion_factory= PotionFactory()
		self.attack_mask_list=[]

	def attack(self):
		attack = AttackMask()

	def run_combat(self, *fighters: str):
		for fighter in fighters:
			character = Player(player_name=fighter)
			print(f'Loaded {character}')

			random_attack_mask = AttackMask(random.randbetween(0,2))
			character = Player(player_name='Baddie')


			

