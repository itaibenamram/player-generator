import sys
import pandas as pd
from bball_generatpr import bball_player
from name_generator import get_data

def generator(n, generator_type):
    """
    main generator function, calls upon the relevant generation function.
    returns a pandas dataframe.

    Keyword arguments:
    n - number of players that needs to be generated.
    generator_type - type of player that needs to be generated.
    """  
    name_data = get_data()
    if generator_type == "-bball":
        player_data = bball_player(name_data, n)
        return pd.DataFrame(player_data)

def generator_type_check(user_argument):
    """
    Checks the type of user input generator.
    returns the argument if it checks out.

    Keyword arguments:
    user_argument - string type
    """  
    possible_arguments = ['main.py', '-bball', '-rpg']
    if user_argument not in possible_arguments:
        raise Exception('An unknown argument was entered')
    else:
        return user_argument
    
def main():
    cl_arguments = sys.argv
    file_name = None
    
    '''
    Handling command line arguments and type of generator to use.
    Arguments are supposed to be entered in the following order:
    python main.py -generator_type -file_name
    '''
    if len(cl_arguments) > 4:
        raise Exception('Too many arguments were entered. Please see the documentations on Github')
    
    elif len(cl_arguments) == 3:
        file_name = cl_arguments[2]
        user_gen_type = cl_arguments[1]
        generator_type = generator_type_check(user_gen_type) 
    elif len(cl_arguments) == 2:
        user_gen_type = cl_arguments[1]
        generator_type = generator_type_check(user_gen_type)

    elif len(cl_arguments) == 1:
        generator_types = {1: '-bball', 2: '-rpg'}
        print('Hello and welcome to Player Generator')
        print('Please choose which type of generator you would like to use: (enter the number according to the list)')
        print('1. Basketball Player Generator \n2. RPG Player Generator')
        user_input = input('Generator: ')
        try:
            user_input = int(user_input)
            generator_type = generator_types[user_input]
        except:
            raise Exception('Generator type must be an integer')


    # Handling number of players generated
    num_players = input("Please enter the number of players you would like to generate: ")
    try:
        num_players = int(num_players)
    except:
        raise Exception('Number of players can only be an integer')
    
    generated_players = generator(int(num_players), generator_type)

    # Handling file name 
    print('If no file name was given when activating the generator, your file will be saved to player.csv')
    if file_name:
        generated_players.to_csv(f'{file_name}.csv')
        print(f'Generated {num_players} players and stored them to {file_name}.csv')
    else:
        generated_players.to_csv('player.csv')
        print(f'Generated {num_players} players and stored them to player.csv')

if __name__ == "__main__":
    main()
    print('Thank you for using Player Generator :D')