from django.db import models
from discordbot.models import User
import json

def default_inventory():
	return json.dumps({
	"equipped":[],
	"stored":[],
})


class Character(models.Model):
	user = models.ForeignKey('discordbot.User', on_delete=models.CASCADE, null=True, related_name="characters")
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
	inventory_instance = models.JSONField(default=default_inventory)

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

	def save(self, *args, **kwargs):
		is_new = self._state.adding
		super().save(*args, **kwargs)
		if is_new:
			InventoryInstance.objects.create(character_name=self)


	

