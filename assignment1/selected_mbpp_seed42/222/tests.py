'''chatgpt'''
'''cot'''
def check_type(test_tuple):
    return len({type(x) for x in test_tuple}) <= 1

def check_type(test_tuple):
    return len({type(x) for x in test_tuple}) <= 1

def check_type(test_tuple):
    return len({type(x) for x in test_tuple}) <= 1

'''self-planning'''
def check_type(test_tuple):
    return all(isinstance(x, type(test_tuple[0])) for x in test_tuple)

def check_type(test_tuple):
    return len({type(x) for x in test_tuple}) == 1 if test_tuple else True

def check_type(test_tuple):
    return all(isinstance(x, type(test_tuple[0])) for x in test_tuple)

'''claude'''
'''cot'''
def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    first_type = type(test_tuple[0])
    return all(type(element) == first_type for element in test_tuple)

def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    first_type = type(test_tuple[0])
    return all(type(element) == first_type for element in test_tuple)

def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    first_type = type(test_tuple[0])
    return all(type(element) == first_type for element in test_tuple)

'''self-planning'''
def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    first_type = type(test_tuple[0])
    return all(type(element) == first_type for element in test_tuple)

def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    first_type = type(test_tuple[0])
    return all(type(element) == first_type for element in test_tuple)

def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    first_type = type(test_tuple[0])
    return all(type(element) == first_type for element in test_tuple)

assert check_type((5, 6, 7, 3, 5, 6) ) == True
assert check_type((1, 2, "4") ) == False
assert check_type((3, 2, 1, 4, 5) ) == True
assert check_type((2, 1, 6, 2, 2, 3)) == True
assert check_type((1, 7, 9, 8, 8, 1)) == True
assert check_type((10, 11, 9, 2, 4, 3)) == True
assert check_type((9, 1, 6, 7, 4, 4)) == True
assert check_type((9, 9, 7, 4, 6, 3)) == True
assert check_type((2, 10, 9, 4, 1, 7)) == True
assert check_type((8, 9, 8, 2, 5, 5)) == True
assert check_type((5, 10, 6, 8, 7, 9)) == True
assert check_type((5, 5, 4, 1, 3, 6)) == True
assert check_type((5, 8, 10, 4, 7, 1)) == True
assert check_type((8, 9, 3, 5, 4, 1)) == True
assert check_type((9, 8, 5, 6, 10, 1)) == True
assert check_type((8, 5, 9, 8, 1, 5)) == True
assert check_type((1, 2, 3, 2, 3, 3)) == True
assert check_type((1, 2, 12, 7, 1, 10)) == True
assert check_type((8, 11, 12, 1, 5, 4)) == True
assert check_type((6, 1, 3, 2, 7, 8)) == True
assert check_type((7, 3, 11, 3, 2, 11)) == True
assert check_type((2, 1, 5, 5, 7, 3)) == True
assert check_type((8, 7, 8, 2, 2, 4)) == True
assert check_type((1, 3, 12, 8, 2, 3)) == True
assert check_type((3, 3, 4, 5, 6, 11)) == True
assert check_type((4, 3, 5, 6, 5, 9)) == True
assert check_type((3, 7, 3, 1, 4, 10)) == True
assert check_type((8, 10, 4, 2, 10, 1)) == True
assert check_type((4, 9, 8, 3, 7, 6)) == True
assert check_type((5, 2, 8, 8, 8, 2)) == True
assert check_type((10, 2, 6, 8, 10, 3)) == True
assert check_type((5, 6, 12, 7, 9, 11)) == True
assert check_type((2, 4, 8, 3, 1, 7)) == True
assert check_type((7, 3, 12, 4, 10, 6)) == True
assert check_type((5, 6, 4, 6, 3, 1)) == True
assert check_type((8, 3, 4, 7, 9, 4)) == True
assert check_type((6, 5, '3')) == False
assert check_type((6, 2, '0')) == False
assert check_type((5, 4, '3')) == False
assert check_type((3, 7, '5')) == False
assert check_type((2, 6, '6')) == False
assert check_type((4, 6, '0')) == False
assert check_type((5, 4, '3')) == False
assert check_type((5, 4, '1')) == False
assert check_type((1, 7, '0')) == False
assert check_type((3, 1, '5')) == False
assert check_type((4, 5, '7')) == False
assert check_type((6, 2, '3')) == False
assert check_type((6, 3, '4')) == False
assert check_type((4, 7, '3')) == False
assert check_type((5, 2, '4')) == False
assert check_type((2, 6, '3')) == False
assert check_type((2, 2, '8')) == False
assert check_type((3, 3, '4')) == False
assert check_type((1, 6, '4')) == False
assert check_type((4, 7, '3')) == False
assert check_type((2, 1, '6')) == False
assert check_type((3, 7, '3')) == False
assert check_type((3, 2, '6')) == False
assert check_type((4, 7, '7')) == False
assert check_type((2, 4, '9')) == False
assert check_type((3, 7, '0')) == False
assert check_type((6, 4, '6')) == False
assert check_type((2, 6, '5')) == False
assert check_type((2, 5, '0')) == False
assert check_type((3, 6, '9')) == False
assert check_type((6, 6, '3')) == False
assert check_type((4, 3, '3')) == False
assert check_type((6, 7, '5')) == False
assert check_type((1, 1, 3, 5, 7)) == True
assert check_type((4, 7, 2, 3, 7)) == True
assert check_type((1, 4, 2, 4, 6)) == True
assert check_type((5, 1, 2, 3, 10)) == True
assert check_type((1, 3, 2, 2, 2)) == True
assert check_type((8, 1, 2, 2, 6)) == True
assert check_type((3, 7, 1, 6, 5)) == True
assert check_type((5, 6, 1, 9, 10)) == True
assert check_type((5, 2, 1, 3, 6)) == True
assert check_type((5, 2, 4, 2, 3)) == True
assert check_type((3, 6, 4, 1, 5)) == True
assert check_type((8, 2, 3, 4, 1)) == True
assert check_type((8, 2, 1, 1, 9)) == True
assert check_type((8, 1, 4, 8, 1)) == True
assert check_type((5, 3, 2, 5, 7)) == True
assert check_type((4, 6, 6, 5, 9)) == True
assert check_type((6, 7, 2, 3, 1)) == True
assert check_type((6, 3, 2, 4, 5)) == True
assert check_type((7, 3, 2, 2, 1)) == True
assert check_type((3, 1, 4, 1, 3)) == True
assert check_type((2, 5, 6, 6, 8)) == True
assert check_type((3, 2, 3, 3, 7)) == True
assert check_type((3, 3, 5, 3, 3)) == True
assert check_type((7, 4, 5, 8, 3)) == True
assert check_type((3, 1, 5, 6, 7)) == True
assert check_type((8, 7, 5, 8, 6)) == True
assert check_type((4, 6, 5, 1, 10)) == True
assert check_type((1, 6, 2, 8, 8)) == True
assert check_type((8, 7, 4, 8, 6)) == True
assert check_type((5, 2, 4, 1, 2)) == True
assert check_type((4, 5, 6, 9, 4)) == True
assert check_type((1, 2, 5, 7, 1)) == True
assert check_type((7, 1, 5, 4, 6)) == True