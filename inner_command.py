import broad
from asyncio import Lock
import re
import json
from resourse import Loader



class InnerCommand:
    def __init__(self, command: str):...


def parse_command(command: str,loader:Loader):
    """Parse a command string into a structured format."""
    print(loader.piece_name)
    print(loader.base_parse_order)
    print(loader.base_parse_number)



#input:'馬一進二' or '車一平二'
#output: {'type': 'move', 'piece': '馬', 'from': 1, 'to': 2}

if __name__ == "__main__":
    command= '馬一進二'
    parse_command(command,Loader())

