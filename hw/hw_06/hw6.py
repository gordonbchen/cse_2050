def swap(vals: list[int], i: int, j: int) -> None:
    """Swap vals[i] and vals[j] in place."""
    vals[i], vals[j] = vals[j], vals[i]


def bubble_sort(matrix: list[list[int]]) -> tuple[list[int], int]:
    """Bubble sort the first row. Return the sorted first row and # swaps."""
    vals = matrix[0]

    total_swaps = 0
    for i in range(len(vals) - 1):
        swaps = 0
        for j in range(len(vals) - 1):
            if vals[j] > vals[j + 1]:
                swap(vals, j, j + 1)
                swaps += 1

        if swaps == 0:
            break
        total_swaps += swaps

    return vals, total_swaps


def insertion_sort(matrix: list[list[int]]) -> tuple[list[int], int]:
    """Insertion sort the second row. Return the sorted second row and # swaps."""
    vals = matrix[1]

    total_swaps = 0
    for i in range(1, len(vals)):
        while (i > 0) and (vals[i] < vals[i - 1]):
            swap(vals, i, i - 1)
            i -= 1
            total_swaps += 1

    return vals, total_swaps


def selection_sort(matrix: list[list[int]]) -> tuple[list[int], int]:
    """Selection sort the third row. Return the sorted third row and # swaps."""
    vals = matrix[2]

    total_swaps = 0
    for i in range(len(vals) - 1):
        min_idx = i
        for j in range(i + 1, len(vals)):
            if vals[j] < vals[min_idx]:
                min_idx = j

        if min_idx != i:
            swap(vals, min_idx, i)
            total_swaps += 1

    return vals, total_swaps


def merge(
    first_row: list[int], second_row: list[int], third_row: list[int]
) -> list[int]:
    """
    Merges three sorted rows of the matrix into one sorted 1D list.

    Args:
        first_row: sorted 1st row.
        second_row: sorted 2nd row.
        third row: sorted 3rd row.

    Returns:
        sorted_list: All rows merged into a sorted 1D list.
    """
    sorted_list = []
    i = j = k = 0
    n = len(first_row)  # Since each row has the same number of elements

    while i < n or j < n or k < n:
        # Compare elements in each row, making sure to stay within bounds
        smallest = float("inf")
        target_row = 0

        if i < n and first_row[i] < smallest:
            smallest = first_row[i]
            target_row = 1
        if j < n and second_row[j] < smallest:
            smallest = second_row[j]
            target_row = 2
        if k < n and third_row[k] < smallest:
            smallest = third_row[k]
            target_row = 3

        # Add the smallest element to the merged list and move that index forward.
        if target_row == 1:
            sorted_list.append(first_row[i])
            i += 1
        elif target_row == 2:
            sorted_list.append(second_row[j])
            j += 1
        elif target_row == 3:
            sorted_list.append(third_row[k])
            k += 1

    return sorted_list


if __name__ == "__main__":
    # Example:
    matrix = [
        [10, 2, 3, 8, 1],  # First row (Bubble Sort)
        [7, 15, 14, 20, 9],  # Second row (Insertion Sort)
        [25, 12, 5, 3, 16],  # Third row (Selection Sort)
    ]

    # Step 1: Sort the first row using Bubble Sort
    sorted_1_bubble, bubble_swaps = bubble_sort(matrix)
    print("After Bubble Sort:", sorted_1_bubble, "Swaps:", bubble_swaps)

    # Step 2: Sort the second row using Insertion Sort
    sorted_2_insertion, insertion_swaps = insertion_sort(matrix)
    print("After Insertion Sort:", sorted_2_insertion, "Swaps:", insertion_swaps)

    # Step 3: Sort the third row using Selection Sort
    sorted_3_selection, selection_swaps = selection_sort(matrix)
    print("After Selection Sort:", sorted_3_selection, "Swaps:", selection_swaps)

    # Step 4: Merge the sorted rows into one sorted list
    merged_list = merge(sorted_1_bubble, sorted_2_insertion, sorted_3_selection)
    print("Merged List:", merged_list)
