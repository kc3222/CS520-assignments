def min_val(listval):
    numeric_values = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return min(numeric_values) if numeric_values else None