from django.core.management.base import BaseCommand
from oblivionalchemy.models import Character
from oblivionalchemy.utils.create_test_characters import create_test_characters
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
	help = 'Tests Combat'

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


