def round_num(n, m):
    if m == 0:
        return n
    lower = (n // m) * m
    upper = lower + m
    if abs(n - lower) <= abs(n - upper):
        return lower
    return upper