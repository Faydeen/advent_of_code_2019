import time

def read_file(day, section):
    with open(f"files/input_{day}_{section}.txt") as f:
        content = f.readlines()
    return [x.strip() for x in content]

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"\nTime required: {(time.time() - start_time)*1000:.2f} ms\n")
        return result
    return wrapper