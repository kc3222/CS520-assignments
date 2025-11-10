# def num_position(text):
#     for i, ch in enumerate(text):
#         if ch.isdigit():
#             return i
#     return -1

def num_position(text):
    for i, ch in enumerate(text):
        if ch.isdigit():
            # BUG: Off-by-one error - returning 1-based index instead of 0-based
            # This is a common indexing mistake
            return i + 1
    return -1
