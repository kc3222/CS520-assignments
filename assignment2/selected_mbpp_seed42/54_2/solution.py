def counting_sort(my_list):
    if not my_list:
        return []
    min_v = min(my_list)
    max_v = max(my_list)
    k = max_v - min_v + 1
    counts = [0] * k
    for v in my_list:
        counts[v - min_v] += 1
    total = 0
    for i in range(k):
        total += counts[i]
        counts[i] = total
    output = [0] * len(my_list)
    for v in reversed(my_list):
        idx = v - min_v
        counts[idx] -= 1
        output[counts[idx]] = v
    return output
