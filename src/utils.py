import yaml
import os


my_input = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.yaml')

def get_inputs(inputs_file=my_input, args=None):
    '''
    reads inputs from YAML file
    INPUTS:
        my_input (str): path to YAML file
    OUTPUTS:
        person attributes to be read by the generations.py file
    '''
    with open(inputs_file, 'r') as stream:
        inputs = yaml.safe_load(stream)
    inputs = check_inputs(inputs)
    return inputs

def check_inputs(inputs):
    '''
    validates user inputs
    '''
    inputs['num_years'] = validate_num_years(inputs['num_years'])
    inputs['start_year'] = validate_start_year(inputs['start_year'], inputs['num_years'])
    inputs['father'] = validate_father(inputs['father'])
    inputs['mother'] = validate_mother(inputs['mother'])

    return inputs

def validate_num_years(num_years):
    '''
    checks to make sure that the num_years attribute is an integer < 3000
    '''
    if num_years < 3000 and isinstance(num_years, int):
        return num_years
    else:
        raise Exception("Your simulation is running for too long (num_years + start_year > 2999), or num_years isn't a valid integer")

def validate_start_year(start_year, num_years):
    '''
    checks to make sure that the start_year is valid
    '''
    if start_year + num_years < 3000 and isinstance(start_year, int):
        return start_year
    else:
        raise Exception("Your simulation is running for too long (num_years + start_year > 2999), or start_year isn't a valid integer")

def validate_father(father):
    '''
    checks to make sure that the father's attributes are valid
    '''
    if isinstance(father[0], str) and isinstance(father[1], str) and isinstance(father[2], int) and isinstance(father[3], int):
        return father
    else:
        raise Exception("There's somethign wrong with your father")

def validate_mother(mother):

    if isinstance(mother[0], str) and isinstance(mother[1], str) and isinstance(mother[2], int) and isinstance(mother[3], int):
        return mother
    else:
        raise Exception("There's something wrong with your mother")


get_inputs()
