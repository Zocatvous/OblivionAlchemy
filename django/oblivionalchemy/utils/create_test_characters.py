from oblivionalchemy.models import Character
from inventory.models import InventoryInstance
from django.db.models import IntegerField

def create_test_characters(start=10, limit=200, increment=10, truncate=False):
    if truncate:
        print('Truncating character database...')
        Character.objects.all().delete()

    print(f'Creating records {start} through {limit}..')

    for i in range(start, limit+1, increment):
        field_values = {}
        for field in Character._meta.get_fields():
            if not field.auto_created and not field.is_relation:
                if isinstance(field, IntegerField):
                    field_values[field.name] = i
                elif field.name == 'name':
                    field_values[field.name] = f'Test{i}'
        print('Creating record {}\r'.format(i), end='\r')
        Character.objects.create(**field_values)

