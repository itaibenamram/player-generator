## Welcome to Player Generator :gear:

Player Generator aims to be an extensive generator that will help you create player data with ease for use in Apps / board games / database testing or whatever comes to mind.

### Why was the player generator created? 

Although there are numerous types of generators on the internet I wanted to create a versatile generator that can generate a big amount of data for a website I am building (to test it's database).

I Started to put together the generator that I hope to turn into an API (but that's still far away).



### Current features :rocket::

- Command line arguments - define the type of generator you want using the command-line
- Name generator - create as many unique names as you'd like and export them to a .csv file.
- General Basketball player - creates a player with the following properties:
  - name, gender, team, age, height, weight, games_played
- RPG player generator.
- Generated data into `.csv`.



### How To Use :wrench::

Currently the only way yo use the generator is to clone the repository and download the file,

When in the directory of `player-generator` you can run the generator using `python main.py` or use the command arguments for a quicker use.

The following command line arguments are currently available:

- Generator types (needs to come after `main.py`)
  - `-bball` to activate the basketball player generator.
  - `-rpg` to activate the rpg player generator.
- File name to save to (note that you only need to define the file name, and not the file type).:
  - `-file_name`

Example:

```bash
$ python main.py -bball -players
```

The above example will use the basketball generator and save the results to players.csv.

In the future you'll be able to define the amount of players you want to generate.



### Current To-Do's:

1. Implement the option to choose the amount of players generated via the command line.
2. Implement a single generation type that prints to the console.
3. Define the requirements to create new sport models.
4. Implement the option to save to different file types.
5. Implement a test system for easier development.
6. Continuously reworking the README.md :raised_hands:



### Helping the project:

If you'd like to help and work on this project or you have a cool idea you would like me to implement, just open an issue, fork the project or contact me :)

If you're interested in adding a generator, consider the following things:

- All the generators return a pandas dataframe.
- There currently are no strict standards as to what the generators need to return in terms of properties/schema, meaning if you'd like to create a monster generator it is definitely possible!
- Please insert your newly coded generator under `/generators`
- Do use the available generators if they help your generator structure. Meaning if you need a name for your schema - use the name generator!



#### Change Log:

##### 17/10/2020 -

:heavy_check_mark: Arrange the code files - split the functions into relevant pages,

:heavy_check_mark: Finish the basketball player model - without realistic numbers.

:heavy_check_mark: Implement the .csv export function.

:heavy_check_mark: Implement the RPG generator (more on that below)

:heavy_check_mark: Restructure the project to allow only name generation.

:heavy_check_mark: ​Restructure the projects file system - put the different generator files in a separate folder.

:heavy_check_mark: Various bug fixes.



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
