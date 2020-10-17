from random import randint, uniform
from name_generator import name_generator
from gender_generator import gender_generator
import pandas as pd

def attribute_gen(att_range):

    ''' Generates attributes based on the range values below, returns an integer'''

    low_range = (1,4)
    mid_range = (5,7)
    high_range = (7,10)

    if att_range == 'l':
        return randint(low_range[0], low_range[1])
    elif att_range == 'm':
        return randint(mid_range[0], mid_range[1])
    elif att_range == 'h':
        return randint(high_range[0], high_range[1])
    else: 
        raise TypeError('There was an error in the range definition')

def rpg_player(name_data, n):

    ''' Generates an RPG player, based on the properties below. Returns a pandas DataFrame '''

    possible_classes = ['barbarian', 'cleric', 'knight', 'mage', 'ranger', 'rouge']
    
    player_properties = ['name', 'gender', 'class', 'age', 'height', 'weight']
    
    p_classes_att_range = {
        'barbarian': [('HP', 'm'), ('STR', 'h'), ('CON', 'm'), ('DEX', 'l'), ('INT', 'l'), ('WIS', 'l'), ('CHA', 'l')],
        'cleric': [('HP', 'l'), ('STR', 'l'), ('CON', 'l'), ('DEX', 'l'), ('INT', 'm'), ('WIS', 'h'), ('CHA', 'l')],
        'knight': [('HP', 'h'), ('STR', 'm'), ('CON', 'l'), ('DEX', 'l'), ('INT', 'l'), ('WIS', 'l'), ('CHA', 'm')],
        'mage': [('HP', 'l'), ('STR', 'l'), ('CON', 'l'), ('DEX', 'l'), ('INT', 'h'), ('WIS', 'm'), ('CHA', 'l')],
        'ranger': [('HP', 'm'), ('STR', 'l'), ('CON', 'm'), ('DEX', 'm'), ('INT', 'l'), ('WIS', 'l'), ('CHA', 'l')],
        'rouge': [('HP', 'm'), ('STR', 'l'), ('CON', 'm'), ('DEX', 'h'), ('INT', 'l'), ('WIS', 'l'), ('CHA', 'm')],}

    player_attributes = ['HP', 'STR', 'CON', 'DEX', 'INT', 'WIS', 'CHA']
    
    # Initializing the data stores.
    p_data_pro = {}
    p_data_att = {}
    for prop in player_properties:
        p_data_pro[prop] = []
    for att in player_attributes:
        p_data_att[att] = []

    for _ in range(n):
        class_type = possible_classes[randint(0,5)]
        # Generate player_properties
        gender, gender_letter = gender_generator()

        p_data_pro['gender'].append(gender_letter)

        p_data_pro['name'].append(name_generator(name_data, gender))
        
        p_data_pro['height'].append((round(uniform(150, 240), 2)))
        
        p_data_pro['age'].append(randint(18,36))
        
        p_data_pro['weight'].append(randint(50, 110))

        p_data_pro['class'].append(class_type)

        # Generate player_attributes based on class
        for attribute_type, attribute_range in p_classes_att_range[class_type]:
            p_data_att[attribute_type].append(attribute_gen(attribute_range))      

        print(f'Generating player {_} out of {n}')

    df_data_pro = pd.DataFrame(p_data_pro)
    df_data_att = pd.DataFrame(p_data_att)

    return df_data_pro.join(df_data_att)
        