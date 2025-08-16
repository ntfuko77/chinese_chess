import json

# manager lock and congifdata and difinition
class Loader:
    def __init__(self):
        path='configs/definition.json'
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.piece_name = data['identity_form']
            self.base_parse_order = data["parse_form"]["base_order"]
            self.base_parse_number = data["parse_form"]["move_number"]