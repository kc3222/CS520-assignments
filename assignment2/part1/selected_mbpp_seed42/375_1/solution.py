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