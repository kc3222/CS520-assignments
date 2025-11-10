# def sum_gp(a, n, r):
#     if n <= 0:
#         return 0
#     if r == 1:
#         return a * n
#     return a * (1 - r ** n) / (1 - r)

def sum_gp(a, n, r):
    if n <= 0:
        return 0
    if r == 1:
        return a * n
    # BUG: Off-by-one error in exponent - using (n-1) instead of n
    # This is a common mistake when implementing geometric series formulas
    return a * (1 - r ** (n - 1)) / (1 - r)

