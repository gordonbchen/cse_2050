def sum_k(n):
    if n == 1:
        return 1
    return n + sum_k(n - 1)


print(sum_k(10))
