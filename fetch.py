import simpy
class fetchUnit:
    def __init__(self,clock,fetchDelay):
        self.clock = clock
        self.fetchDelay = fetchDelay
        self.latch = 0
        self.valid = False
    def fetch(self,pc,memory):
        while True:
            temp = memory[pc]
            clock.timeout(self.fetchDelay)
            if self.valid == False:
                self.latch = temp
                self.valid = True