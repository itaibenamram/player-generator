## Welcome to Player Generator :gear:

A generator that will help you create player data with ease for use in apps / board games / database testing or whatever comes to mind.

### Why was the player generator created? 

Although there are numerous types of generators on the internet I wanted to create a versatile generator that can generate a big amount of data for a website I am building (to test it's database), so might as well share it to get some thoughts/code reviews etc...

### Current features :rocket::

- Command line arguments - define the type of generator you want using the command-line
- Name generator - create as many unique names as you'd like and export them to a .csv file.
- General Basketball player - creates a player with the following properties:
  - name, gender, team, age, height, weight, games_played
- RPG player generator.
- Generated data into `.csv` (more supported types in the future :D).



### How To Use :wrench::

Currently the only way yo use the generator is to clone the repository and download the file,

When in the directory of `player-generator` you can run the generator using `python main.py` or use the command arguments for a quicker use.

The following command line arguments are currently available:

- Generator types - defined using the `gentype=` followed by the generator types available:
  - `name` to activate the name generator.
  - `bball` to activate the basketball player generator.
  - `rpg` to activate the RPG player generator.
- File name to save to (note that you only need to define the file name, and not the file type).:
  - `file_name=<your-file-name>`
- Use `--silent` to hide the console logging of player generation.
- Use `--print` to print the results to console and not save them.
- To define the amount of generated players you want through the command-line use the `genamount=` argument

Example:

```bash
$ python main.py gentype=bball filename=players genamount=50 --silent
```

The above example will use the basketball generator to generate 50 players and save the results to players.csv.

In the future you'll be able to define the amount of players you want to generate.



### Current To-Do's:

Small features :hatching_chick:: 

3. Define the requirements to create new generator.
4. Implement the option to save to different file types.
5. Implement a test system for easier development.
6. Continuously reworking the README.md :raised_hands:

Big features :muscle::

1. Create a custom generator type (user can define the required properties) - or read requirements from JSON files.
2. Enable the user to drop unnecessary generator properties.



### Helping the project:

If you'd like to help and work on this project or you have a cool idea you would like me to implement, just open an issue, fork the project or contact me :)

If you're interested in adding a generator, consider the following things:

- All the generators return a pandas DataFrame.
- There currently are no strict standards as to what the generators need to return in terms of properties/schema, meaning if you'd like to create a monster generator it is definitely possible!
- Please insert your newly coded generator under `/generators`
- Do use the available generators if they help your generator structure. Meaning if you need a name for your schema - use the name generator!



#### Change Log:

##### 19/10/2020:

:heavy_check_mark: If only 1 player is generated, it'll print to console.

:heavy_check_mark: Enabled the option to print all the results to console and not save them - using `--print`

:heavy_check_mark: Added more function documentations.

:heavy_exclamation_mark: Edited the README.md ( Always nice :happy: )



#### Name Generator :name_badge::

Generates a full name and a gender (gender is based on the name).



#### Basketball player generator :basketball::

Currently the basketball generator generates each player with the following properties:

- Name.
- Gender.
- Team name.
- Age.
- Height.
- Weight.
- Games Played

In the future I'd like to create an algorithm that calculates realistic point scores and more properties.



#### RPG player generator :crossed_swords::

Currently the RPG player generator generates each player with the following properties:

- Player general properties: name / gender/ class / age / height / weight

- Player class (one of the following): barbarian / cleric / knight / mage / ranger / rouge
- Class attributes: HP / STR / CON / DEX / INT / WIS / CHA

Ranges of each attributes are based on class and are between the following ranges:

- Low range: 0 - 4
- Mid range: 5 - 7
- High range: 7 - 10
