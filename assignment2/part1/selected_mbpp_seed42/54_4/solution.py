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