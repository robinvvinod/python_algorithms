def bubbleSort(L):
    for j in range(len(L) - 1):
        swap = False
        for i in range(len(L) - j - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                swap = True
        if not swap:
            break
    return L
