from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class User(models.Model):
	discord_id = models.CharField(max_length=100, unique=True, null=False, blank=True)
	character = models.OneToOneField(
		'oblivionalchemy.Character',
		on_delete=models.CASCADE,
		related_name='discord_user'
	)

	def __str__(self):
		return f'<User:{self.discord_id} {self.username}>'


