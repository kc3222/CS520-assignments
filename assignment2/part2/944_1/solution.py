def num_position(text):
    for i, ch in enumerate(text):
        if ch.isdigit():
            return i
    return -1