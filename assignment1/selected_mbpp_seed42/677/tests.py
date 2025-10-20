'''chatgpt'''
# Fail
'''cot'''
def validity_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

def validity_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

def validity_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

'''self-planning'''
def validity_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

def validity_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

def validity_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

'''claude'''
# Fail
'''cot'''
def validity_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

def validity_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

def validity_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

'''self-planning'''
def validity_triangle(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
    except (TypeError, ValueError):
        return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

def validity_triangle(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
    except (TypeError, ValueError):
        return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

def validity_triangle(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
    except (TypeError, ValueError):
        return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

assert validity_triangle(60,50,90)==False
assert validity_triangle(45,75,60)==True
assert validity_triangle(30,50,100)==True
assert validity_triangle(57, 45, 88) == False
assert validity_triangle(55, 54, 94) == False
assert validity_triangle(62, 45, 85) == False
assert validity_triangle(64, 45, 87) == False
assert validity_triangle(55, 50, 86) == False
assert validity_triangle(64, 55, 95) == False
assert validity_triangle(56, 55, 90) == False
assert validity_triangle(57, 47, 95) == False
assert validity_triangle(56, 53, 85) == False
assert validity_triangle(58, 52, 95) == False
assert validity_triangle(58, 45, 89) == False
assert validity_triangle(56, 51, 92) == False
assert validity_triangle(57, 49, 92) == False
assert validity_triangle(58, 51, 91) == False
assert validity_triangle(61, 51, 87) == False
assert validity_triangle(63, 53, 85) == False
assert validity_triangle(62, 45, 90) == False
assert validity_triangle(63, 51, 94) == False
assert validity_triangle(55, 46, 94) == False
assert validity_triangle(59, 45, 85) == False
assert validity_triangle(63, 54, 88) == False
assert validity_triangle(55, 49, 94) == False
assert validity_triangle(64, 55, 87) == False
assert validity_triangle(58, 48, 87) == False
assert validity_triangle(58, 46, 87) == False
assert validity_triangle(63, 48, 92) == False
assert validity_triangle(55, 55, 93) == False
assert validity_triangle(61, 49, 94) == False
assert validity_triangle(56, 54, 92) == False
assert validity_triangle(64, 54, 88) == False
assert validity_triangle(55, 54, 91) == False
assert validity_triangle(58, 45, 93) == False
assert validity_triangle(58, 52, 91) == False
assert validity_triangle(42, 70, 58) == False
assert validity_triangle(49, 78, 65) == False
assert validity_triangle(41, 70, 57) == False
assert validity_triangle(45, 73, 65) == False
assert validity_triangle(47, 74, 62) == False
assert validity_triangle(43, 73, 61) == False
assert validity_triangle(40, 79, 65) == False
assert validity_triangle(50, 74, 65) == False
assert validity_triangle(50, 78, 57) == False
assert validity_triangle(48, 77, 62) == False
assert validity_triangle(40, 70, 65) == False
assert validity_triangle(44, 70, 59) == False
assert validity_triangle(50, 75, 63) == False
assert validity_triangle(47, 80, 58) == False
assert validity_triangle(49, 77, 56) == False
assert validity_triangle(50, 73, 63) == False
assert validity_triangle(42, 75, 62) == False
assert validity_triangle(46, 80, 63) == False
assert validity_triangle(41, 80, 61) == False
assert validity_triangle(44, 74, 56) == False
assert validity_triangle(48, 78, 62) == False
assert validity_triangle(49, 72, 65) == False
assert validity_triangle(45, 71, 63) == False
assert validity_triangle(41, 71, 62) == False
assert validity_triangle(44, 73, 56) == False
assert validity_triangle(43, 73, 60) == False
assert validity_triangle(48, 75, 59) == False
assert validity_triangle(49, 74, 57) == True
assert validity_triangle(44, 78, 57) == False
assert validity_triangle(44, 73, 60) == False
assert validity_triangle(41, 73, 65) == False
assert validity_triangle(40, 79, 58) == False
assert validity_triangle(44, 77, 63) == False
assert validity_triangle(33, 46, 100) == False
assert validity_triangle(33, 50, 105) == False
assert validity_triangle(30, 54, 103) == False
assert validity_triangle(32, 50, 96) == False
assert validity_triangle(31, 52, 99) == False
assert validity_triangle(28, 48, 102) == False
assert validity_triangle(33, 51, 99) == False
assert validity_triangle(30, 49, 102) == False
assert validity_triangle(35, 53, 95) == False
assert validity_triangle(33, 46, 101) == True
assert validity_triangle(25, 46, 102) == False
assert validity_triangle(31, 55, 101) == False
assert validity_triangle(33, 54, 99) == False
assert validity_triangle(29, 48, 97) == False
assert validity_triangle(30, 50, 95) == False
assert validity_triangle(26, 49, 103) == False
assert validity_triangle(29, 53, 96) == False
assert validity_triangle(35, 48, 96) == False
assert validity_triangle(26, 47, 98) == False
assert validity_triangle(28, 55, 98) == False
assert validity_triangle(27, 47, 104) == False
assert validity_triangle(25, 49, 101) == False
assert validity_triangle(25, 54, 98) == False
assert validity_triangle(27, 45, 104) == False
assert validity_triangle(27, 46, 103) == False
assert validity_triangle(26, 48, 97) == False
assert validity_triangle(28, 54, 97) == False
assert validity_triangle(31, 53, 99) == False
assert validity_triangle(30, 50, 98) == False
assert validity_triangle(35, 49, 101) == False
assert validity_triangle(27, 47, 102) == False
assert validity_triangle(27, 47, 99) == False
assert validity_triangle(31, 52, 101) == False