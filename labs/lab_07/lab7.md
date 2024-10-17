# Mod 7 Lab: Which sorting algorithm is which?

Differentiate 5 sorting algorithms (`bubble`, `selection`, `insertion`, `merge`, and `quick`) based on how long they take to sort certain lists.

When you submit a file called `numbers.txt` to Gradescope, it will sort the numbers inside with these 5 algorithms, aliased as `alg_a`, `alg_b`, `alg_c`, `alg_d`, and `alg_e`:

```bash
================
n = 1000
----------------
alg    t (ms)    
----------------
alg_a  24.6      
alg_b  1.35      
alg_c  57        
alg_d  2.12      
alg_e  40.1      
----------------
```

You need to

1) Create lists of different *lengths* and *patterns*

2) Determine which alias corresponds to which sorting algorithm

## Answers

Write your answers in `answers.py`. It contains a dictionary where the keys are the aliased algorithms; you just need to enter the correct values ('bubble', 'selection', 'insertion', 'merge', or 'quick'):

```python
answers = {'alg_a': '', 'alg_b': '', 'alg_c': '', 'alg_d': '', 'alg_e': ''}
```

## Lab Notes

* `generate_numbers.py` contains code to automate the generation of `numbers.txt`.

* Each algorithm is used exactly once.

* The `bubble` and `insertion` sorts are adaptive - they can sort in O(n) in the best case.

* The quicksort algorithm always uses the last element in a sublist as the pivot.

* The largest list you can create is 2000 items due to resource constraints on Gradescope.

## Submitting

Submit by yourself or with a single group member (someone else in your lab section that you work with) by the due date (typically, Friday at 11:59 pm EST) to receive credit.

## Grading

This assignment is entirely auto-graded: 20 points per correct algorithm.