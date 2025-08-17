import broad
from asyncio import Lock
import re
import json
from resourse import Loader
from enum import Enum



class InnerCommand:
    def __init__(self, command: str):...


def parse_command(command: str):
    """Parse a command string into a structured format."""
    parse_numbers=[i for i in Loader.base_parse_number.value]+[str(i) for i in range(1,10)]
    parse_piece=[i for i in Loader.piece_name.value]
    parse_order=Loader.base_parse_order.value
    parse_ordered=Loader.base_parse_select_order.value
    parse_all='^[{}]'.format(''.join(parse_piece))
    parse_all+='[{}]'.format(''.join(parse_numbers))
    parse_all+='[{}]'.format(''.join(parse_order))
    parse_all+='[{}]'.format(''.join(parse_numbers))
    parse_all=re.findall(parse_all, command)
    if parse_all!=[]:
        parse_all=parse_all[0]
        return {'actor':parse_all[:2],'target':parse_all[2:4],'piece':parse_all[0]}
    parse_all='^[{}]'.format(''.join(parse_ordered))
    parse_all+='[{}]'.format(''.join(parse_piece))
    parse_all+='[{}]'.format(''.join(parse_order))
    parse_all+='[{}]$'.format(''.join(parse_numbers))
    parse_all=re.findall(parse_all, command)
    if parse_all!= []:
        parse_all=parse_all[0]
        return {'actor':parse_all[:2],'target':parse_all[2:4],'piece':parse_all[1]}
    parse_all='^[{}]'.format(''.join(parse_piece))
    parse_all+='[{}]'.format(''.join(parse_order))
    parse_all+='[{}]$'.format(''.join(parse_numbers))
    parse_all=re.findall(parse_all, command)
    if parse_all!= []:
        parse_all=parse_all[0]
        return {'actor':parse_all[0],'target':parse_all[1:],'piece':parse_all[0]}
    parse_all='^[{}]'.format(''.join(parse_piece))
    parse_all+='[{}]'.format('吃')
    parse_all+='[{}]$'.format(''.join(parse_piece))
    parse_all=re.findall(parse_all, command)
    if parse_all!= []:
        parse_all=parse_all[0]
        return {'actor':parse_all[0],'target':parse_all[2],'piece':parse_all[1]}
    return None

    # result = {}
    # pattern=[i for i in Loader.base_parse_number.value]+[str(i) for i in range(1,10)]+Loader.base_parse_select_order.value
    # pattern='('+'|'.join(pattern)+')'
    # result={"number":re.findall(pattern, command)}

    # pattern=[i for i in Loader.piece_name.value]
    # pattern='('+'|'.join(pattern)+')'
    # result["name"]=re.findall(pattern, command)

    # pattern=Loader.base_parse_order.value
    # pattern='('+'|'.join(pattern)+')'
    # result["order"]=re.findall(pattern, command)


    
    # print(Loader.piece_name.value)
    # print(Loader.base_parse_order.value)
    # print(Loader.base_parse_number.value)

#input:'馬一進二' or '車一平二'
#output: {'type': 'move', 'piece': '馬', 'from': 1, 'to': 2}

if __name__ == "__main__":
    command= ['馬一進二 888','砲吃馬','車一平二','兵平五']
    [print(parse_command(i)) for i in command]
    
    

