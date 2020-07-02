"""
Right away you get the sense you'll need some kind of recursion to handle this
problem. There's also probably some kind of math theory that explains how we
can solve this problem without having to re-invent the wheel.

Eventually, with a enough searching you'll probably find this:
https://en.wikipedia.org/wiki/Partition_(number_theory)#Odd_parts_and_distinct_parts

Which includes the example:

"Alternatively, we could count partitions in which no number occurs more than
once. Such a partition is called a partition with distinct parts. If we count
the partitions of 8 with distinct parts, we also obtain 6:"

    8
    7 + 1
    6 + 2
    5 + 3
    5 + 2 + 1
    4 + 3 + 1

Doing more searching led me to this website: http://oeis.org/
(The On-Line Encyclopedia of Integer Sequences (OEIS))

Where there is a perfect example of what we are trying to achieve:
http://oeis.org/A008289

There is also this very handy online calculator that can give you more test
case answers (just remember to minus one since the calculator always returns
the number itself as an option):
https://www.wolframalpha.com/input/?i=distinct+partitions+of+10

"""
import math


saved_results = {}


def solution(n):
    """Find the solution!

    Args:
        n: An integer from 3 to 200.

    Returns:
        The number of possible "staircase" combinations.
    """
    num_terms = int(math.floor((math.sqrt(8*n+1)-1)/2))

    result = 0
    for k in range(num_terms + 1):
        result += Q(n, k)

    # Minus 1 since our "staircase" must have 2 numbers
    return result - 1


def Q(n, k):
    """ http://oeis.org/A008289 """
    key = '{},{}'.format(n, k)
    result = 0

    # If already calculated this value, simply return the result
    if key in saved_results:
        return saved_results[key]

    if n < k or k < 1:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = Q(n-k, k) + Q(n-k, k-1)

    # Store the result for later
    saved_results[key] = result

    return result
