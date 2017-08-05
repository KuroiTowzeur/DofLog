from zlib import decompress


class Data:

    def __init__(self, data=bytearray()):
        self.data = data
        self.pos = 0

    def __len__(self):
        return len(self.data)

    def __add__(self, byte):
        self.data.extend(byte)
        return self.data

    def __radd__(self, byte):
        temp = bytearay(byte)
        temp.extend(self.data)
        return temp

    def __iadd__(self, byte):
        self.data.extend(byte)
        return self

    def verif(self, l):
        if len(self) < self.pos + l:
            raise IndexError(self.pos, l, len(self))

    def read(self, l):
        self.verif(l)
        self.pos += l
        return self.data[self.pos-l:self.pos]

    def uncompress(self):
        self.data = decompress(self.data)

    def readBoolean(self):
        return bool(self.read(1))

    def readByte(self):
        return int.from_bytes(self.read(1), 'big', signed=True)

    def readUnsignedByte(self):
        return int.from_bytes(self.read(1), 'big')

    def readShort(self):
        return int.from_bytes(self.read(2), 'big', signed=True)

    def readUnsignedShort(self):
        return int.from_bytes(self.read(2), 'big')

    def readInt(self):
        return int.from_bytes(self.read(4), 'big', signed=True)

    def readUnsignedInt(self):
        return int.from_bytes(self.read(4), 'big')

    def readUTF(self):
        textLen = self.readUnsignedShort()
        textRaw = self.read(lon)
        return textRaw.decode()
    
    def readBytes(self, len):
        return self.read(len)

    def writeBoolean(self, b):    
        self.data.extend(bytes([int(b)]))

    def writeByte(self, b):
        self.data.extend(b.to_bytes(1, 'big', signed=True))
        
    def writeUnsignedByte(self, b):
         self.data.extend(b.to_bytes(1, 'big'))

    def writeShort(self, s):
        self.data.extend(s.to_bytes(2, 'big', signed=True))

    def writeUnsignedShort(self, us):
        self.data.extend(us.to_bytes(2, 'big'))

    def writeUnsignedInt(self, ui):
        self.data.extend(ui.to_bytes(4, 'big')

    def writeUTF(self, ch):
        dat = ch.encode()
        self.writeUnsignedShort(len(dat))
        self.data.extend(dat)


class Buffer(Data):

    def end(self):
        self.data = self.data[self.pos:]
        self.pos = 0

# class BooleanByteWrapper():
# 	def getFlag(a,pos):
# 		return bool(a&(2**pos))
# 	def getAllFlags(a,nb_pos):
# 		return tuple(BooleanByteWrapper.getFlag(a,pos) for pos in range(nb_pos))
# 	def setFlag(a, pos, b):
# 		if b:
# 			return a|2**pos
# 		else:
# 			return a&~2**pos
# 	def setAllFlags(a,l):
# 		for pos in range(nb_pos):
# 			a=BooleanByteWrapper.setFlag(a, pos, l[pos])
# 		return a
