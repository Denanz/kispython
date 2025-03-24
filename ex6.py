def main(A):

    N = {5 * i for i in A if not (-12 <= i)}

    M = {3 * i for i in A if not (i <= 58)}

    Theta = {abs(v) for v in N if (v > 85 or v <= -80)}

    Lambda = M.union(Theta)

    beta = abs(len(Theta) * len(Lambda)) + sum(lmbd % 2
                                               for lmbd in Lambda)

    return beta
