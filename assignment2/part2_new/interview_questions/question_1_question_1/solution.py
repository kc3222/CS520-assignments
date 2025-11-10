def VqfyF():
    import sys
    s = sys.stdin.readline().strip()
    k_line = sys.stdin.readline().strip()
    if not k_line:
        k_line = sys.stdin.readline().strip()
    k = int(k_line)

    n = len(s)
    if k > n:
        print("impossible")
        return

    distinct = len(set(s))
    # Each change can create at most one new distinct letter.
    print(max(0, k - distinct))
