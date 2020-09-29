def binarySearch(s, x):
    start = 0
    end = len(s) - 1
    while start <= end:
        mid = (start + end) // 2
        if x == s[mid]:
            return mid
        else:
            if x > s[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def binarySearchRecursive(s, start, end, x):
    if end >= start:
        mid = (start + end) // 2
        if s[mid] == x:
            return mid

        if s[mid] > x:
            return binarySearchRecursive(s, start, mid - 1, x)
        else:
            return binarySearchRecursive(s, mid + 1, end, x)

    else:
        return -1
