'''chatgpt'''
'''cot'''
# Run 1: Pass
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

# Run 2: Pass
def counting_sort(my_list):
    if not my_list:
        return []
    min_v = min(my_list)
    max_v = max(my_list)
    size = max_v - min_v + 1
    counts = [0] * size
    for v in my_list:
        counts[v - min_v] += 1
    result = []
    for i, c in enumerate(counts):
        if c:
            result.extend([i + min_v] * c)
    return result

# Run 3: Pass
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

'''self-planning'''
# Run 1: Pass
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

# Run 2: Pass
def counting_sort(my_list):
    if not my_list:
        return []
    min_v = min(my_list)
    max_v = max(my_list)
    counts = [0] * (max_v - min_v + 1)
    for v in my_list:
        counts[v - min_v] += 1
    result = []
    for i, c in enumerate(counts):
        result.extend([i + min_v] * c)
    return result

# Run 3: Pass
def counting_sort(my_list):
    if not my_list:
        return []
    min_v = min(my_list)
    max_v = max(my_list)
    count = [0] * (max_v - min_v + 1)
    for v in my_list:
        count[v - min_v] += 1
    output = [0] * len(my_list)
    idx = 0
    for i, c in enumerate(count):
        for _ in range(c):
            output[idx] = i + min_v
            idx += 1
    return output

'''claude'''
'''cot'''
# Run 1: Pass
def counting_sort(my_list):
    if not my_list:
        return my_list
    
    min_val = min(my_list)
    max_val = max(my_list)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    
    for num in my_list:
        count[num - min_val] += 1
    
    sorted_list = []
    for i in range(range_size):
        sorted_list.extend([i + min_val] * count[i])
    
    return sorted_list

# Run 2: Pass
def counting_sort(my_list):
    if not my_list:
        return my_list
    
    min_val = min(my_list)
    max_val = max(my_list)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    
    for num in my_list:
        count[num - min_val] += 1
    
    sorted_list = []
    for i in range(range_size):
        sorted_list.extend([i + min_val] * count[i])
    
    return sorted_list

# Run 3: Pass
def counting_sort(my_list):
    if not my_list:
        return my_list
    
    min_val = min(my_list)
    max_val = max(my_list)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    
    for num in my_list:
        count[num - min_val] += 1
    
    sorted_list = []
    for i in range(range_size):
        sorted_list.extend([i + min_val] * count[i])
    
    return sorted_list

'''self-planning'''
# Run 1: Pass
def counting_sort(my_list):
    if not my_list:
        return my_list
    
    min_val = min(my_list)
    max_val = max(my_list)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    
    for num in my_list:
        count[num - min_val] += 1
    
    sorted_list = []
    for i in range(range_size):
        sorted_list.extend([i + min_val] * count[i])
    
    return sorted_list

# Run 2: Pass
def counting_sort(my_list):
    if not my_list:
        return my_list
    
    min_val = min(my_list)
    max_val = max(my_list)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    
    for num in my_list:
        count[num - min_val] += 1
    
    sorted_list = []
    for i in range(range_size):
        sorted_list.extend([i + min_val] * count[i])
    
    return sorted_list

# Run 3: Pass
def counting_sort(my_list):
    if not my_list:
        return my_list
    
    min_val = min(my_list)
    max_val = max(my_list)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    
    for num in my_list:
        count[num - min_val] += 1
    
    sorted_list = []
    for i in range(range_size):
        sorted_list.extend([i + min_val] * count[i])
    
    return sorted_list

