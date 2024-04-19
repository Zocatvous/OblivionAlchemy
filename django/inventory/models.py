from django.db import models
from oblivionalchemy.models import Character


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

#UPSTREAM MODEL IS STORED AS A FOREIGN KEY!


