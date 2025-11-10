def is_coprime(a, b):
    a, b = abs(int(a)), abs(int(b))
    if a == 0 and b == 0:
        return False
    while b:
        a, b = b, a % b
    return a == 1