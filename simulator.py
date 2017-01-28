from sys import argv
import assembler
import memory
import arf
import fetch
import decode
import dispatch
import fu
import reorder
import writeBack

fetchDelay = 1
decodeDelay = 1
dispatchDelay = 1
fuDelay = 1
reorderDelay = 1
writeBackDelay = 1


class processor:

    def __init__(self, memory, regValues):
        self.memory = memory
        self.arf = arf.arf(regValues)

        self.clock = simpy.Environment()

        self.fetchUnit = fetch.fetchUnit(clock, fetchDelay)
        self.decodeUnit = decode.decodeUnit(clock, decodeDelay)
        self.dispatchUnit = dispatch.dispatchUnit(clock, dispatchDelay)
        self.fu = fu.fu(clock, fuDelay)
        self.reorderUnit = reorder.reorderUnit(clock, reorderDelay)
        self.writeBackUnit = writeBack.writeBackUnit(clock, writeBackDelay)

        self.pc = 0
        self.exitCode = False
        self.flush = False
        
        self.clock.process(fetchUnit.fetch())
        self.clock.process(decodeUnit.decode())
        self.clock.process(dispatchUnit.dispatch())
        self.clock.process(fu.execute())
        self.clock.process(reorderUnit.reorder())
        self.clock.process(writeBackUnit.writeBack())

        clock.run(until=1024)
if __name__ == '__main__':
    program = assembler(argv[1])
    p = processor(program.memory, program.regValues)
