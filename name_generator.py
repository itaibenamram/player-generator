from pathlib import Path

def get_data():
    data_file_names = ['male-names', 'female-names', 'last-names', 'basketball-teams']
    data = {}
    for file in data_file_names:
        file_folder = Path("data/")
        file_path = file_folder / f'{file}.txt'
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