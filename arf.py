
class entry:
    def __init__(self,i):
        self.data = i
        self.tag = 0
        self.busy = 0

class rrf:
    def __init__(self, regValues):
        self.registers = [entry(i) for i in regValues]

    def __getitem__(self, index):
        return self.registers[index]

    def __setitem__(self, index,value):
        self.registers[index] = value
