import random


def bubble_sort(L: list[int]) -> None:
    for i in range(len(L) - 1):
        swapped = False
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swapped = True

        if not swapped:
            break


def selection_sort_min(L: list[int]) -> None:
    for i in range(len(L) - 1):
        min_idx = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_idx]:
                min_idx = j

        if i != min_idx:
            L[i], L[min_idx] = L[min_idx], L[i]


def selection_sort_max(L: list[int]) -> None:
    for i in range(len(L) - 1):
        max_idx = 0
        for j in range(1, len(L) - i):
            if L[j] > L[max_idx]:
                max_idx = j

        switch_idx = len(L) - 1 - i
        if switch_idx != max_idx:
            L[switch_idx], L[max_idx] = L[max_idx], L[switch_idx]


def insertion_sort_left(L: list[int]) -> None:
    for i in range(1, len(L)):
        while (L[i] < L[i - 1]) and (i > 0):
            L[i], L[i - 1] = L[i - 1], L[i]
            i -= 1


def insertion_sort_right(L: list[int]) -> None:
    for i in range(len(L) - 2, -1, -1):
        while (i < (len(L) - 1)) and (L[i] > L[i + 1]):
            L[i], L[i + 1] = L[i + 1], L[i]
            i += 1


def merge_sort(L: list[int]) -> None:
    if len(L) <= 1:
        return

    # Divide.
    mid_idx = len(L) // 2
    left = L[:mid_idx]
    right = L[mid_idx:]

    # Conquer.
    merge_sort(left)
    merge_sort(right)

    # Combine.
    i = 0
    j = 0
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            L[i + j] = left[i]
            i += 1
        else:
            L[i + j] = right[j]
            j += 1

    L[i + j :] = left[i:] + right[j:]


def quick_sort(L: list[int]) -> None:
    _quick_sort(L, left=0, right=len(L))


def _quick_sort(L: list[int], left: int, right: int) -> None:
    if left >= right:
        return

    # Divide.
    pivot = random.randint(left, right - 1)
    L[pivot], L[right - 1] = L[right - 1], L[pivot]

    pivot = right - 1
    i = left
    j = pivot - 1

    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while (i < j) and (L[j] >= L[pivot]):
            j -= 1

        if i < j:
            L[i], L[j] = L[j], L[i]

    if L[i] >= L[pivot]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    # Conquer.
    _quick_sort(L, left, pivot)
    _quick_sort(L, pivot + 1, right)


if __name__ == "__main__":
    for sort_func in [
        bubble_sort,
        selection_sort_min,
        selection_sort_max,
        insertion_sort_left,
        insertion_sort_right,
        merge_sort,
        quick_sort,
    ]:
        print(sort_func.__name__)
        L = [random.randint(0, 1_000) for i in range(10)]
        L_true = sorted(L)
        sort_func(L)
        assert L_true == L
