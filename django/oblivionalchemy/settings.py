import os
import sys

from django.conf import settings
from django.core.management import execute_from_command_line


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

SHELL_PLUS_IMPORTS = [
	('oblivionalchemy.models', ('Character')),
	('oblivionalchemy.oblivion_alchemy', ('AlchemyFactory')),
	('oblivionalchemy.plant', ('PlantFactory')),
	('oblivionalchemy.helper', ('emojimap','pretty_string')),
	('oblivionalchemy.action_mask', ('ActionMask')),
	('oblivionalchemy.player', 'Player')
	('oblivionalchemy.combat', 'CombatFactory')
]

# settings.configure (
# 	DATABASES, INSTALLED_APPS, SHELL_PLUS_IMPORTS
# 	)
# django.setup()

