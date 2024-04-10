from django.core.management.base import BaseCommand
from oblivionalchemy.models import Character
from oblivionalchemy.utils.create_test_characters import create_test_characters
from django.db import connection
from django.conf import settings

from django.core.management.base import BaseCommand
# Import your Player and CombatFactory classes
from oblivionalchemy.player import Player
from oblivionalchemy.combat import CombatFactory

class Command(BaseCommand):
    help = 'Runs a combat simulation between two players.'

    def handle(self, *args, **options):
        # Instantiate your players
        player1 = Player(name='Test10', character_alias='Clint')
        player2 = Player(name='Test100', character_alias='Natasha')

        # Create a CombatFactory with the players
        combat_factory = CombatFactory(player1, player2)
        
        # Run the combat
        combat_factory.combat(verbose=True)

        self.stdout.write(self.style.SUCCESS('Successfully ran combat simulation.'))


