from sys import argv
import memory
import re
import rrf

class assembler:

    def __init__(self, fileName):
        self.memory = memory.mainMemory()
        self.regValues = [0 for i in range(16)]
        self.assemble(fileName)

    def assemble(self, fileName):
        with open(fileName, 'r') as f:
            pc = 0
            lines = f.readlines()
            self.labels = self.generateLabelAddresses(lines)
            for l in lines:
                # comment
                if l[0] == '#':
                    continue
                # setting initial regValues
                elif l[:2] == '$R':
                    rid = int(l.split('$')[1][1:])
                    self.regValues[rid] = int(l.split('$')[2])
                elif l[:1] == '$':
                    location = int(l.split('$')[1])
                    value = int(l.split('$')[2])
                    self.memory[location] = value
                elif ':' in l:
                    if l.split(':')[1].strip() != '':
                        self.parse(l.split(':')[1].strip(), pc)
                        pc += 2
                else:
                    self.parse(l.strip(), pc)
                    pc += 2


    def parse(self, instruction, pc):
        code = {'ADD': 0, 'SUB': 2, 'MUL': 6, 'LD': 8, 'SD': 10, 'JMP': 12, 'BEQZ': 13, 'HLT': 14}
        parts = instruction.split()
        word = 0
        opcode = code[parts[0]]
        operand1 = 0
        operand2 = 0
        operand3 = 0
        if '#' in instruction:
            opcode |= 1
        t = re.sub(r'[^0-9]*', ' ', instruction)
        if parts[0] == 'JMP':
            operand3 = self.labels[parts[1]]
        elif parts[0] == 'BEQZ':
            operand1 = int(t.split()[0])
            operand3 = self.labels[parts[2]]
        elif parts[0] != 'HLT':
            operand1 = int(t.split()[0])
            operand2 = int(t.split()[1])
            operand3 = int(t.split()[2])
        self.memory[pc] = self.createInstruction(opcode, operand1, operand2, operand3)

    def createInstruction(self, opcode, operand1, operand2, operand3):
        return (opcode << 12) | (operand1 << 8) | (operand2 << 4) | operand3

    def generateLabelAddresses(self, lines):
        addr = 0
        labels = {}
        for l in lines:
            if l[0] == '$' or l[0] == '#':
                continue
            elif ':' in l:
                labels[l.split(':')[0]] = addr
                addr += 2
            else:
                addr += 2
        return labels


def fourBits(t):
    return [t >> 12, (t >> 8) & 15, (t >> 4) & 15, t & 15]
if __name__ == '__main__':
    a = assembler(argv[1])
    print(a.regValues)