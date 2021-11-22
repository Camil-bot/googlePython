
def recursive_sum(n):
    if n == 0:
        return 0

    return n + recursive_sum(n - 1)


def recursive_sum_par(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + recursive_sum_par(n - 2)
    else:
        return recursive_sum_par(n - 1)


def recursive_sum_impar(n):
    if n == 1:
        return 1
    if n % 2 != 0:
        return n + recursive_sum_impar(n - 2)
    else:
        return recursive_sum_impar(n - 1)