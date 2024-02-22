
OVERVIEW
This repo is an ongoing project that I have been working on in earnest for about a month as attempt to implement a discord chat bought version of the alchemy system in Elder Scrolls IV: Oblivion. I love this Alchemy system and have very few critiques of it - I would love to see it and have access to it wherever I go. 

Currently this bot is being hosted through Heroku and all of its CI/CD is done there. I am not currently planning on rolling it out widely to external servers until I have the ability to be
sure that it will pay for itself without any issues regarding monetization and IP licensing. But we'll cross that bridge when we come to it.

The resources folder contains all of the broad data that will eventually be replaced by some form of post grass database. And there are several other minor files like… That are part of the Hoku implementation that I have in place right now.
The functioning portion of this code right now is a view set that randomly select a new flower from somewhere in Tamriel and presents it to the user in the form of the discord message complete with emojis representing the various magical, active effects

- oblivion_alchemy.py
This file contains an ongoing implementation of the various details for calculating duration and magnitude for various potions. A few of the critical components have already been implemented like stacking and returning a set of all matching common effects from any matching strings of plant names in find_common_effects_between_plants(). The method for determining and overriding negative effects for positive ones in get_polarity_from_effects() etc. 

All of this work is an attempt to implement the ssytems outlined in the Oblivion:Alchemy page on the UESP Wiki largely written by the modding community for Oblivion located here (https://en.uesp.net/wiki/Oblivion:Alchemy)

I still have yet to create methods for contributions from all of the Retort Magnitude Factors and 
calculating the contributions of various changes in Player active effects. But It is a work in progress. 


DISCORD IMPLEMENTATION.
- discord_bot.py
Currently all existing functionality for the Discord bot is contained withint discord_bot.py. There is a View that retrieves a single random flower from a method on the Plant class in plant.py.

- plant.py

This will likely be a very lean class that wraps and delivers any functionality native to individual or collections of plants to be handed over to the AlchemyFactory. 

- player.py
This is just a file that will hold all state based information about characters and enemy NPC's which will be one of the three different "gameplay loops" for this bot. 

- combat.py
Eventually this will be a spot for 


Validated against potions results generated here:
https://en.uesp.net/oblivion/alchemy/alc_calc.php
