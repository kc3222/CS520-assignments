def min_val(listval):
    numeric_values = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    if not numeric_values:
        return None
    return min(numeric_values)