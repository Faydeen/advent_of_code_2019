from queue import SimpleQueue
from operator import add, mul


class Computer:
    def __init__(self, instructions, pc=0, rb=0):
        # Init memory
        self.memory = [0 for i in range(5000)]
        # Cree une copie superficiel
        self.memory[:len(instructions)-1] = instructions[:]
        self.pc = pc  # instruction pointer
        self.rb = rb  # Relative base pointer
        self.inputs = SimpleQueue()
        self.isWaitingForInput = False

    def clear(self):
        while self.inputs.empty() == False:
            self.inputs.get()

    def get_addr_param(self, offset):
        instruction = str(self.memory[self.pc])
        mode = 0
        if(len(instruction) > offset + 1):
            mode = int(instruction[len(instruction) - (offset + 2)])
        if mode == 0:
            return self.memory[self.pc+offset]
        elif mode == 1:
            return self.pc+offset
        elif mode == 2:
            return self.rb + self.memory[self.pc+offset]
        else:
            raise RuntimeError(
                f'bad mode {mode} at position {self.pc}')

    def get_param(self, offset):
        return self.memory[self.get_addr_param(offset)]

    def write_value(self, offset, value):
        self.memory[self.get_addr_param(offset)] = value

    def getAction(self):
        return abs(self.memory[self.pc]) % 100

    def eval(self):
        """Add an input to the queue"""
        while self.pc < len(self.memory):
            action = self.getAction()
            if action == 99:
                raise StopIteration
            if action == 1:
                """ Add first two into three """
                self.write_value(3, add(self.get_param(1), self.get_param(2)))
                self.pc += 4
            elif action == 2:
                """ Multiply first two into three"""
                self.write_value(3, mul(self.get_param(1), self.get_param(2)))
                self.pc += 4
            elif action == 3:
                """set input at adress"""
                self.isWaitingForInput = True
                self.write_value(1, self.inputs.get())
                self.isWaitingForInput = False
                self.pc += 2
            elif action == 4:
                result = self.get_param(1)
                self.pc += 2
                return result
            elif action == 5:
                """ jump-if-true """
                condition = self.get_param(1)
                if condition != 0:
                    self.pc = self.get_param(2)
                else:
                    self.pc += 3
            elif action == 6:
                """ jump-if-false """
                condition = self.get_param(1)
                if condition == 0:
                    self.pc = self.get_param(2)
                else:
                    self.pc += 3
            elif action == 7:
                """ less than """
                if self.get_param(1) < self.get_param(2):
                    self.write_value(3, 1)
                else:
                    self.write_value(3, 0)
                self.pc += 4
            elif action == 8:
                """ equals """
                if self.get_param(1) == self.get_param(2):
                    self.write_value(3, 1)
                else:
                    self.write_value(3, 0)
                self.pc += 4
            elif action == 9:
                """ Relative base update """
                self.rb = self.rb + self.get_param(1)
                self.pc += 2
            else:
                raise RuntimeError(
                    f'bad opcode {action} at position {self.pc}')

    def put(self, obj):
        """Add an input to the queue"""
        self.inputs.put(obj)
