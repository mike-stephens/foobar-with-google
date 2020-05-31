import math

def solution(area):
    result = []

    while (area > 0):
        square_root = int(math.sqrt(area))
        value = pow(square_root, 2)
        result.append(value)
        area -= value

    return result
