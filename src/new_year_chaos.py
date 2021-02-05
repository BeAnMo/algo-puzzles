#!/bin/python3
import math
import os
import random
import re
import sys

"""
From Hackerrank
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

Test cases in stdin
2 (t = number of cases)
5 (n = size of queue)
2 1 5 3 4 (queue)
0 (answer, number of moves)
5 (n = size of queue)
2 5 1 3 4 (queue)
Too chaotic (answer)
"""

# Complete the minimumBribes function below.


def minimumBribes(q):
    moves = 0

    for i, actual in enumerate(q):
        # queue starts at 1 not 0.
        # This is the number seen
        # in the ordered queue.
        expected = i + 1

        if actual - expected > 2:
            print("Too chaotic")
            return None

        elif actual != expected:
            # Looks at queue elements starting at
            # 2 before actual (1 before becomes 2 becomes of 1-based index)
            # and iterates until 1 before expected.
            # e.g. [2, 1]
            # actual = 2, expected = 1
            # for j in range(max(0, 0), 0)
            # 2 > 2 ? no -> no moves
            # for j in range(max(0, -1), 1)
            # 2 > 1 ? yes -> moves += 1
            for j in range(max(0, actual - 2), i):
                if q[j] > actual:
                    moves += 1

    print(moves)


if __name__ == "__main__":
    q0 = [2, 1, 5, 3, 4]
    a0 = 3
    q1 = [2, 5, 1, 3, 4]
    q1 = "Too chaotic"

    minimumBribes(q0)