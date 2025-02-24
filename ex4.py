import math


def main(n):
    if n == 0:
        return 0.53
    else:
        prev = main(n-1)
        return prev + math.pow(math.cos(prev), 3) + 57
