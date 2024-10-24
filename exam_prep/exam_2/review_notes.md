# Exam 2 Review Notes

## Mod 5: Recursion and Dynamic Programming
* Fibonacci without memoization: O(2^n), each call calls 2 more times, tree depth is n.
* Fibonacci with memoization: O(n)

## Mod 6: Searching and Sorting
* Binary search passing indicies (not slicing): O(logn), each call splits the list in half.

Quadratic soring algorithms
* Bubble sort: worst O(n^2), average O(n^2), best O(n)
    * Stable
    * After i iterations, last i items are sorted
    * Adaptive, keep track of if swapped
* Cocktail sort: worst O(n^2), average O(n^2), best O(n)
    * Bubbling both ways n//2 times.
* Selection sort: worst O(n^2), average O(n^2), best O(n^2)
    * O(n) swaps
    * Unstable
    * After i iterations, first i items are sorted
    * Not adaptive
* Insertion sort: worst O(n^2), average O(n^2), best O(n)
    * Stable
    * After i iterations, first i items are sorted relative to each other
    * Adaptive

* Timsort: worst O(nlogn), average O(nlogn), best O(n)

# Mod 7: Divide and Conquer
* Mergesort: worst O(nlogn), average O(nlogn), best O(nlogn)
    * log(n) depth b/c divides in half each time
    * O(n) to combine 2 sorted lists
    * Stable
    * Space complexity: O(n) b/c creates list copies in slicing
* Quicksort: worst O(n^2), average O(nlogn), best O(nlogn)
    * Worst case O(n^2) if choosing bad pivot (sorted or reverse sorted)
    * Best pivot = median
    * Can choose random pivot to avoid worst case O(n^2)
    * Unstable
