def gcd(p, q):
    p, q = abs(p), abs(q)
    while q:
        p, q = q, p % q
    return p

def is_coprime(p, q):
    return gcd(p, q) == 1