from django.core.management.base import BaseCommand

#from oblivionalchemy.utils.create_test_characters import create_test_characters
from django.db import connection, transaction
from django.conf import settings

from oblivionalchemy.models import Character, InventoryInstance, DiscordUser
from django.db.models import IntegerField
import uuid

def create_test_characters(start=10, limit=200, increment=10, truncate=False):
	if truncate:
		print('Truncating character database...')
		with transaction.atomic():
			InventoryInstance.objects.all().delete()
			DiscordUser.objects.all().delete()
			Character.objects.all().delete()


	print(f'Creating records {start} through {limit}..')

	for i in range(start, limit+1, increment):
		name = f'Test{i}'
		field_values = {}
		for field in Character._meta.get_fields():
			if not field.auto_created and not field.is_relation and field.name != 'id':
				if isinstance(field, IntegerField):
					field_values[field.name] = i
				elif field.name == 'name':
					field_values[field.name] = f'{name}'
				elif field.name == 'user':
					field_values[field.name] = 'placeholder_{}'.format(uuid.uuid1())

		character = Character.objects.create(**field_values)
		discord_user = DiscordUser.objects.create(discord_id='TestUser{}'.format(i), character=character)
		character.user = discord_user
		inventory = InventoryInstance.objects.create(character_name=character)
		character.inventory_instance = inventory
		character.save()

		print('Creating record {}\r'.format(i), end='\r')

		# character = Character.objects.create(user=discord_user, **field_values)


class Command(BaseCommand):
	help = 'Deletes and recreates the Test Character data'

	def add_arguments(self, parser):
		parser.add_argument('--start', type=int, default=10)
		parser.add_argument('--limit', type=int, default=200)
		parser.add_argument('--increment', type=int, default=10)
		parser.add_argument('--truncate', action='store_true')

	def handle(self, *args, **options):
		start = options['start']
		limit = options['limit']
		increment = options['increment']
		truncate = options['truncate']
		record_count = Character.objects.all().count()

		if truncate:
			retries = 1
			while retries >= 0:
				check=input(f"Are you sure you want to delete and recreate character data ({record_count} records)? (yes/no): ")
				if check == "yes":
					db_engine = settings.DATABASES['default']['ENGINE']
					if 'sqlite3' in db_engine:
						with connection.cursor() as cursor:
							cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'oblivionalchemy_character';")
						self.stdout.write(self.style.SUCCESS('Successfully reset SQLite index'))
					create_test_characters(start=start, limit=limit, increment=increment, truncate=truncate)
					return
				elif check == 'no':
					self.stdout.write(self.style.SUCCESS('Operation Cancelled'))
					return
				else:
					self.stdout.write(self.style.ERROR('Invalid input. Please type "yes" or "no"'))
					retries -= 1
			record_count = Character.objects.all().count()
			self.stdout.write(self.style.SUCCESS('Successfully truncated and created character data. ({})'.format(record_count)))

		else:
			retries = 1
			check = input("Are you sure you want create character data? (yes/no): ")
			if check =='yes':
				create_test_characters(start=start, limit=limit, increment=increment, truncate=truncate)
				return
			elif check == 'no':
				self.stdout.write(self.style.SUCCESS('Operation Cancelled'))
				return
			else:
				self.stdout.write(self.style.ERROR('Invalid input. Please type "yes" or "no"'))
				retries -= 1
			record_count = Character.objects.all().count()
			self.stdout.write(self.style.SUCCESS('Successfully created character data.({})'.format(record_count)))


