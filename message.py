from binrw import Data

class Msg():

    def __init__(self, buf):
        self.b = True
        try:
            self.header = int.from_bytes(buf.read(2), byteorder='big')
            
            self.id = self.header >> 2
            self.lenType = self.header & 3
            
            self.lenData = int.from_bytes(buf.read(self.lenType), byteorder='big')
                      
        except IndexError:
            buf.pos = 0
            self.b = False
        else:
            buf.end()

    def __bool__(self):
        return self.b
