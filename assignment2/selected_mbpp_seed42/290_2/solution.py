def max_length(list1):
    lists = [x for x in list1 if isinstance(x, list)]
    if not lists:
        return []
    m = max(len(x) for x in lists)
    return [x for x in lists if len(x) == m]