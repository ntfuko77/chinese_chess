import numpy
import json
from PIL import Image
class Broad():
    def __init__(self):
        self.onbraod=Image.new("RGBA",(969,1118),(0,0,0,0))
        path='configs/definition.json'
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            opening_setup=data['opening_setup']
            self.dic_console_name_p=data["consol_name_p"]

            basic_position=numpy.zeros((32, 2), dtype=int)
            basic_state=numpy.zeros((32,2),dtype=int)
            basic_type=numpy.zeros((32, 2), dtype=object)
            for i in range(32):
                x=opening_setup[str(i)]['placement']
                x=numpy.array([x%9,x//9])
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
        ...
    @property
    def real_positon(self):
        out=self.basic_position.copy()
        out=out*numpy.array([105,108])
        out=out+numpy.array([17,24])
        return out
class Picture_loader:
    def __init__(self):
        self.background=Image.open('pic/0.jpg')
class picture():
    def __init__(self,loader:Picture_loader):
        self.loader=loader
        self.refresh()
        self.mask=Image.open("pic/mask.png")
        self.mask=self.mask.resize((90,90))
        self.pieces=[Image.open('pic/b'+str(i)+'.png') for i in range(7)]
        self.pieces+=[Image.open('pic/r'+str(i)+'.png') for i in range(7)]
        self.pieces=[i.resize((90,90)) for i in self.pieces]
        return
    def draw_piece(self,broad:Broad):
        p_position=broad.real_positon
        for number in range(32):
            if broad.basic_state[number, 1] == 1:
                return
            pic_num= broad.basic_state[number,0]
            pic = self.pieces[pic_num] if number <16 else self.pieces[pic_num+7]
            pos = p_position[number]
            broad.onbraod.paste(pic, (int(pos[0]), int(pos[1])), self.mask)
        return

    def draw(self,broad:Broad):
        out=self.background.copy()
        out.paste(self.background,(0, 0))
        self.draw_piece(broad)
        out.paste(broad.onbraod,(0, 0), broad.onbraod)
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
