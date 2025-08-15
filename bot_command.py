import json
def load(path=r'configs\bot.json'):
    """Load bot configuration from a JSON file."""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
def ctreate_room():
    ...

if __name__ == '__main__':
    data=load()
    print(data)