from random import randint, uniform
import pandas as pd

def get_data():
    data_file_names = ['male-names', 'female-names', 'last-names', 'basketball-teams']
    data = {}
    for file in data_file_names:
        file_path = f'Sports_Player_Generator/data/{file}.txt'
        file_data = open(file_path, 'r')
        file_data = file_data.readlines()
        file_data = list(map(lambda word: word.strip(), file_data))
        data[file] = file_data
    return data

from random import randint, uniform
def name_generator(data, gender):
    gender_key = f'{gender}-names'
    first_name = data[gender_key][randint(0,len(data[gender_key]))].capitalize()
    last_name = data['last-names'][randint(0, len(data['last-names']))].capitalize()
    full_name = f'{first_name} {last_name}'
    
    return(full_name)

def main_generator(n):
    name_data = get_data()
    player_properties = ['name', 'team', 'age', 'height', 'weight', 'games_played']
    player_data = {}
    for prop in player_properties:
        player_data[prop] = []

    for x in range(n):
        gender_type = randint(0,1)
        if gender_type == 1:
            gender = 'male'
        else:
            gender = 'female'
        player_data['name'].append(name_generator(name_data, gender))
        
        player_data['team'].append(name_data['basketball-teams'][randint(0,len(name_data['basketball-teams']))])
        
        player_data['height'].append((round(uniform(150, 240), 2)))
        
        player_data['age'].append(randint(18,36))
        
        player_data['weight'].append(randint(50, 110))
        
        player_data['games_played'].append(randint(0,100))
    
    return pd.DataFrame(player_data)
    