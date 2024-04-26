


from oblivionalchemy.models import InventoryItem


def create_all_inventory_items():
	InventoryItem.objects.create(name='Stick', )






class Command(BaseCommand):
	help = 'Deletes and recreates the Test InventoryItem data'

	def add_arguments(self, parser):
		parser.add_argument('--truncate', action='store_true')

	def handle(self, *args, **options):
		truncate = options['truncate']
		record_count = InventoryItem.objects.all().count()

		if truncate:
			retries = 1
			while retries >= 0:
				check=input(f"Are you sure you want to delete and recreate character data ({record_count} item records)? (yes/no): ")
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
			record_count = InventoryItem.objects.all().count()
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
			record_count = InventoryItem.objects.all().count()
			self.stdout.write(self.style.SUCCESS('Successfully created character data.({})'.format(record_count)))