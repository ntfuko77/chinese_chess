import json
from enum import Enum

# manager lock and congifdata and difinition
class Loader(Enum):
    path='configs/definition.json'
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        piece_name = data['identity_form']
        base_parse_order = data["parse_form"]["base_order"]
        base_parse_number = data["parse_form"]["move_number"]
        base_parse_select_order = data["parse_form"]["ordered"]