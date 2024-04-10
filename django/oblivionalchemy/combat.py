from typing import List
from .player import Player
from .helper import pretty_string,color_text
from .action_mask import ActionMask

import random


class CombatFactory:
	def __init__(self, *players:List[Player]):
		# self.baddies = pd.read_csv('./resources/csv/baddies.csv')
		self.attack_mask_list=[]
		self.players = players

	def __repr__(self):
		return f"CombatFactory({', '.join(x.character_alias for x in self.players)})"

	def is_any_player_dead(self):
		for player in self.players:
			if player.current_health <= 0:
				return True
		return False 

# I need to create an object or workflow that allows for 
	def combat(self, verbose=False):
		turn_order = sorted(self.players, key=lambda player: player.character.speed, reverse=True)
		combat_continues = True
		while combat_continues and not self.is_any_player_dead():
			for player in turn_order:
				targets = [target for target in turn_order if target != player]
				#this is setup to only target the first target in the list and will need to be refactored for multiway combat
				target=targets[0]
				action_mask = ActionMask(effect='damage_health', target=target , damage=round(random.randint(0,player.character.strength),0), duration=1)

				self.attack(player,target,action_mask)
				target.process_action_masks()

				if verbose:
					print(f"{color_text(player.character_alias,'green')} hit with {color_text(pretty_string(action_mask.effect),'cyan')} for {color_text(action_mask.damage, 'red')} on {color_text(target,'yellow')}")
				#print(f"Status: {target} {player}")
				#print(f"{target.character_alias} has {target.current_health} after {player.character_alias} attack")
				if self.is_any_player_dead()==True:
					print(f'combat over {player.character_alias} wins')
					combat_continues=False
					break
				
				if not combat_continues or self.is_any_player_dead():
					break 


	def run_combat(self, *fighters: str):
		for fighter in fighters:
			character = Player(player_name=fighter)
			print(f'Loaded {character}')

			random_attack_mask = AttackMask(random.randbetween(0,2))
			character = Player(player_name='Baddie')

	def run_random_combat(self):
		pass		

	def attack(self, attacker, target, action_mask:ActionMask, verbose=False):
		if verbose:
			print(f"masking {target.character_alias} with {action_mask.damage}")
		attacker.outgoing_mask_list.append(action_mask)
		target.incoming_mask_list.append(action_mask)


# player1 = Player(name='Test10', character_alias='Clint')
# player2 = Player(name='Test100', character_alias='Natasha')

# combat_factory = CombatFactory(player1,player2)
# combat_factory.combat(verbose=True)
