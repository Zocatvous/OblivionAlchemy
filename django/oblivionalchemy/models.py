from django.db import models
# from discordbot.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import json


def default_effects_for_item():
	return {
		"effects":[],
		"elapsed_duration":0
	}


class DiscordUser(models.Model):
	discord_id = models.CharField(max_length=100, unique=True, null=True,)
	character = models.OneToOneField(
		'Character',
		on_delete=models.CASCADE,
		related_name='discord_user',
		default=None,
		null=True
	)

	def __init__(self, discord_id, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.discord_id = discord_id

	def __str__(self):
		return f'<User:{self.discord_id}>'


class InventoryItem(models.Model):
	name = models.CharField(max_length=40)
	weight = models.IntegerField(default = 0)
	hitpoints = models.IntegerField(default = 100)
	is_default = models.BooleanField(default=False)
	effects = models.JSONField(default = default_effects_for_item)
	rarity = models.IntegerField(default=100)

	@property
	def rarity(self):
		return 666


#UPSTREAM MODEL IS STORED AS A FOREIGN KEY!
class InventoryInstance(models.Model):
	character_name = models.OneToOneField('Character', on_delete=models.CASCADE, null=True, related_name="characters")
	items = models.JSONField(default=dict)

	def save(self, *args, **kwargs):
		if not self.pk:
			existing_items = InventoryItem.objects.all()
			self.items = {item.name: {'id':item.id, "quantity":0, "equipped":False,} for item in existing_items}
		super().save(*args, **kwargs)

	def add_item(self, item_id, quantity):
		items = self.items
		items.append({'item_id': item_id, 'quantity': quantity})
		self.items = items
		self.save(update_fields=['items'])

	def get_items(self):
		return [(item['item_id'], item['quantity']) for item in self.items]



class Character(models.Model):
	user = models.OneToOneField(DiscordUser, on_delete=models.CASCADE, null=True, related_name="characters")
	name = models.CharField(max_length=40, null=True)
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
	inventory_instance = models.OneToOneField(InventoryInstance, on_delete=models.CASCADE, related_name="characters", null=True, blank=True)

	def __repr__(self):
		return f'<Character {self.name} HP:{self.max_hitpoints} MP:{self.max_magicka} FP:{self.max_fatigue}>' 

	def __str__(self):
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
		# print('creating={}'.format(self._state.adding))
		creating = self._state.adding
		super().save(*args, **kwargs)  # First save to ensure self has an ID.
		if creating:
			if not hasattr(self, 'inventory_instance'):
				InventoryInstance.objects.create(character_name=self)
				self.save()  # Update self after creating related instances.




