from random import randint, uniform

def gender_generator():
    ''' randomly generates the player gender and gender_letter '''
    gender_type = randint(0,1)
    if gender_type == 1:
        gender = 'male'
        gender_letter = 'M'
    else:
        gender = 'female'
        gender_letter = 'F'
    return (gender, gender_letter)