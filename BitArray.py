from math import ceil


class BitArray:
    def __init__(self, bits=None, length=None, file=None):
        if bits is None:
            self.array = 0
            self.length = 0
            if file is not None:
                self.write(file)
        elif type(bits) in {chr, str}:
            self.array = int(bits, 2)
            self.length = len(bits)
            if file is not None:
                self.write(file)
        elif type(bits) == int:
            self.array = bits
            self.length = length if length else bits.bit_length()
            if file is not None:
                self.write(file)
        elif type(bits) == BitArray:
            self.array = bits.array
            self.length = bits.length
            if file is not None:
                self.write(file)
        elif type(bits) == bytes:
            temp = BitArray(int.from_bytes(bits, 'big'))
            cutoff = int(temp[:8])
            self.array = int(temp[8 + cutoff:])
            self.length = len(temp) - (8 + cutoff)
            del temp
            if file is not None:
                self.write(file)
        elif bits is None and file is not None:
            try:
                self.__init__(self.read(file))
            except:
                raise Exception(f'File {file} is invalid!')
        else:
            raise Exception(f"""
Bits must be of type str or int.
{type(bits)} is something completly different.
""")
    
    def __call__(self, step=1):
        for i in range(0, len(self), step):
            if i+step <= len(self):
                yield self[i:i+step]
    
    def __getitem__(self, idx):
        if type(idx) == slice:
            start = (idx.start if idx.start is not None else 0) % len(self)
            stop = (idx.stop if idx.stop is not None else len(self)) % (len(self) + 1)
            return BitArray((self.array >> len(self) - stop) & ((1 << stop - start) - 1),
                            length=stop-start)
        else:
            return BitArray(self.array & 1 << (len(self) - idx - 1) , length=1)
    
    def __setitem__(self, idx, value):
        if type(value) != BitArray:
            raise Exception(f"""
Value must be of type BitArray.
{type(value)} is something completly different.
""")
        cutoff = min(len(self), idx + len(value))
        self.array = (self[:idx]|value[:cutoff]|self[cutoff:]).array
    
    def __or__(self, other):
        return BitArray(self.array << len(other)|other.array, length=len(self) + len(other))
    
    def __repr__(self):
        return f'BitArray[{str(self)}]'
    
    def __str__(self):
        if self.array is not None:
            return bin(self.array).replace('0b', '').zfill(len(self))[:len(self)]
        else:
            return ''
    
    def __len__(self):
        return self.length
    
    def __int__(self):
        return self.array
    
    def __bool__(self):
        return bool(self.array)
    
    def __eq__(self, other):
        return self.array == other.array and len(self) == len(other)