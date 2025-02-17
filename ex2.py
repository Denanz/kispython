import math


def main(x):
    if x < 41:
        return math.pow(math.sin(x), 7)
    elif 41 <= x < 125:
        return (
            math.pow(math.sqrt(x), 3)
            - ((54 + x + 88 * math.pow(x, 3)) / 31)
        )
    else:  # x >= 125
        return (
            54 * math.pow(math.ceil(94 * math.pow(x, 2) + (x / 25)), 7)
            + 62 * x
            + 13
        )
