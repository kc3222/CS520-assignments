# Run 1: Pass
# def special_factorial(n):
#     if n < 0:
#         raise ValueError("n must be non-negative")
#     fact = 1
#     result = 1
#     for k in range(1, n + 1):
#         fact *= k
#         result *= fact
#     return result

# Run 2: Pass
# def special_factorial(n):
#     fact = 1
#     result = 1
#     for k in range(1, n + 1):
#         fact *= k
#         result *= fact
#     return result

# Run 3: Pass
def special_factorial(n):
    fact = 1
    result = 1
    for i in range(1, n + 1):
        fact *= i
        result *= fact
    return result

def check(candidate):

    # Check some simple cases
    assert candidate(4) == 288, "Test 4"
    assert candidate(5) == 34560, "Test 5"
    assert candidate(7) == 125411328000, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == 1, "Test 1"

check(special_factorial)