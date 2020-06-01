def solution(l):  # noqa: E741
    """Find the solution!

    Args:
        input_list: A list of string values.

    Returns:
        A list of string values sorted in ascending order.
    """
    l.sort(cmp=compare)
    return l


def compare(version1, version2):
    """Compare 2 version numbers (strings) for the .sort() comparison.

    Args:
        version1: A string similar to "0", "0.0" or "0.0.0".
        version2: A string similar to "0", "0.0" or "0.0.0".

    Returns:
        An integer of -1, 1 or 0 depending on the comparison result.
    """
    version1 = version1.split('.')
    version2 = version2.split('.')

    max_len = len(version1)
    if len(version2) > max_len:
        max_len = len(version2)

    for i in range(0, max_len):
        v1 = get_compare_value(version1, i)
        v2 = get_compare_value(version2, i)

        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1

    return 0


def get_compare_value(version, index):
    """Get an integer value from a list of strings and an index.

    Args:
        version: A list of one or more strings.
        index: An integer representing the list index to retrieve.

    Returns:
        An integer value from the list index or -1 if the index doesn't exist.
    """
    try:
        return int(version[index])
    except IndexError:
        return -1
