from fib_memo import fib_default, fib_helper
import numpy as np
import timeit

SETUP_Code = """
from __main__ import k, fib_default, fib_helper
"""

STMT_fib_default = """
fib_default(k)
"""

STMT_fib_helper = """
fib_helper(k)
"""

UNIT_FACTOR = 1000
print("Times to find Fib(k). Each function is run 1000 times for each number.")
for k in range(10, 100, 10):
    # Setup lists to store values
    t_defaults = []
    t_helpers = []
    percents_slower = []

    # calculate fib(100) 1000 times, record the time
    for _ in range(100):
        t_defaults.append(
            UNIT_FACTOR
            * timeit.timeit(setup=SETUP_Code, stmt=STMT_fib_default, number=1000)
        )
        t_helpers.append(
            UNIT_FACTOR
            * timeit.timeit(setup=SETUP_Code, stmt=STMT_fib_helper, number=1000)
        )
        percents_slower.append(100 * (t_defaults[-1] - t_helpers[-1]) / t_helpers[-1])

    print(f"k={k}".center(50, "-"))
    print(f"{'':10}{'t_default':10}{'t_helper':10}{'Percent slower':20}")
    print(
        f"{'average':<10}{np.average(t_defaults):<10.3g}{np.average(t_helpers):<10.3g}{np.average(percents_slower):<10.3g}"
    )
    print(
        f"{'std':<10}{np.std(t_defaults):<10.3g}{np.std(t_helpers):<10.3g}{np.std(percents_slower):<10.3g}"
    )
    print()
