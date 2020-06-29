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
