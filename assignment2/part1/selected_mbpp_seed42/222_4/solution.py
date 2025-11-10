def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    first_type = type(test_tuple[0])
    return all(type(element) == first_type for element in test_tuple)