from django.db import models

class InventoryItem(models.Model):
	name = models.Charfield(max_length=40)
	weight = models.IntegerField(default = 0)
	hitpoints = models.IntegerField(default = 1)
	effects_obj = models.JSONField()
