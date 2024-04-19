from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from oblivionalchemy.models import Character

@receiver(post_save, sender=User)
def create_default_character(sender, instance, created:bool, **kwargs):
	if created:
		Character.objects.create(user=instance, name="Default Name")
		# Set other default values as necessary
