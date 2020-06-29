# 7DE = (7 * 16^2) + (13 * 16^1) + (14 * 16^0) = 2014


def k2d(s, k):
    mapping = "0123456789ABCDEF"
    result = 0
    for i in range(len(s)):
        position = mapping.index(s[i])
        power = len(s) - i - 1
        result += position * (k**power)
    return result
