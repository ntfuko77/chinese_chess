import numpy
import json
from PIL import Image
from enum import Enum

class config(Enum):
    broad_size=(969,1118)
    piece_space=[105,108]
    piece_fix=[17,24]
    piece_size=(90,90)



class Layer:
    broad_size=config.broad_size.value
    empty=Image.new("RGBA",broad_size,(0,0,0,0))

class Base_piece:
    piece_space=config.piece_space.value
    piece_fix=config.piece_fix.value
    piece_size=config.piece_size.value


class Broad():
    def __init__(self):
        self.layer=None
        path='configs/definition.json'
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            opening_setup=data['opening_setup']
            self.dic_console_name_p=data["consol_name_p"]

            basic_position=numpy.zeros((32, 2), dtype=int)
            basic_state=numpy.zeros((32,2),dtype=int)

            for i in range(32):
                x=opening_setup[str(i)]['placement']
                x=numpy.array([x%9,x//9])
                basic_position[i]= x
                x=opening_setup[str(i)]['type']
                basic_state[i]=[x,0]
                


            self.basic_position=numpy.array(basic_position)
            self.basic_state=basic_state
    @property
    def consol_view(self):
        out=numpy.zeros((32, 2), dtype=object)
        for i in range(32):
            out[i,0]=self.dic_console_name_p[str(self.basic_state[i, 0])]
            out[i,1]='alive' if self.basic_state[i, 1] == 0 else 'dead'
        return numpy.hstack((self.basic_position, out))
    @property
    def basic_view(self):
        out=numpy.hstack((self.basic_position, self.basic_state))
        return out
    @property
    def total_view(self):
        out=numpy.hstack((self.basic_position, self.basic_state, self.consol_view))
        return out
    @property
    def real_positon(self):
        out=self.basic_position.copy()
        out=out*numpy.array(Base_piece.piece_space)
        out=out+numpy.array(Base_piece.piece_fix)
        return out
class Picture_loader:
    def __init__(self):
        self.background=Image.open('pic/0.jpg')
class picture():
    def __init__(self,loader:Picture_loader):
        self.loader=loader
        self.refresh()
        self.mask=Image.open("pic/mask.png")
        self.mask=self.mask.resize(Base_piece.piece_size)
        self.pieces=[Image.open('pic/b'+str(i)+'.png') for i in range(7)]
        self.pieces+=[Image.open('pic/r'+str(i)+'.png') for i in range(7)]
        self.pieces=[i.resize(Base_piece.piece_size) for i in self.pieces]
        return
    def draw_piece(self,broad:Broad):
        p_position=broad.real_positon
        for number in range(32):
            if broad.basic_state[number, 1] == 1:
                return
            pic_num= broad.basic_state[number,0]
            pic = self.pieces[pic_num] if number <16 else self.pieces[pic_num+7]
            pos = p_position[number]
            broad.layer = Layer.empty.copy()
            broad.layer.paste(pic, (int(pos[0]), int(pos[1])), self.mask)
        return

    def draw(self,broad:Broad):
        out=self.background.copy()
        out.paste(self.background,(0, 0))
        self.draw_piece(broad)
        out.paste(broad.layer,(0, 0), broad.layer)
        out=out.convert("RGB")
        out.save('pic/broad.jpg',"JPEG", quality=20)
    def refresh(self):
        original=Image.new("RGBA",(969,1118))
        original.paste(self.loader.background,(0, 0))
        self.background=original
        return




if __name__ == "__main__":
    broad = Broad()
    loader= Picture_loader()
    pic= picture(loader)    
    pic.draw(broad)
