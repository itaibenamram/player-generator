import sys
import pandas as pd
from generators import gender_generator, bball_generator, name_generator, rpg_generator 

# TODO implement a single use print to console mode.
# TODO implement save type file.

name_gen_name = 'name'
basketball_gen_name = 'bball'
rpg_gen_name = 'rpg'


def commandline_argument_check(command_input):
    ''' 
    Accepts the list of the command inputted by the user and
    Turns on / off the generator settings
    Returns the relevant settings?

    console commands - effect the data displayed when generator runs.
    main commands - define which generator to use and file type / name.

    '''
    # Default Settings
    gentype = None
    file_name = None
    file_type = '.csv'
    checked_arguments = {'silent': False,
                    'genamount' : None,
                    'filetype': file_type,
                    'gentype': gentype,
                    'filename': file_name}
    
    possible_generators = [name_gen_name, basketball_gen_name, rpg_gen_name]

    # Handle the command arguments
    main_commands = [command.split('=') for  command in command_input if '=' in command]
    console_commands = [command for command in command_input if '--' in command]

    m_commands_dic = {}
    try:
        for command_type, user_argument in main_commands:
            m_commands_dic[command_type] = user_argument
    except:
        raise Exception('One or more than one arguments were not entered correctly.')

    # comparing user arguments to available arguments:
    for key in m_commands_dic:
        try:
            if key == 'gentype':
                if m_commands_dic[key] in possible_generators:
                    checked_arguments[key] = m_commands_dic[key]
                else:
                    print('Invalid generator was entered - please pick one from the list below.')
            if key == 'genamount':
                try:
                    checked_arguments[key] = int(m_commands_dic[key])
                except ValueError:
                    raise ValueError('Invalid number of generated players requested.')
            else:
                checked_arguments[key] = m_commands_dic[key]
        except KeyError:
            continue

    if '--silent' in console_commands:
        checked_arguments['silent'] = True

    return checked_arguments


def generator(n, generator_type, silent):
    """
    main generator function, calls upon the relevant generation function.
    returns a pandas dataframe.

    Keyword arguments:
    n - number of players that needs to be generated.
    generator_type - type of generator that needs to be used (type tuple => Generator_name, generator_type)
    silent - boolean, if user wants to prints the process to the commandline
    """  
    name_data = name_generator.get_data()
    
    if generator_type == basketball_gen_name:
        player_data = bball_generator.bball_player(name_data, n, silent)
    elif generator_type == rpg_gen_name:
        player_data = rpg_generator.rpg_player(name_data, n, silent)
    elif generator_type == name_gen_name:
        player_data = name_generator.name_generator(name_data, n, silent)

    return player_data


def main():
    checked_arguments = commandline_argument_check(sys.argv)  

    if checked_arguments['gentype'] == None:
        generator_types = [('Name Generator', name_gen_name),
                        ('Basketball Player Generator', basketball_gen_name),
                        ('RPG Player Generator', rpg_gen_name)]
        generator_dic = {}
        print('Please choose which type of generator you would like to use: (enter the number according to the list)')
        
        i = 0
        for gen_name, gen_type in generator_types:
            generator_dic[gen_type] = i
            i += 1
            print(f'{i}. {gen_name}')
        
        user_input = input('Generator: ')
        try:
            user_input = int(user_input)
            generator_type = generator_types[user_input - 1]
            checked_arguments['gentype'] = generator_type[1] 
        except:
            raise Exception('Generator type must be an integer')
    else:
        print(f'Generator type is : {checked_arguments["gentype"]}')

    # Handling number of players generated
    if checked_arguments['genamount'] == None:
        num_players = input("Please enter the number of players you would like to generate: ")
        try:
            checked_arguments['genamount'] = int(num_players)
        except:
            raise Exception('Number of players can only be an integer')
    
    # Generating the data
    generated_players = generator(checked_arguments['genamount'], checked_arguments['gentype'], checked_arguments['silent'])

    # Handling file name 
    if checked_arguments['filename']:
        generated_players.to_csv(f'{checked_arguments["filename"]}{checked_arguments["filetype"]}')
        print(f'Generated {checked_arguments["genamount"]} players and stored them to {checked_arguments["filename"]}{checked_arguments["filetype"]}')
    else:
        print(f'No file name was given when activating the generator, your file will be saved to player{checked_arguments["filetype"]}')
        generated_players.to_csv('player.csv')
        print(f'Generated {checked_arguments["genamount"]} players and stored them to player{checked_arguments["filetype"]}')

if __name__ == "__main__":
    main()
    print('Thank you for using Player Generator if you liked the generator please star the project on github!')
    print('https://github.com/itaibenamram/player-generator')