def qs(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    return qs([x for x in L[1:] if x < pivot]) + [pivot] + qs(
        [x for x in L[1:] if x >= pivot])
