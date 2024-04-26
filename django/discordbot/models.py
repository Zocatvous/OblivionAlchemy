from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from oblivionalchemy.models import Character
import uuid

class DiscordUser(models.Model):
	discord_id = models.CharField(max_length=100, unique=True, null=False,)
	character = models.OneToOneField(
		'oblivionalchemy.Character',
		on_delete=models.CASCADE,
		related_name='discord_user',
		default=None
	)

	def __init__(self, discord_id, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.discord_id = discord_id

	def __str__(self):
		return f'<User:{self.discord_id}>'


@receiver(post_save, sender=DiscordUser)
def create_default_character(sender, instance, created, **kwargs):
    if created:
        name = "DefaultSignalName_{}".format(uuid.uuid4())
        from .models import Character  # Import here to avoid circular imports
        character = Character.objects.create(user=instance, name=name)
        instance.character = character
        instance.save()

	# def save(self, *args, **kwargs):
	# 	if not self.character_id:
	# 		new_character = Character.objects.create(name='Default_DiscordSignalName_{}'.format(uuid.uuid1()))
	# 		self.character = new_character
	# 	super(DiscordUser, self).save(*args, **kwargs)

