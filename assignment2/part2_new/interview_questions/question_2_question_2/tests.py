import pytest
from solution import Solution


def test_largest_component_size():
    """Test Solution.largestComponentSize method."""
    sol = Solution()
    result = sol.largestComponentSize([4, 6, 15, 35])
    assert result == 4, f'Expected 4, got {result}'


#iteration 1
def test_empty_list():
    """Test with empty list."""
    sol = Solution()
    result = sol.largestComponentSize([])
    assert result == 0, f'Expected 0, got {result}'


def test_single_element():
    """Test with single element."""
    sol = Solution()
    result = sol.largestComponentSize([7])
    assert result == 1, f'Expected 1, got {result}'


def test_two_elements_shared_factor():
    """Test with two elements sharing a factor."""
    sol = Solution()
    result = sol.largestComponentSize([4, 6])
    assert result == 2, f'Expected 2, got {result}'


def test_two_elements_no_shared_factor():
    """Test with two elements not sharing a factor."""
    sol = Solution()
    result = sol.largestComponentSize([3, 5])
    assert result == 1, f'Expected 1, got {result}'


def test_multiple_components():
    """Test with multiple components of different sizes."""
    sol = Solution()
    result = sol.largestComponentSize([20, 50, 9, 63])
    assert result == 2, f'Expected 2, got {result}'


def test_all_connected():
    """Test with all elements connected."""
    sol = Solution()
    result = sol.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39])
    assert result == 8, f'Expected 8, got {result}'


def test_prime_numbers():
    """Test with prime numbers."""
    sol = Solution()
    result = sol.largestComponentSize([2, 3, 5, 7, 11])
    assert result == 1, f'Expected 1, got {result}'


def test_large_numbers():
    """Test with larger numbers."""
    sol = Solution()
    result = sol.largestComponentSize([100, 200, 300, 400])
    assert result == 4, f'Expected 4, got {result}'


def test_powers_of_two():
    """Test with powers of two."""
    sol = Solution()
    result = sol.largestComponentSize([2, 4, 8, 16, 32])
    assert result == 5, f'Expected 5, got {result}'


def test_mixed_sizes():
    """Test with mixed component sizes."""
    sol = Solution()
    result = sol.largestComponentSize([2, 3, 4, 5, 6, 7, 8, 9])
    assert result == 6, f'Expected 6, got {result}'


def test_square_numbers():
    """Test with square numbers."""
    sol = Solution()
    result = sol.largestComponentSize([4, 9, 16, 25, 36])
    assert result == 4, f'Expected 4, got {result}'


def test_union_find_path_compression():
    """Test union-find path compression with deep trees."""
    sol = Solution()
    # Create a scenario that exercises path compression
    result = sol.largestComponentSize([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    assert result == 10, f'Expected 10, got {result}'


def test_size_comparison_in_union():
    """Test size comparison logic in union operation."""
    sol = Solution()
    # Create scenario where size[rx] < size[ry] to test the swap
    result = sol.largestComponentSize([3, 6, 9, 12, 15, 18, 21, 24])
    assert result == 8, f'Expected 8, got {result}'


def test_large_prime_factors():
    """Test with numbers having large prime factors."""
    sol = Solution()
    result = sol.largestComponentSize([97, 98, 99, 100])
    assert result == 2, f'Expected 2, got {result}'


def test_single_large_prime():
    """Test with a single large prime number."""
    sol = Solution()
    result = sol.largestComponentSize([9973])
    assert result == 1, f'Expected 1, got {result}'
