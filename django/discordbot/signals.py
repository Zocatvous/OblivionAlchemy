from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DiscordUser
from oblivionalchemy.models import Character
import uuid


@receiver(post_save, sender=DiscordUser)
def create_default_character(sender, instance, name="DefaultSignalName_{}".format(uuid.uuid1()), created:bool, **kwargs):
	if created:
		print('Signaling Char Creation for DiscordUser {instance}')
		name="DefaultSignalName_{}".format(uuid.uuid1())
		character = Character.objects.create(user=instance, name=name)
		instance.character = character
		instance.save()
