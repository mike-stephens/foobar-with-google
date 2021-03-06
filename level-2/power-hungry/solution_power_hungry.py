"""
Could solve this without the initial .sort() by keeping track of odd number
of negative numbers and then dividing by the largest negative number.
Ex: In [-2, -3, -5] the "-2" is the largest negative number.
"""


def solution(xs):
    """Find the solution!

    Args:
        xs: A list of integer values.

    Returns:
        A number as a string representing the solution.
    """
    # Change [3, -1, 0, -5] into [-5, -1, 0, 3]
    xs.sort()

    result = 1

    count_neg = 0
    count_pos = 0
    count_zero = 0

    pending_neg = None

    for power in xs:
        if power < 0:
            count_neg += 1
            if pending_neg:
                result *= power * pending_neg
                pending_neg = None
            else:
                pending_neg = power
        elif power > 0:
            count_pos += 1
            result *= power
        else:
            count_zero += 1

    # If only 0s, return 0
    if len(xs) == count_zero:
        result = 0
    elif count_neg == 1:
        # If a single negative number, return negative number
        if len(xs) == count_neg:
            result = pending_neg
        # If a single negative number and 0s, return 0
        elif len(xs) == count_zero + count_neg:
            result = 0

    return str(result)
