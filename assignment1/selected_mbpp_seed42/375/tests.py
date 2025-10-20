'''chatgpt'''
'''cot'''
# def round_num(n, m):
# if m == 0:
# return n
# return round(n / m) * m

# def round_num(n, m):
# if m == 0:
# return n
# return round(n / m) * m

# def round_num(n, m):
# if m == 0:
# return n
# return round(n / m) * m

'''self-planning'''
# def round_num(n, m):
# if m == 0:
# return n
# return round(n / m) * m

# def round_num(n, m):
# if m == 0:
# return n
# return round(n / m) * m

# def round_num(n, m):
# if m == 0:
# return n
# return round(n / m) * m

'''claude'''
# Fail
'''cot'''
def round_num(n, m):
    if m == 0:
        return n
    return round(n / m) * m

def round_num(n, m):
    if m == 0:
        return n
    return round(n / m) * m

def round_num(n, m):
    if m == 0:
        return n
    return round(n / m) * m

'''self-planning'''
def round_num(n, m):
    if m == 0:
        return n
    return round(n / m) * m

def round_num(n, m):
    if m == 0:
        return n
    return round(n / m) * m

def round_num(n, m):
    if m == 0:
        return n
    return round(n / m) * m

'''Fixed by adding tests'''
'''chatgpt'''
def round_num(n, m):
    m_abs = abs(m)
    if m_abs == 0:
        return n
    r = n % m_abs
    down = n - r
    up = down + (0 if r == 0 else m_abs)
    if r > m_abs / 2:
        return up
    else:
        return down

'''claude'''
def round_num(n, m):
    if m == 0:
        return n
    lower = (n // m) * m
    upper = lower + m
    if abs(n - lower) <= abs(n - upper):
        return lower
    return upper

assert round_num(4722,10)==4720
assert round_num(1111,5)==1110
assert round_num(219,2)==218
assert round_num(5091, 9) == 5094
assert round_num(5326, 8) == 5328
assert round_num(5141, 11) == 5137
assert round_num(4194, 9) == 4194
assert round_num(4406, 9) == 4410
assert round_num(4821, 7) == 4823
assert round_num(4141, 13) == 4147
assert round_num(4945, 11) == 4950
assert round_num(5182, 6) == 5184
assert round_num(4787, 6) == 4788
assert round_num(4099, 12) == 4104
assert round_num(5152, 11) == 5148
assert round_num(5669, 13) == 5668
assert round_num(4550, 12) == 4548
assert round_num(4959, 7) == 4956
assert round_num(5318, 9) == 5319
assert round_num(4914, 11) == 4917
assert round_num(4006, 5) == 4005
assert round_num(4834, 14) == 4830
assert round_num(5003, 13) == 5005
assert round_num(4989, 15) == 4995
assert round_num(4787, 5) == 4785
assert round_num(5581, 15) == 5580
assert round_num(3947, 12) == 3948
assert round_num(5208, 6) == 5208
assert round_num(4300, 9) == 4302
assert round_num(4308, 14) == 4312
assert round_num(5583, 9) == 5580
assert round_num(3800, 9) == 3798
assert round_num(4179, 13) == 4173
assert round_num(3719, 15) == 3720
assert round_num(4335, 13) == 4329
assert round_num(4846, 15) == 4845
assert round_num(120, 4) == 120
assert round_num(2064, 9) == 2061
assert round_num(1603, 7) == 1603
assert round_num(1338, 6) == 1338
assert round_num(337, 8) == 336
assert round_num(1352, 5) == 1350
assert round_num(1713, 5) == 1715
assert round_num(1057, 10) == 1060
assert round_num(437, 7) == 434
assert round_num(1821, 6) == 1818
assert round_num(1486, 2) == 1486
assert round_num(1134, 4) == 1132
assert round_num(106, 9) == 108
assert round_num(1399, 9) == 1395
assert round_num(779, 2) == 778
assert round_num(890, 5) == 890
assert round_num(959, 6) == 960
assert round_num(1189, 6) == 1188
assert round_num(1587, 8) == 1584
assert round_num(657, 10) == 660
assert round_num(1804, 8) == 1800
assert round_num(1016, 9) == 1017
assert round_num(850, 4) == 848
assert round_num(1862, 10) == 1860
assert round_num(1860, 4) == 1860
assert round_num(488, 7) == 490
assert round_num(582, 10) == 580
assert round_num(375, 7) == 378
assert round_num(1624, 6) == 1626
assert round_num(908, 10) == 910
assert round_num(747, 2) == 746
assert round_num(1637, 7) == 1638
assert round_num(106, 10) == 110
assert round_num(215, 3) == 216
assert round_num(222, 6) == 222
assert round_num(219, 3) == 219
assert round_num(222, 1) == 222
assert round_num(219, 1) == 219
assert round_num(218, 4) == 216
assert round_num(221, 2) == 220
assert round_num(220, 2) == 220
assert round_num(214, 4) == 212
assert round_num(214, 5) == 215
assert round_num(223, 1) == 223
assert round_num(219, 3) == 219
assert round_num(221, 5) == 220
assert round_num(219, 1) == 219
assert round_num(218, 5) == 220
assert round_num(217, 3) == 216
assert round_num(221, 1) == 221
assert round_num(219, 2) == 218
assert round_num(223, 6) == 222
assert round_num(223, 2) == 222
assert round_num(217, 1) == 217
assert round_num(222, 6) == 222
assert round_num(216, 4) == 216
assert round_num(219, 4) == 220
assert round_num(221, 5) == 220
assert round_num(217, 4) == 216
assert round_num(222, 7) == 224
assert round_num(215, 6) == 216
assert round_num(215, 1) == 215
assert round_num(221, 3) == 222
assert round_num(217, 5) == 215
assert round_num(214, 2) == 214
assert round_num(216, 6) == 216