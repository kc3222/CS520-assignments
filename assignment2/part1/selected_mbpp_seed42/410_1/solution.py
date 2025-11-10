import math

def min_val(listval):
    m = None
    for x in listval:
        if isinstance(x, bool):
            continue
        if isinstance(x, (int, float)):
            if isinstance(x, float) and math.isnan(x):
                continue
            if m is None or x < m:
                m = x
    return m