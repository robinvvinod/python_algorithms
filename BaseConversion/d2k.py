def d2k(num, k):
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVQXYZ"
    res = ""
    while num > 0:
        digit = num % k
        res += str(mapping[digit])
        num //= k
    return res
