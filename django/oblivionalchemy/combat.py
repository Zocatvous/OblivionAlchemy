from typing import List

from potion import PotionFactory
from player import Player
from action_mask import ActionMask
import random

class CombatFactory:
	def __init__(self, *characters:List[Player]):
		self.baddies = pd.read_csv('./resources/csv/baddies.csv')
		self.attack_mask_list=[]
		self.characters = characters



# I need to create an object or workflow that allows for 
	def combat(self):
		turn_order = sorted(characters, key=lambda player: player.speed)
		player2 = turn_order[1]
		targets = [target for target in turn_order if target != player]
		for player in turn_order:
			#this is setup to only target the first target in the list and will need to be refactored for multiway combat
			self.attack(player, ActionMask(effect='damage_health', target=targets[0] , damage=player.strength, duration=0))
			player.process_action_masks()


	def run_combat(self, *fighters: str):
		for fighter in fighters:
			character = Player(player_name=fighter)
			print(f'Loaded {character}')

			random_attack_mask = AttackMask(random.randbetween(0,2))
			character = Player(player_name='Baddie')

	def run_random_combat(self):
		pass
		

	def attack(self, attacker, target, action_mask:ActionMask):
		attacker.action_mask,append(action_mask)






player1 = Player(name='BOB_Player_1')
player2 = Player(name='ORC1')

combat_factory = CombatFactory(player1,player2)
