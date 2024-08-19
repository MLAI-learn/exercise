class Mobilephone:
    def __init__(self,st,n,d,f,r,ram,s):
        self.Screentype=st
        self.Networktype=n
        self.Dualsim=d
        self.Frontcamera=f
        self.rearcamera=r
        self.RAM=ram
        self.Storage=s


    def make_call(self):
         print('making call')

    def recieve_call(self):
         print('call recived')

    def take_a_picture(self):
         print('picture captured')

    

class Apple(Mobilephone):
    def __init__(self,name, st, n, d, f, r, ram, s,rr):
        Mobilephone.__init__(self,st, n, d, f, r, ram, s)
        self.refreshrate= rr
        self.name=name
    
    def __str__(self):
        return f'''the specs of {self.name} are:
    Screentype={self.Screentype}
    Networktype={self.Networktype}
    DualSim={self.Dualsim}
    Frontcamera={self.Frontcamera}
    rearcamera={self.rearcamera}
    RAM={self.RAM}
    Storage={self.Storage}
    Refreshrate={self.refreshrate}'''


class Samsung(Mobilephone):
    def __init__(self,name, st, n, d, f, r, ram, s,ui):
        Mobilephone.__init__(self,st, n, d, f, r, ram, s)
        self.ui=ui
        self.name=name
    

    def __str__(self):
        return f'''the specs of {self.name} are:
    Screentype={self.Screentype}
    Networktype={self.Networktype}
    DualSim={self.Dualsim}
    Frontcamera={self.Frontcamera}
    rearcamera={self.rearcamera}
    RAM={self.RAM}
    Storage={self.Storage}
    UI={self.ui}'''


iphone_15=Apple('iphone','touch screen','5G','true','16MP','48MP','4GB','64GB','90hz')

A15=Samsung('A15','touch screen','5G','true','16MP','48MP','4GB','64GB','one UI')
 
print(iphone_15)
print(A15)
A15.make_call()
iphone_15.recieve_call()
iphone_15.take_a_picture()
print(A15.Screentype)





