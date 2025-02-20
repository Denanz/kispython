import math


def main(m, n, y, b):
    # Вычисление первой части - двойная сумма
    sum1 = 0
    for j in range(1, n + 1):
        for k in range(1, m + 1):
            term = ((91 * (k ** 3) - j) ** 2) - 0.01 - (20 * (y ** 5))
            sum1 += term

    # Вычисление второй части - сумма произведений
    sum2 = 0
    for k in range(1, b + 1):
        product = 1
        for i in range(1, m + 1):
            product *= (72 * (k ** 14) - 640 * (i ** 3))
        sum2 += product

    return sum1 + sum2
