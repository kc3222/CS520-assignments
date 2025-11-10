import pytest
from solution import Solution


def test_largest_component_size():
    """Test Solution.largestComponentSize method."""
    sol = Solution()
    result = sol.largestComponentSize([4, 6, 15, 35])
    assert result == 4, f'Expected 4, got {result}'
