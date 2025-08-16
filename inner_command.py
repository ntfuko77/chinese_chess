import broad
from asyncio import Lock
import re
import json
from resourse import Loader



class InnerCommand:
    def __init__(self, command: str):...


def parse_command(command: str):
    """Parse a command string into a structured format."""
    print(Loader.piece_name.value)
    print(Loader.base_parse_order.value)
    print(Loader.base_parse_number.value)




#input:'馬一進二' or '車一平二'
#output: {'type': 'move', 'piece': '馬', 'from': 1, 'to': 2}

if __name__ == "__main__":
    command= '馬一進二'
    parse_command(command)

