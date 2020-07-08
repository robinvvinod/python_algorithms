# Time complexity
# Worst case --> O(nlogn)
# Average case --> O(nlogn)


def merge(l, r):
    i = 0
    j = 0
    res = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        elif l[i] > r[j]:
            res.append(r[j])
            j += 1

    while i < len(l):
        res.append(l[i])
        i += 1

    while j < len(r):
        res.append(r[j])
        j += 1

    return res


def mergeSort(arr):
    L = len(arr)
    if L <= 1:
        return arr

    mid = int(L / 2)
    l = mergeSort(arr[:mid])
    r = mergeSort(arr[mid:])
    return merge(l, r)
