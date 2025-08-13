from PIL import Image

class position():
    def __init__(self,p):
        if p==-99:
            self.inboard=False
            return
        self.inboard=True
        def to_two_dimensional(p:int)->tuple:
            if p>=0:
                return (p%9,p//9)
            if p<0:
                return to_two_dimensional(90+p)
            
        if type(p)==int:
            p=to_two_dimensional(p)

        x=[17+i*105 for i in range(9)]
        y=[24+i*108 for i in range(10)]
        self.index=p[0]+p[1]
        self.p=(x[p[0]], y[p[1]])
        self.tp=p
        return
    def __getitem__(self):
        return self.index
    def index(self,n:int):
        return position((n%9,n//9))
        
        
class pieces():
    
    def __init__(self,name,own:bool,pos:position):
        x=['車','馬','象','士','將','砲','兵']
        x_2=['俥','傌','相','仕','帥','炮','卒']
        ind={x[i]:('pic/b'+str(i)+'.png','pic/r'+str(i)+'.png') for i in range(7)}
        ind.update({x_2[i]:ind[x[i]] for i in range(7)})
        ind={i:(Image.open(ind[i][0]),Image.open(ind[i][1])) for i in ind}
        self.pos=pos
        self.own=own
        if own:
            self.img=ind[name][0]
        else:
            self.img=ind[name][1]
        if name in x :
            self.name = name
        return

class game():
    def p_resize(self,n=90):
        self.p_resize=([i.img.resize((n,n)) for i in self.piece[0]],[i.img.resize((n,n)) for i in self.piece[1]])
        self.mask=Image.open("pic/mask.png")
        self.mask=self.mask.resize((n,n))
        return
    def __init__(self):
        name=['車','馬','象','士']
        name=name+['將']+name[::-1]+['砲']*2+['卒']*5
        pie=([pieces(i,True,position(-99)) for i in name],[pieces(i,False,position(-99)) for i in name])
        self.piece=pie
        self.back=Image.open('pic/0.jpg')
    def paste_all(self):
        self.p_resize()
        onboardpie=([i for i in self.piece[0]+self.piece[1] if i.pos.inboard])
        [self.out.paste(i.img.resize((90,90)),i.pos.p,self.mask) for i in onboardpie]
        return
    def start_game(self):
        place=(0,1,2,3,4,5,6,7,8,19,25,27,29,31,33,35)
        for b_r_piece in self.piece:
            for i in range(16):
                if b_r_piece[i].own:
                    b_r_piece[i].pos=position(place[i])
                else:
                    b_r_piece[i].pos=position(-place[i]-1)
        return
    def show(self):
        self.out=Image.new("RGBA",(969,1118))
        self.out.paste(self.back)
        self.paste_all()
        self.out.show()
        return
    
if __name__ == '__main__':
    g=game()
    g.start_game()
    g.show()
"""
x=position((2,5))
back=Image.open("pic/0.jpg")
a=Image.open("pic/bp0.png")
a=a.resize((90,90))
out=Image.new("RGBA",(969,1118))
mask=Image.open("pic/mask.png")
mask=mask.resize((90,90))
out.paste(back)
out.paste(a,x.p,mask)
out.show()

broad = Image.open("c87f0f89d89027925cce477fb5045e0c.png")
rb = [Image.open("Xiangqi_rd1.png")]
rb = [i.resize((67,67)) for i in rb]

out = Image.new("RGBA" , (800,1067))
out.paste(broad)
out.paste(rb[0] , position((2,5)).p,rb[0])
out.show()
"""
