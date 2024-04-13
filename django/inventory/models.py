from django.db import models
from oblivionalchemy.models import Character


class InventoryItem(models.Model):
	name = models.CharField(max_length=40)
	weight = models.IntegerField(default = 0)
	hitpoints = models.IntegerField(default = 100)
	is_default = models.BooleanField(default=False)
	effects_obj = models.JSONField()

#UPSTREAM MODEL IS STORED AS A FOREIGN KEY!
class InventoryInstance(models.Model):
	character_name = models.OneToOneField('oblivionalchemy.Character', on_delete=models.CASCADE)
	items = models.ManyToManyField('InventoryItem', blank=True)  # Assuming 'InventoryItem' is defined elsewhere

	def __str__(self):
		return f"<{self.character.name}'s Inventory>"

