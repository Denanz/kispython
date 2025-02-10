import math


def main(y, z):
    x1 = 70 * math.pow((math.pow(y, 3)) / 87 + z + math.pow(y, 2), 6)
    x2 = (54 + z + 88 * math.pow(z, 3)) / 31
    x3 = math.pow(math.sqrt(y), 3)
    x4 = 72 * math.pow(y + 49 * math.pow(y, 3) + 1, 3)
    x5 = math.pow(81 * math.pow(z, 3), 7) / 98
    x6 = x1 / (x3 - x2)
    x7 = x4 + x5

    return x6 - x7
