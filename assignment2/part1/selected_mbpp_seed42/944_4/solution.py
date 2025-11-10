def num_position(text):
    for i, char in enumerate(text):
        if char.isdigit():
            return i
    return -1