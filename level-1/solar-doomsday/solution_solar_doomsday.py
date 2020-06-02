import math


def solution(area):
    """Find the solution!

    Args:
        area: An integer representing a total area.

    Returns:
        A list of integers representing the solution.
    """
    result = []

    while (area > 0):
        # math.sqrt() will return a decimal
        # int() will remove the decimal (and will not round the value)
        square_root = int(math.sqrt(area))
        value = pow(square_root, 2)
        result.append(value)
        area -= value

    return result
