def count_down(n):
    print(n)

    if n >= 0:
        count_down(n - 1)


count_down(10)
