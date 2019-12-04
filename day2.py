def intComputer(input):
    instructionPointer = 0
    while instructionPointer < len(input):
        action = input[instructionPointer]
        if action == 99:
            break
        if action == 1:
            input[input[instructionPointer+3]] = input[input[instructionPointer+1]] + input[input[instructionPointer+2]]
            instructionPointer+=4
        elif action == 2:
            input[input[instructionPointer+3]] = input[input[instructionPointer+1]] * input[input[instructionPointer+2]]
            instructionPointer+=4
        else:
            break
    return input

def parse(lines):
    return list(map(int, lines[0].split(",")))
    
def solve(input, noun, verb):
    input[1] = noun
    input[2] = verb
    return intComputer(input)

