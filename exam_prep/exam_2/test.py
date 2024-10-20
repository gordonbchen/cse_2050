import random
import sys

random.seed(658)
sys.setrecursionlimit(1000000)


def foo(counter=0):
    """Generates random numbers until we get a 50"""
    # Track how many calls we've made
    counter += 1

    random_number = random.randint(1, 100)
    if random_number == 50:
        return

    foo(counter)


foo()
