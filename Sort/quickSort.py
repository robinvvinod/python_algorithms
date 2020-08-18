# Time complexity
# Worst case --> O(n^2)
# Average case --> O(nlogn)


def quickSort(L):

    less = []
    more = []

    if len(L) < 2:
        return L

    pivot = L[0]

    for i in range(1, len(L)):
        if L[i] < pivot:
            less.append(L[i])
        else:
            more.append(L[i])

    return quickSort(less) + [pivot] + quickSort(more)


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high -= 1

        while low <= high and array[low] <= pivot:
            low += 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)
