
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

 SHELL_PLUS_PRE_IMPORTS = [('oblivionalchemy.character','character'),('inventory.models','')]
 SHELL_PLUS = 'ipython'