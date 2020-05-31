def solution(xs):
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
            count_neg += 1
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
