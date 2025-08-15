import broad
from asyncio import Lock
class InnerCommand:
    def __init__(self, command: str):...

def parse_command(command: str):...
#input:'馬一進二' or '車一平二'
#output: {'type': 'move', 'piece': '馬', 'from': 1, 'to': 2}