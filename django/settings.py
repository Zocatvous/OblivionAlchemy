import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line


MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',  # Should be before AuthenticationMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


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
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',  # This is crucial for Django's type system
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Add your custom apps here
	'inventory',
	'discordbot',
	'oblivionalchemy',
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