import pandas as pd
from random import randint, uniform
from name_generator import get_data, name_generator

def generator(n):
    name_data = get_data()
    player_properties = ['name', 'team', 'age', 'height', 'weight', 'games_played']
    player_data = {}
    for prop in player_properties:
        player_data[prop] = []

    for _ in range(n):
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
    
def main():
    num_players = input("Please enter the number of players you would like to generate: ")
    file_path = input("Please enter where you want the results to be saved: ")
    generated_players = generator(int(num_players))
    generated_players.to_csv(f'{file_path}.csv')
    print(f'Generated {num_players} and stored them to {file_path}.csv')

if __name__ == "__main__":
    main()