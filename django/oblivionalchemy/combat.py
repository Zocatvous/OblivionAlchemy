from typing import List
from .player import Player
from .helper import pretty_string
from .action_mask import ActionMask
import random

class CombatFactory:
	def __init__(self, *players:List[Player]):
		# self.baddies = pd.read_csv('./resources/csv/baddies.csv')
		self.attack_mask_list=[]
		self.players = players

	def __repr__(self):
		return f"CombatFactory({', '.join(x.character_alias for x in self.players)})"

	def one_player_alive(self):
		for player in self.players:
			if player.current_health <= 0:
				return True
		return False

# I need to create an object or workflow that allows for 
	def combat(self, verbose=False):
		turn_order = sorted(self.players, key=lambda player: player.character.speed, reverse=True)
		print(turn_order)
		while self.one_player_alive():
			for player in turn_order:
				targets = [target for target in turn_order if target != player]
				#this is setup to only target the first target in the list and will need to be refactored for multiway combat
				target=targets[0]
				action_mask = ActionMask(effect='damage_health', target=target , damage=player.character.strength, duration=1)
				self.attack(player,target,action_mask)
				player.process_action_masks()
				if verbose:
					print(f'{player.name} {pretty_string(action_mask.effect)} for {action_mask.damage} on {targets[0]}')


	def run_combat(self, *fighters: str):
		for fighter in fighters:
			character = Player(player_name=fighter)
			print(f'Loaded {character}')

			random_attack_mask = AttackMask(random.randbetween(0,2))
			character = Player(player_name='Baddie')

	def run_random_combat(self):
		pass
		

	def attack(self, attacker, target, action_mask:ActionMask):
		attacker.mask_list.append(action_mask)

player1 = Player(name='Test10', character_alias='Clint')
player2 = Player(name='Test100', character_alias='Natasha')


combat_factory = CombatFactory(player1,player2)
combat_factory.combat(verbose=True)
