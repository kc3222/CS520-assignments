'''chatgpt'''
'''cot'''
def is_coprime(a, b):
    a, b = abs(int(a)), abs(int(b))
    if a == 0 and b == 0:
        return False
    while b:
        a, b = b, a % b
    return a == 1

def is_coprime(a, b):
    a, b = abs(int(a)), abs(int(b))
    if a == 0 and b == 0:
        return False
    while b:
        a, b = b, a % b
    return a == 1

def is_coprime(a, b):
    a, b = abs(int(a)), abs(int(b))
    if a == 0 and b == 0:
        return False
    while b:
        a, b = b, a % b
    return a == 1

'''self-planning'''
def is_coprime(a, b):
    a, b = abs(int(a)), abs(int(b))
    if a == 0 and b == 0:
        return False
    while b:
        a, b = b, a % b
    return a == 1

def is_coprime(p, q):
    while q:
        p, q = q, p % q
    return abs(p) == 1

def is_coprime(p, q):
    a, b = abs(p), abs(q)
    while b:
        a, b = b, a % b
    return a == 1

'''claude'''
'''cot'''
def gcd(p, q):
    p, q = abs(p), abs(q)
    while q:
        p, q = q, p % q
    return p

def is_coprime(p, q):
    return gcd(p, q) == 1

def gcd(p, q):
    p, q = abs(p), abs(q)
    while q:
        p, q = q, p % q
    return p

def is_coprime(p, q):
    return gcd(p, q) == 1

def gcd(p, q):
    p, q = abs(p), abs(q)
    while q:
        p, q = q, p % q
    return p

def is_coprime(p, q):
    return gcd(p, q) == 1

'''self-planning'''
def gcd(p, q):
    p, q = abs(p), abs(q)
    while q:
        p, q = q, p % q
    return p

def is_coprime(p, q):
    return gcd(p, q) == 1

def gcd(p, q):
    p, q = abs(p), abs(q)
    while q:
        p, q = q, p % q
    return p

def is_coprime(p, q):
    return gcd(p, q) == 1

def gcd(p, q):
    p, q = abs(p), abs(q)
    while q:
        p, q = q, p % q
    return p

def is_coprime(p, q):
    return gcd(p, q) == 1

assert is_coprime(17,13) == True
assert is_coprime(15,21) == False
assert is_coprime(25,45) == False
assert is_coprime(14, 12) == False
assert is_coprime(18, 8) == False
assert is_coprime(17, 14) == True
assert is_coprime(17, 15) == True
assert is_coprime(12, 17) == True
assert is_coprime(17, 13) == True
assert is_coprime(13, 18) == True
assert is_coprime(12, 11) == True
assert is_coprime(18, 10) == False
assert is_coprime(16, 11) == True
assert is_coprime(13, 12) == True
assert is_coprime(15, 13) == True
assert is_coprime(13, 17) == True
assert is_coprime(19, 17) == True
assert is_coprime(14, 9) == True
assert is_coprime(15, 10) == False
assert is_coprime(15, 9) == False
assert is_coprime(15, 9) == False
assert is_coprime(15, 13) == True
assert is_coprime(13, 13) == False
assert is_coprime(21, 12) == False
assert is_coprime(16, 14) == False
assert is_coprime(22, 14) == False
assert is_coprime(14, 8) == False
assert is_coprime(16, 17) == True
assert is_coprime(13, 8) == True
assert is_coprime(16, 11) == True
assert is_coprime(16, 16) == False
assert is_coprime(15, 15) == False
assert is_coprime(20, 12) == False
assert is_coprime(16, 14) == False
assert is_coprime(12, 10) == False
assert is_coprime(16, 17) == True
assert is_coprime(16, 25) == True
assert is_coprime(15, 21) == False
assert is_coprime(17, 26) == True
assert is_coprime(20, 16) == False
assert is_coprime(18, 18) == False
assert is_coprime(17, 23) == True
assert is_coprime(18, 24) == False
assert is_coprime(14, 16) == False
assert is_coprime(10, 18) == False
assert is_coprime(14, 26) == False
assert is_coprime(12, 21) == False
assert is_coprime(13, 20) == True
assert is_coprime(18, 18) == False
assert is_coprime(17, 16) == True
assert is_coprime(11, 18) == True
assert is_coprime(16, 24) == False
assert is_coprime(16, 21) == True
assert is_coprime(19, 21) == True
assert is_coprime(16, 18) == False
assert is_coprime(13, 19) == True
assert is_coprime(11, 17) == True
assert is_coprime(14, 23) == True
assert is_coprime(10, 17) == True
assert is_coprime(16, 21) == True
assert is_coprime(18, 23) == True
assert is_coprime(15, 16) == True
assert is_coprime(14, 17) == True
assert is_coprime(10, 18) == False
assert is_coprime(12, 17) == True
assert is_coprime(20, 21) == True
assert is_coprime(17, 17) == False
assert is_coprime(18, 24) == False
assert is_coprime(15, 25) == False
assert is_coprime(22, 40) == False
assert is_coprime(24, 41) == True
assert is_coprime(24, 44) == False
assert is_coprime(21, 50) == True
assert is_coprime(23, 47) == True
assert is_coprime(21, 46) == True
assert is_coprime(27, 48) == False
assert is_coprime(27, 47) == True
assert is_coprime(27, 46) == True
assert is_coprime(22, 41) == True
assert is_coprime(22, 45) == True
assert is_coprime(25, 41) == True
assert is_coprime(22, 40) == False
assert is_coprime(23, 45) == True
assert is_coprime(20, 41) == True
assert is_coprime(20, 45) == False
assert is_coprime(29, 47) == True
assert is_coprime(27, 41) == True
assert is_coprime(20, 49) == True
assert is_coprime(24, 44) == False
assert is_coprime(22, 48) == False
assert is_coprime(28, 46) == False
assert is_coprime(26, 44) == False
assert is_coprime(24, 41) == True
assert is_coprime(27, 41) == True
assert is_coprime(23, 43) == True
assert is_coprime(22, 50) == False
assert is_coprime(28, 43) == True
assert is_coprime(24, 44) == False
assert is_coprime(25, 44) == True
assert is_coprime(21, 40) == True
assert is_coprime(21, 40) == True
assert is_coprime(25, 42) == True