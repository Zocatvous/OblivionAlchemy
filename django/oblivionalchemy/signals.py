from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from discordbot.models import DiscordUser
from .models import InventoryInstance, DiscordUser, Character


# @receiver(post_save, sender=apps.get_model('oblivionalchemy', 'Character'))
# def create_inventory_instance(sender, instance, created, **kwargs):
# 	if created:
# 		InventoryInstance.objects.create(character_name=instance)

# @reciever(post_save, sender=DiscordUser)
# def create_character_instance(sender, instance, created, **kwargs):
# 	if created:
# 		InventoryInstance.objects.create(user=instance)


# @receiver(post_save, sender=DiscordUser)
# def create_default_character(sender, instance, name="DefaultSignalName_{}".format(uuid.uuid1()), created:bool, **kwargs):
# 	if created:
# 		print('Signaling Char Creation for DiscordUser {instance}')
# 		name="DefaultSignalName_{}".format(uuid.uuid1())
# 		character = Character.objects.create(user=instance, name=name)
# 		instance.character = character
# 		instance.save()
