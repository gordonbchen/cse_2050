def binary_search_iter(L: list[int], item: int) -> bool:
    """Use binary search to determine if the item is in the sorted list."""
    left = 0
    right = len(L)

    while left < right:
        mid = (left + right) // 2
        if item == L[mid]:
            return True
        elif item < L[mid]:
            right = mid
        else:
            left = mid + 1

    return False


def binary_search_recr(L: list[int], item: int) -> bool:
    """Use recursive binary search to determine if the item is in the sorted list."""
    return _binary_search_recr(L, item, left=0, right=len(L))


def _binary_search_recr(L: list[int], item: int, left: int, right: int) -> bool:
    """Use recursive binary search to determine if the item is in the sorted list."""
    if left >= right:
        return False

    mid = (left + right) // 2
    if item == L[mid]:
        return True
    elif item < L[mid]:
        return _binary_search_recr(L, item, left=0, right=mid)
    else:
        return _binary_search_recr(L, item, left=mid + 1, right=right)


def binary_search_index(L: list[int], item: int) -> int:
    """Use recursive binary search to find the index of the item in the list."""
    return _binary_search_index(L, item, left=0, right=len(L))


def _binary_search_index(L: list[int], item: int, left: int, right: int) -> int:
    """Use recursive binary search to find the index of the item in the list."""
    if left >= right:
        return -1

    mid = (left + right) // 2
    if item == L[mid]:
        return mid
    elif item < L[mid]:
        return _binary_search_index(L, item, left=0, right=mid)
    else:
        return _binary_search_index(L, item, left=mid + 1, right=right)


if __name__ == "__main__":
    print("Binary search iter")
    print(binary_search_iter([1, 2, 3, 4, 5, 6], -1))
    print(binary_search_iter([1, 2, 3, 4, 5, 6], 7))
    print(binary_search_iter([1, 2, 3, 4, 5, 6], 1))
    print(binary_search_iter([1, 2, 3, 4, 5, 6], 2))
    print(binary_search_iter([1, 2, 3, 4, 5, 6], 5))
    print(binary_search_iter([1, 2, 3, 4, 5, 6], 6))

    print("\nBinary search recur")
    print(binary_search_recr([1, 2, 3, 4, 5, 6], -1))
    print(binary_search_recr([1, 2, 3, 4, 5, 6], 7))
    print(binary_search_recr([1, 2, 3, 4, 5, 6], 1))
    print(binary_search_recr([1, 2, 3, 4, 5, 6], 2))
    print(binary_search_recr([1, 2, 3, 4, 5, 6], 5))
    print(binary_search_recr([1, 2, 3, 4, 5, 6], 6))

    print("\nBinary search index")
    print(binary_search_index([1, 2, 3, 4, 5, 6], -1))
    print(binary_search_index([1, 2, 3, 4, 5, 6], 7))
    print(binary_search_index([1, 2, 3, 4, 5, 6], 1))
    print(binary_search_index([1, 2, 3, 4, 5, 6], 2))
    print(binary_search_index([1, 2, 3, 4, 5, 6], 5))
    print(binary_search_index([1, 2, 3, 4, 5, 6], 6))
