## Welcome to Player Generator :information_desk_person:

Player Generator aims to be an extensive generator that will help you create player data with ease for use in Apps / board games / database testing or whatever comes to mind.

### Why was the player generator created?

Although there are numerous types of generators on the internet I wanted to create a versatile generator that can generate a big amount of data for a website I am building (to test it's database).

I Started to put together the generator that I hope to turn into an API (but that's still far away).



### Current features :rocket::

- Name generator - create as many unique names as you'd like and export them to a .csv file.
- Command line arguments - define the type of generator you want using the command-line
- General Basketball player - creates a player with the following properties:
  - name, gender, team, age, height, weight, games_played
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
3. Define the requirements to create new sport models.
4. Implement the option to save to different file types.
4. Restructure the projects file system - put the different generator files in a separate folder.
5. Continuously reworking the README.md :raised_hands:



#### Implemented in past commits:

1. Arrange the code files - split the functions into relevant pages,
   - I want to package the files a bit differently, still figuring that one out :bulb:
2. Finish the basketball player model - without realistic numbers.
3. Implement the .csv export function.
4. Implement the RPG generator (more on that below)



#### Basketball player generator:

Currently the basketball generator generates each player with the following properties:

- Name.
- Gender.
- Team name.
- Age.
- Height.
- Weight.
- Games Played

In the future I'd like to create an algorithm that calculates realistic point scores and more properties.



#### RPG player generator:

Currently the RPG player generator generates each player with the following properties:

- Player general properties: name / gender/ class / age / height / weight

- Player class (one of the following): barbarian / cleric / knight / mage / ranger / rouge
- Class attributes: HP / STR / CON / DEX / INT / WIS / CHA

Ranges of each attributes are based on class and are between the following ranges:

- Low range: 0 - 4
- Mid range: 5 - 7
- High range: 7 - 10



### This is an open source project!

If you'd like to help and work on this project or you have a cool idea you would like me to implement, just open an issue, fork the project or contact me :)