assert counting_sort([1,23,4,5,6,7,8]) == [1, 4, 5, 6, 7, 8, 23]
assert counting_sort([12, 9, 28, 33, 69, 45]) == [9, 12, 28, 33, 45, 69]
assert counting_sort([8, 4, 14, 3, 2, 1]) == [1, 2, 3, 4, 8, 14]
assert counting_sort([5, 18, 8, 3, 7, 11, 11]) == [3, 5, 7, 8, 11, 11, 18]
assert counting_sort([2, 23, 5, 7, 7, 9, 10]) == [2, 5, 7, 7, 9, 10, 23]
assert counting_sort([2, 23, 7, 4, 11, 12, 8]) == [2, 4, 7, 8, 11, 12, 23]
assert counting_sort([3, 26, 6, 9, 5, 12, 10]) == [3, 5, 6, 9, 10, 12, 26]
assert counting_sort([3, 27, 3, 7, 6, 9, 9]) == [3, 3, 6, 7, 9, 9, 27]
assert counting_sort([2, 18, 9, 10, 9, 12, 6]) == [2, 6, 9, 9, 10, 12, 18]
assert counting_sort([5, 24, 2, 8, 2, 8, 3]) == [2, 2, 3, 5, 8, 8, 24]
assert counting_sort([1, 21, 9, 7, 4, 5, 11]) == [1, 4, 5, 7, 9, 11, 21]
assert counting_sort([3, 19, 6, 5, 2, 5, 11]) == [2, 3, 5, 5, 6, 11, 19]
assert counting_sort([1, 22, 4, 9, 7, 4, 4]) == [1, 4, 4, 4, 7, 9, 22]
assert counting_sort([2, 21, 9, 4, 6, 3, 9]) == [2, 3, 4, 6, 9, 9, 21]
assert counting_sort([6, 25, 8, 2, 6, 10, 7]) == [2, 6, 6, 7, 8, 10, 25]
assert counting_sort([3, 26, 6, 8, 5, 2, 7]) == [2, 3, 5, 6, 7, 8, 26]
assert counting_sort([5, 18, 8, 2, 8, 3, 5]) == [2, 3, 5, 5, 8, 8, 18]
assert counting_sort([5, 22, 8, 3, 4, 12, 5]) == [3, 4, 5, 5, 8, 12, 22]
assert counting_sort([3, 20, 3, 8, 6, 10, 13]) == [3, 3, 6, 8, 10, 13, 20]
assert counting_sort([6, 23, 7, 1, 1, 10, 11]) == [1, 1, 6, 7, 10, 11, 23]
assert counting_sort([4, 28, 7, 3, 11, 12, 11]) == [3, 4, 7, 11, 11, 12, 28]
assert counting_sort([4, 28, 9, 3, 4, 4, 5]) == [3, 4, 4, 4, 5, 9, 28]
assert counting_sort([6, 24, 7, 1, 10, 11, 9]) == [1, 6, 7, 9, 10, 11, 24]
assert counting_sort([3, 23, 6, 1, 11, 11, 6]) == [1, 3, 6, 6, 11, 11, 23]
assert counting_sort([3, 18, 9, 8, 2, 2, 7]) == [2, 2, 3, 7, 8, 9, 18]
assert counting_sort([6, 21, 5, 4, 4, 9, 11]) == [4, 4, 5, 6, 9, 11, 21]
assert counting_sort([4, 21, 1, 7, 6, 5, 5]) == [1, 4, 5, 5, 6, 7, 21]
assert counting_sort([3, 21, 1, 6, 8, 4, 13]) == [1, 3, 4, 6, 8, 13, 21]
assert counting_sort([2, 23, 8, 9, 1, 6, 12]) == [1, 2, 6, 8, 9, 12, 23]
assert counting_sort([4, 19, 8, 9, 8, 11, 10]) == [4, 8, 8, 9, 10, 11, 19]
assert counting_sort([3, 27, 8, 5, 2, 6, 13]) == [2, 3, 5, 6, 8, 13, 27]
assert counting_sort([4, 20, 3, 7, 8, 10, 7]) == [3, 4, 7, 7, 8, 10, 20]
assert counting_sort([4, 28, 4, 9, 1, 12, 12]) == [1, 4, 4, 9, 12, 12, 28]
assert counting_sort([4, 22, 3, 4, 3, 10, 5]) == [3, 3, 4, 4, 5, 10, 22]
assert counting_sort([6, 20, 1, 5, 3, 9, 10]) == [1, 3, 5, 6, 9, 10, 20]
assert counting_sort([5, 24, 5, 10, 8, 12, 7]) == [5, 5, 7, 8, 10, 12, 24]
assert counting_sort([15, 7, 25, 28, 68, 46]) == [7, 15, 25, 28, 46, 68]
assert counting_sort([14, 10, 26, 30, 71, 41]) == [10, 14, 26, 30, 41, 71]
assert counting_sort([7, 6, 30, 38, 69, 45]) == [6, 7, 30, 38, 45, 69]
assert counting_sort([17, 13, 27, 28, 67, 40]) == [13, 17, 27, 28, 40, 67]
assert counting_sort([8, 4, 23, 29, 71, 42]) == [4, 8, 23, 29, 42, 71]
assert counting_sort([17, 6, 23, 38, 66, 50]) == [6, 17, 23, 38, 50, 66]
assert counting_sort([13, 12, 28, 32, 69, 44]) == [12, 13, 28, 32, 44, 69]
assert counting_sort([13, 13, 26, 37, 66, 41]) == [13, 13, 26, 37, 41, 66]
assert counting_sort([14, 12, 31, 34, 73, 50]) == [12, 14, 31, 34, 50, 73]
assert counting_sort([13, 6, 27, 29, 64, 42]) == [6, 13, 27, 29, 42, 64]
assert counting_sort([12, 13, 27, 32, 71, 40]) == [12, 13, 27, 32, 40, 71]
assert counting_sort([14, 5, 32, 36, 73, 47]) == [5, 14, 32, 36, 47, 73]
assert counting_sort([15, 7, 27, 34, 71, 42]) == [7, 15, 27, 34, 42, 71]
assert counting_sort([13, 8, 27, 35, 74, 44]) == [8, 13, 27, 35, 44, 74]
assert counting_sort([8, 9, 29, 30, 64, 44]) == [8, 9, 29, 30, 44, 64]
assert counting_sort([8, 10, 30, 32, 65, 41]) == [8, 10, 30, 32, 41, 65]
assert counting_sort([13, 8, 24, 30, 74, 47]) == [8, 13, 24, 30, 47, 74]
assert counting_sort([10, 6, 31, 38, 64, 48]) == [6, 10, 31, 38, 48, 64]
assert counting_sort([8, 13, 24, 28, 67, 45]) == [8, 13, 24, 28, 45, 67]
assert counting_sort([8, 8, 23, 30, 67, 42]) == [8, 8, 23, 30, 42, 67]
assert counting_sort([13, 11, 28, 38, 64, 42]) == [11, 13, 28, 38, 42, 64]
assert counting_sort([15, 13, 31, 29, 71, 48]) == [13, 15, 29, 31, 48, 71]
assert counting_sort([13, 14, 32, 29, 72, 44]) == [13, 14, 29, 32, 44, 72]
assert counting_sort([12, 10, 29, 32, 70, 47]) == [10, 12, 29, 32, 47, 70]
assert counting_sort([9, 8, 32, 35, 74, 49]) == [8, 9, 32, 35, 49, 74]
assert counting_sort([9, 11, 23, 30, 74, 43]) == [9, 11, 23, 30, 43, 74]
assert counting_sort([8, 12, 32, 33, 66, 42]) == [8, 12, 32, 33, 42, 66]
assert counting_sort([17, 14, 29, 32, 72, 45]) == [14, 17, 29, 32, 45, 72]
assert counting_sort([10, 14, 28, 31, 64, 50]) == [10, 14, 28, 31, 50, 64]
assert counting_sort([17, 7, 29, 38, 69, 48]) == [7, 17, 29, 38, 48, 69]
assert counting_sort([8, 9, 30, 38, 71, 50]) == [8, 9, 30, 38, 50, 71]
assert counting_sort([17, 13, 23, 37, 72, 46]) == [13, 17, 23, 37, 46, 72]
assert counting_sort([17, 10, 31, 33, 74, 50]) == [10, 17, 31, 33, 50, 74]
assert counting_sort([11, 1, 14, 4, 6, 2]) == [1, 2, 4, 6, 11, 14]
assert counting_sort([11, 6, 14, 5, 7, 2]) == [2, 5, 6, 7, 11, 14]
assert counting_sort([11, 1, 16, 1, 1, 6]) == [1, 1, 1, 6, 11, 16]
assert counting_sort([12, 2, 15, 8, 6, 4]) == [2, 4, 6, 8, 12, 15]
assert counting_sort([8, 8, 11, 3, 7, 4]) == [3, 4, 7, 8, 8, 11]
assert counting_sort([12, 5, 12, 1, 3, 3]) == [1, 3, 3, 5, 12, 12]
assert counting_sort([6, 8, 10, 4, 2, 3]) == [2, 3, 4, 6, 8, 10]
assert counting_sort([6, 9, 12, 3, 7, 1]) == [1, 3, 6, 7, 9, 12]
assert counting_sort([3, 4, 17, 8, 3, 3]) == [3, 3, 3, 4, 8, 17]
assert counting_sort([11, 9, 13, 5, 3, 6]) == [3, 5, 6, 9, 11, 13]
assert counting_sort([3, 9, 11, 4, 7, 4]) == [3, 4, 4, 7, 9, 11]
assert counting_sort([5, 7, 11, 8, 3, 4]) == [3, 4, 5, 7, 8, 11]
assert counting_sort([3, 9, 18, 4, 2, 5]) == [2, 3, 4, 5, 9, 18]
assert counting_sort([8, 8, 9, 8, 4, 5]) == [4, 5, 8, 8, 8, 9]
assert counting_sort([6, 6, 18, 3, 6, 1]) == [1, 3, 6, 6, 6, 18]
assert counting_sort([4, 5, 19, 4, 5, 6]) == [4, 4, 5, 5, 6, 19]
assert counting_sort([9, 6, 12, 8, 7, 3]) == [3, 6, 7, 8, 9, 12]
assert counting_sort([4, 1, 9, 5, 5, 1]) == [1, 1, 4, 5, 5, 9]
assert counting_sort([9, 5, 18, 1, 4, 2]) == [1, 2, 4, 5, 9, 18]
assert counting_sort([5, 7, 10, 3, 7, 3]) == [3, 3, 5, 7, 7, 10]
assert counting_sort([9, 5, 18, 5, 6, 2]) == [2, 5, 5, 6, 9, 18]
assert counting_sort([13, 3, 12, 4, 2, 5]) == [2, 3, 4, 5, 12, 13]
assert counting_sort([13, 3, 10, 1, 5, 3]) == [1, 3, 3, 5, 10, 13]
assert counting_sort([6, 7, 12, 6, 7, 1]) == [1, 6, 6, 7, 7, 12]
assert counting_sort([5, 8, 18, 7, 6, 5]) == [5, 5, 6, 7, 8, 18]
assert counting_sort([8, 3, 14, 4, 1, 3]) == [1, 3, 3, 4, 8, 14]
assert counting_sort([11, 7, 15, 4, 6, 3]) == [3, 4, 6, 7, 11, 15]
assert counting_sort([3, 5, 10, 2, 6, 2]) == [2, 2, 3, 5, 6, 10]
assert counting_sort([5, 5, 10, 7, 3, 5]) == [3, 5, 5, 5, 7, 10]
assert counting_sort([4, 5, 18, 6, 2, 6]) == [2, 4, 5, 6, 6, 18]
assert counting_sort([3, 8, 9, 2, 2, 1]) == [1, 2, 2, 3, 8, 9]
assert counting_sort([6, 2, 10, 5, 4, 3]) == [2, 3, 4, 5, 6, 10]
assert counting_sort([3, 7, 14, 2, 5, 4]) == [2, 3, 4, 5, 7, 14]