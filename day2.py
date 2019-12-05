import intcodeComputer

def parse(lines):
    return list(map(int, lines[0].split(",")))
    
def solve(input, noun, verb):
    input[1] = noun
    input[2] = verb
    return intcodeComputer.process(input)

