import random

# Max is 2000 due to memory constraints on gradescope containers
n = 1000

# Bubble: n best case, n^2 worst case.
# Selection: n^2 best and worst case.
# Insertion: n best case, n^2 worst case.
# Merge: nlog(n) sort.
# Quick: nlog(n) sort for random pivots. n^2 sort for sorted.

# Find merge and quicksort.
# Will be fastest algos.
# L = [random.randint(0, n) for i in range(n)]
# ================
# n = 1000
# ----------------
# alg    t (ms)
# ----------------
# alg_a  28.9
# alg_b  1.51  QUICKSORT or MERGESORT
# alg_c  65.6
# alg_d  2.36  QUICKSORT or MERGESORT
# alg_e  47.7
# ----------------
# alg_b and alg_d are merge and quicksort.

# Differentiate merge and quicksort (and selection sort).
# L = list(range(n))
# ================
# n = 1000
# ----------------
# alg    t (ms)
# ----------------
# alg_a  58.9  SELECTIONSORT
# alg_b  76.4  QUICKSORT
# alg_c  0.141
# alg_d  3.52  MERGESORT
# alg_e  0.661
# ----------------
# alg_b is quick sort.
# alg_d is merge sort.
# alg_a is selection sort.

# Test with few out of order.
# L = list(range(n))
# L[500] = 100
# ================
# n = 1000
# ----------------
# alg    t (ms)
# ----------------
# alg_a  34.8  SELECTIONSORT
# alg_b  38.5  QUICKSORT
# alg_c  27  BUBBLESORT
# alg_d  1.77  MERGESORT
# alg_e  0.402  INSERTIONSORT
# ----------------
# alg_c is bubble sort.
# alg_e is insertion sort.


with open("./numbers.txt", mode="w") as f:
    for item in L:
        f.write(str(item))
        f.write(" ")
