import time


def read_file(day, section):
    with open("files/input_"+day+"_"+section+".txt") as f:
        content = f.readlines()
    return [x.strip() for x in content]
