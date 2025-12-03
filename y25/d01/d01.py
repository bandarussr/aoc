from utils import read_input

DIAL_START = 50
MOD = 100

def star1(test: bool=False) -> str:
    input = read_input(1, test)

    curr = DIAL_START
    num_zero = 0

    for line in input:
        pol = 1 if line[0] == 'R' else -1
        num = int(line[1:])

        curr = (curr + pol * num) % MOD

        if curr == 0:
            num_zero += 1

    return str(num_zero)

def star2(test: bool=False) -> str:
    input = read_input(1, test)
    return ""
