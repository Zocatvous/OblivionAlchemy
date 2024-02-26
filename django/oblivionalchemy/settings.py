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
	('oblivionalchemy.models', ('Character'))
]