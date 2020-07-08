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
