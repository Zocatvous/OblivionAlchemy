from django.db import models
# from oblivionalchemy.models import Character
from django.apps import apps
from django.db.models.signals import post_save
from django.dispatch import receiver

def default_effects_for_item():
	return {
	"effects":[],
	"elapsed_duration":0
}

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
	character_name = models.OneToOneField('oblivionalchemy.Character', on_delete=models.CASCADE, null=True, related_name="character")
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

# @receiver(post_save, sender=apps.get_model('oblivionalchemy', 'Character'))
# def create_inventory_instance(sender, instance, created, **kwargs):
# 	if created:
# 		InventoryInstance.objects.create(character_name=instance)