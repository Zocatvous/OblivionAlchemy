from django.db import models

class Character(models.Model):
	name = models.CharField(max_length=40)  
	strength = models.IntegerField(default=10)
	endurance = models.IntegerField(default=10)
	agility = models.IntegerField(default=10)
	speed = models.IntegerField(default=10)
	willpower = models.IntegerField(default=10)
	intelligence = models.IntegerField(default=10)
	personality = models.IntegerField(default=10)
	luck = models.IntegerField(default=10)
	alchemy = models.IntegerField(default=10)
	survival = models.IntegerField(default=10)
	blade = models.IntegerField(default=10)
	marksman = models.IntegerField(default=10)

	def __repr__(self):
		return f'<Character {self.name} HP:{self.max_hitpoints} MP:{self.max_magicka} FP:{self.max_fatigue}>' 

	@property
	def max_hitpoints(self):
		return 2 * self.endurance

	@property
	def max_magicka(self):
		return 2 * self.intelligence

	@property
	def max_fatigue(self):
		return self.strength + self.endurance + self.agility + self.willpower


	

