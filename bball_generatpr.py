from random import randint, uniform
from name_generator import single_name_generator
from gender_generator import gender_generator
import pandas as pd

def bball_player(name_data, n):
    player_properties = ['name', 'gender', 'team', 'age', 'height', 'weight', 'games_played']
    player_data = {}
    for prop in player_properties:
        player_data[prop] = []

    for _ in range(n):
        gender, player_data['gender'] = gender_generator()

        player_data['name'].append(single_name_generator(name_data, gender))
        
        player_data['team'].append(name_data['basketball-teams'][randint(0,len(name_data['basketball-teams']))])
        
        player_data['height'].append((round(uniform(150, 240), 2)))
        
        player_data['age'].append(randint(18,36))
        
        player_data['weight'].append(randint(50, 110))
        
        player_data['games_played'].append(randint(0,100))

        print(f'Generating player {_} out of {n}')
    return pd.DataFrame(player_data)

