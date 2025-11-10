def check_type(test_tuple):
    return all(isinstance(x, type(test_tuple[0])) for x in test_tuple)