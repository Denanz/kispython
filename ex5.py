def main(x, y, z):
    n = len(x)  # Длина вектора n определяется по x
    result = sum(
        21 * (x[n - i] ** 3 + 79 * z[n - i] ** 2 + y[n - i]) ** 2
        for i in range(1, n + 1)
    )
    return result
