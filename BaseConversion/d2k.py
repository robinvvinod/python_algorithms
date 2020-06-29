def d2k(num, k):
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVQXYZ"
    result = ""
    while num > 0:
        digit = num % k
        result = str(mapping[digit]) + result
        num //= k
    return result
