from pathlib import Path
from os import chdir
from random import randint, uniform
from generators import gender_generator
import pandas as pd

def get_data():
    """Imports all the names from txt files and returns a dictionary."""

    data_file_names = ['male-names', 'female-names', 'last-names', 'basketball-teams']
    data = {}
    for file in data_file_names:
        path = Path('..')
        file_folder = Path(f"{path.cwd()}/data/")
        file_path = file_folder / f'{file}.txt'
        file_data = open(file_path, 'r')
        file_data = file_data.readlines()
        file_data = list(map(lambda word: word.strip(), file_data))
        data[file] = file_data
    return data


def single_name_generator(name_data, gender):
    """ Generated a full name and returns a string"""
    gender_key = f'{gender}-names'
    first_name = name_data[gender_key][randint(0,len(name_data[gender_key]))].capitalize()
    last_name = name_data['last-names'][randint(0, len(name_data['last-names']))].capitalize()
    full_name = f'{first_name} {last_name}'
    
    return(full_name)

def name_generator(name_data, n):
    ''' Generates a full name, gender => returns a pandas DataFrame '''
    data = {'name': [], 'gender': []}
    for _ in range(n):
        gender, gender_letter = gender_generator.gender_generator()
        data['name'].append(single_name_generator(name_data, gender))
        data['gender'].append(gender_letter)
        print(f'Generating name {_} out of {n}')
    return pd.DataFrame(data)


