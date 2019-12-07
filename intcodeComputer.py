def process(instructions, initInstructionPointer=0, inputs=[]):
    result = None
    instructionPointer = initInstructionPointer
    while instructionPointer < len(instructions):
        action = getAction(instructions, instructionPointer)
        if action == 99:
            break
        if action == 1:
            # Add first two into three
            instructions[instructions[instructionPointer+3]] = getParam(
                instructions, instructionPointer, 1) + getParam(instructions, instructionPointer, 2)
            instructionPointer += 4
        elif action == 2:
            # Multiply first two into three
            instructions[instructions[instructionPointer+3]] = getParam(
                instructions, instructionPointer, 1) * getParam(instructions, instructionPointer, 2)
            instructionPointer += 4
        elif action == 3:
            # set input at adress
            instructions[instructions[instructionPointer+1]] = inputs.pop(0)
            instructionPointer += 2
        elif action == 4:
            # print out
            result = getParam(instructions, instructionPointer, 1)
            instructionPointer += 2
            break
        elif action == 5:
            # jump-if-true
            condition = getParam(instructions, instructionPointer, 1)
            if condition != 0:
                instructionPointer = getParam(
                    instructions, instructionPointer, 2)
            else:
                instructionPointer += 3
        elif action == 6:
            # jump-if-false
            condition = getParam(instructions, instructionPointer, 1)
            if condition == 0:
                instructionPointer = getParam(
                    instructions, instructionPointer, 2)
            else:
                instructionPointer += 3
        elif action == 7:
            # less than
            if getParam(instructions, instructionPointer, 1) < getParam(instructions, instructionPointer, 2):
                instructions[instructions[instructionPointer + 3]] = 1
            else:
                instructions[instructions[instructionPointer + 3]] = 0
            instructionPointer += 4
        elif action == 8:
            # equals
            if getParam(instructions, instructionPointer, 1) == getParam(instructions, instructionPointer, 2):
                instructions[instructions[instructionPointer + 3]] = 1
            else:
                instructions[instructions[instructionPointer + 3]] = 0
            instructionPointer += 4
        else:
            raise RuntimeError(
                f'bad opcode {action} at position {instructionPointer}')
    return instructions, instructionPointer, inputs, result


def getParam(input, instructionPointer, offset):
    instruction = str(input[instructionPointer])
    mode = 0
    if(len(instruction) > offset + 1):
        mode = int(instruction[len(instruction) - (offset + 2)])
    if mode == 0:
        return input[input[instructionPointer+offset]]
    else:
        return input[instructionPointer+offset]


def getAction(input, instructionPointer):
    return abs(input[instructionPointer]) % 100
