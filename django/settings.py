import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DATABASES = {
			'default': {
						'ENGINE': 'django.db.backends.sqlite3',
						'NAME': 'mydatabase',
									}
			}

INSTALLED_APPS = [
'django_extensions',
'oblivionalchemy',
]



DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'mydatabase',
	}
}

INSTALLED_APPS = [
	'inventory',
	'oblivionalchemy',
	'django_extensions'
 ]

SHELL_PLUS_IMPORTS = [
('oblivionalchemy.models', ('Character')),
('oblivionalchemy.oblivion_alchemy', ('AlchemyFactory')),
('oblivionalchemy.plant', ('PlantFactory')),
('oblivionalchemy.helper', ('emojimap','pretty_string')),
('oblivionalchemy.action_mask', ('ActionMask')),
('oblivionalchemy.player', 'Player'),
('oblivionalchemy.combat', 'CombatFactory'),
# ('inventory.models',''),
 ]

 #SHELL_PLUS = 'ipython'