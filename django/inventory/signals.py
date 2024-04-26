from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from oblivionalchemy.models import Character
from .models import InventoryInstance

@receiver(post_save, sender=apps.get_model('oblivionalchemy', 'Character'))
def create_inventory_instance(sender, instance, created, **kwargs):
    if created:
        InventoryInstance.objects.create(character_name=instance)