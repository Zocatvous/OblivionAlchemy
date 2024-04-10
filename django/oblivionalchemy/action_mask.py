
class ActionMask:
	def __init__(self, effect:str, target:str, damage:int, duration:int):
		self.damage = damage
		self.effect = effect
		self.duration = duration
		self.target = target


class AttackMask(ActionMask):
	def __init__():
		self.weapon = ''
