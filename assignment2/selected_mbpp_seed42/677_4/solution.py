def validity_triangle(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
    except (TypeError, ValueError):
        return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a