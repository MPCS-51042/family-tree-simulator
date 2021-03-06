import yaml
import os


my_input = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.yaml')

def get_inputs(inputs_file=my_input, args=None):

    with open(inputs_file, 'r') as stream:
        inputs = yaml.safe_load(stream)

    return inputs


get_inputs()





