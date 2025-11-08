def check_type(test_tuple):
    return len({type(x) for x in test_tuple}) <= 1