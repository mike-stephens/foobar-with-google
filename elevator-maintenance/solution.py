def solution(l):
    l.sort(cmp=compare)
    return l


def compare(version1, version2):
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
    try:
        return int(version[index])
    except IndexError:
        return -1
