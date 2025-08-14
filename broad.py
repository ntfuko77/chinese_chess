import numpy
import json
class Broad():
    def __init__(self):
        path='difinition.json'
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            opening_setup=data['opening_setup']
            self.dic_console_name_p=data["consol_name_p"]

            basic_position=numpy.zeros((32, 2), dtype=int)
            basic_state=numpy.zeros((32,2),dtype=int)
            basic_type=numpy.zeros((32, 2), dtype=object)
            for i in range(32):
                x=opening_setup[str(i)]['placement']
                x=numpy.array([x//9,x%9])
                basic_position[i]= x
                x=opening_setup[str(i)]['type']
                basic_state[i]=[x,0]
                


            self.basic_position=numpy.array(basic_position)
            self.basic_state=basic_state
    @property
    def basic_type(self):
        out=numpy.zeros((32, 2), dtype=object)
        for i in range(32):
            out[i,0]=self.dic_console_name_p[str(self.basic_state[i, 0])]
            out[i,1]='alive' if self.basic_state[i, 1] == 0 else 'dead'
            
        return out


if __name__ == "__main__":
    broad = Broad()
    print(numpy.hstack((broad.basic_position, broad.basic_type,broad.basic_state)))
print('start')
