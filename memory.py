from pprint import pprint


class mainMemory:

    def __init__(self):
        self.memory = [0 for i in range(1024)]

    def __getitem__(self, index):
        return self.combineBytes(self.memory[index], self.memory[index + 1])

    def __setitem__(self, index, value):
        self.memory[index] = self.lsb(value)
        self.memory[index + 1] = self.msb(value)

    def readByte(self, index):
        return self.memory[index]

    def writeByte(self, index, value):
        self.memory[index] = value

    def lsb(self, value):
        return value & 255

    def msb(self, value):
        return value >> 8

    def combineBytes(self, lsb, msb):
        return (msb << 8) + lsb

if __name__ == '__main__':
    m = mainMemory()
    print(m.lsb(-16), m.msb(-16), m.combineBytes(m.lsb(-16), m.msb(-16)))
    # m[10] = 100
    # m[1000] = 1000
    # pprint(vars(m))
