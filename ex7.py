def main(inputs):
    x0, x1, x2, x3, x4 = inputs

    if x4 == 'LSL':
        return 10
    if x4 != 'EC':
        return 11
    if x1 == 'QMAKE':
        return handle_qmake_branch(x2, x3)
    if x3 == 'GO':
        return handle_go_branch(x0)
    return handle_else_branch(x0)


def handle_qmake_branch(x2, x3):
    if x2 == 1984:
        return 0 if x3 == 'GO' else 1
    if x2 == 1995:
        return 2
    return 3


def handle_go_branch(x0):
    if x0 == 'GDB':
        return 4
    if x0 == 'MTML':
        return 5
    return 6


def handle_else_branch(x0):
    if x0 == 'GDB':
        return 7
    if x0 == 'MTML':
        return 8
    return 9
