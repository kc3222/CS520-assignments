def counting_sort(my_list):
    if not my_list:
        return []
    mn = min(my_list)
    mx = max(my_list)
    k = mx - mn + 1
    counts = [0] * k
    for x in my_list:
        counts[x - mn] += 1
    result = []
    for i, c in enumerate(counts):
        if c:
            result.extend([i + mn] * c)
    return result