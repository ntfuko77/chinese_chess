import numpy
import json
from PIL import Image
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
    @property
    def view(self):
        out=numpy.hstack((self.basic_position, self.basic_state))
class picture():
    def __init__(self):
        self.background=Image.open('pic/0.jpg')
        self.mask=Image.open("pic/mask.png")
        self.mask=self.mask.resize((90,90))
        self.pieces=[Image.open('pic/b'+str(i)+'.png') for i in range(7)]
        self.pieces+=[Image.open('pic/r'+str(i)+'.png') for i in range(7)]
        self.pieces=[i.resize((90,90)) for i in self.pieces]
        return
    def draw(self,broad:Broad):
        out=Image.new("RGBA",(969,1118))
        out.paste(self.background)
        out.show()

if __name__ == "__main__":
    broad = Broad()
    pic= picture()
    pic.draw(broad)
