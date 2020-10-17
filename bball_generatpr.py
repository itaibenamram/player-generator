from random import randint, uniform
from name_generator import name_generator

def bball_player(name_data, n):
    player_properties = ['name', 'gender', 'team', 'age', 'height', 'weight', 'games_played']
    player_data = {}
    for prop in player_properties:
        player_data[prop] = []

    for _ in range(n):
        gender_type = randint(0,1)
        if gender_type == 1:
            gender = 'male'
            player_data['gender'] = 'M'
        else:
            gender = 'female'
            player_data['gender'] = 'F'
        player_data['name'].append(name_generator(name_data, gender))
        
        player_data['team'].append(name_data['basketball-teams'][randint(0,len(name_data['basketball-teams']))])
        
        player_data['height'].append((round(uniform(150, 240), 2)))
        
        player_data['age'].append(randint(18,36))
        
        player_data['weight'].append(randint(50, 110))
        
        player_data['games_played'].append(randint(0,100))

        print(f'Generating player {_} out of {n}')
    return player_data

