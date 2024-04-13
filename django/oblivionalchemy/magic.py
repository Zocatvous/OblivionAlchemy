

from .player import Player

#produces magical action masks for a specific character, handles whether or not the action mask is 
#sent into a target or another target, The MagicFactory will be how any given SpellObject produces its 
#magical effects and potentially how they are mapped to a character

#maybe lets have this be the way that you add spells

class SpellFactory:
	def __init__(self, player:Player):
		self.player = player
		

class MagickaFactory:
	def __init__(self, player:Player)
		self.name = 'asdf'