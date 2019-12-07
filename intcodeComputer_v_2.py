from queue import SimpleQueue
from operator import add, mul


class Computer:
    def __init__(self, instructions):
        self.instructions = instructions[:]  # Cree une copie superficiel
        self.pc = 0  # instruction pointer
        self.inputs = SimpleQueue()

    def getParam(self, offset):
        instruction = str(self.instructions[self.pc])
        mode = 0
        if(len(instruction) > offset + 1):
            mode = int(instruction[len(instruction) - (offset + 2)])
        if mode == 0:
            return self.instructions[self.instructions[self.pc+offset]]
        else:
            return self.instructions[self.pc+offset]

    def getAction(self):
        return abs(self.instructions[self.pc]) % 100

    def eval(self):
        while self.pc < len(self.instructions):
            action = self.getAction()
            if action == 99:
                raise StopIteration
            if action == 1:
                # Add first two into three
                self.instructions[self.instructions[self.pc+3]
                                  ] = add(self.getParam(1), self.getParam(2))
                self.pc += 4
            elif action == 2:
                # Multiply first two into three
                self.instructions[self.instructions[self.pc+3]
                                  ] = mul(self.getParam(1), self.getParam(2))
                self.pc += 4
            elif action == 3:
                # set input at adress
                self.instructions[self.instructions[self.pc+1]
                                  ] = self.inputs.get()
                self.pc += 2
            elif action == 4:
                result = self.getParam(1)
                self.pc += 2
                return result
            elif action == 5:
                # jump-if-true
                condition = self.getParam(1)
                if condition != 0:
                    self.pc = self.getParam(2)
                else:
                    self.pc += 3
            elif action == 6:
                # jump-if-false
                condition = self.getParam(1)
                if condition == 0:
                    self.pc = self.getParam(2)
                else:
                    self.pc += 3
            elif action == 7:
                # less than
                if self.getParam(1) < self.getParam(2):
                    self.instructions[self.instructions[self.pc + 3]] = 1
                else:
                    self.instructions[self.instructions[self.pc + 3]] = 0
                self.pc += 4
            elif action == 8:
                # equals
                if self.getParam(1) == self.getParam(2):
                    self.instructions[self.instructions[self.pc + 3]] = 1
                else:
                    self.instructions[self.instructions[self.pc + 3]] = 0
                self.pc += 4
            else:
                raise RuntimeError(
                    f'bad opcode {action} at position {self.pc}')

    def put(self, obj):
        """Add an input to the queue"""
        self.inputs.put(obj)
