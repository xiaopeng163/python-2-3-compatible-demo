"""
binary search
"""


def binary_search(l, n, t):
    """
    :param l: list of sorted integer
    :param n: the length of the list l
    :param t: the target number want to find
    """
    i = 0
    r = n - 1
    while i <= r:
        mid = (r + i) / 2
        if l[mid] == t:
            return mid
        elif l[mid] > t:
            r = mid - 1
        else:
            i = mid + 1
    return -1
