def binary_search(L: list[int], target: int) -> int:
    return _binary_search(L, left=0, right=len(L), target=target)


def _binary_search(L: list[int], left: int, right: int, target: int) -> int:
    if left >= right:
        return -1

    mid = (left + right) // 2
    if L[mid] == target:
        return mid
    elif target > L[mid]:
        return _binary_search(L, mid + 1, right, target)
    else:
        return _binary_search(L, left, mid, target)


if __name__ == "__main__":
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in L:
        print(i, binary_search(L, i))

    print(-1, binary_search(L, -1))
    print(100, binary_search(L, 100))
