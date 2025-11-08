"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_counting_sort_1():
    """Test counting_sort case 1."""
    assert solution.counting_sort([1,23,4,5,6,7,8]) == [1, 4, 5, 6, 7, 8, 23]

def test_counting_sort_2():
    """Test counting_sort case 2."""
    assert solution.counting_sort([12, 9, 28, 33, 69, 45]) == [9, 12, 28, 33, 45, 69]

def test_counting_sort_3():
    """Test counting_sort case 3."""
    assert solution.counting_sort([8, 4, 14, 3, 2, 1]) == [1, 2, 3, 4, 8, 14]

def test_counting_sort_4():
    """Test counting_sort case 4."""
    assert solution.counting_sort([5, 18, 8, 3, 7, 11, 11]) == [3, 5, 7, 8, 11, 11, 18]

def test_counting_sort_5():
    """Test counting_sort case 5."""
    assert solution.counting_sort([2, 23, 5, 7, 7, 9, 10]) == [2, 5, 7, 7, 9, 10, 23]

def test_counting_sort_6():
    """Test counting_sort case 6."""
    assert solution.counting_sort([2, 23, 7, 4, 11, 12, 8]) == [2, 4, 7, 8, 11, 12, 23]

def test_counting_sort_7():
    """Test counting_sort case 7."""
    assert solution.counting_sort([3, 26, 6, 9, 5, 12, 10]) == [3, 5, 6, 9, 10, 12, 26]

def test_counting_sort_8():
    """Test counting_sort case 8."""
    assert solution.counting_sort([3, 27, 3, 7, 6, 9, 9]) == [3, 3, 6, 7, 9, 9, 27]

def test_counting_sort_9():
    """Test counting_sort case 9."""
    assert solution.counting_sort([2, 18, 9, 10, 9, 12, 6]) == [2, 6, 9, 9, 10, 12, 18]

def test_counting_sort_10():
    """Test counting_sort case 10."""
    assert solution.counting_sort([5, 24, 2, 8, 2, 8, 3]) == [2, 2, 3, 5, 8, 8, 24]

def test_counting_sort_11():
    """Test counting_sort case 11."""
    assert solution.counting_sort([1, 21, 9, 7, 4, 5, 11]) == [1, 4, 5, 7, 9, 11, 21]

def test_counting_sort_12():
    """Test counting_sort case 12."""
    assert solution.counting_sort([3, 19, 6, 5, 2, 5, 11]) == [2, 3, 5, 5, 6, 11, 19]

def test_counting_sort_13():
    """Test counting_sort case 13."""
    assert solution.counting_sort([1, 22, 4, 9, 7, 4, 4]) == [1, 4, 4, 4, 7, 9, 22]

def test_counting_sort_14():
    """Test counting_sort case 14."""
    assert solution.counting_sort([2, 21, 9, 4, 6, 3, 9]) == [2, 3, 4, 6, 9, 9, 21]

def test_counting_sort_15():
    """Test counting_sort case 15."""
    assert solution.counting_sort([6, 25, 8, 2, 6, 10, 7]) == [2, 6, 6, 7, 8, 10, 25]

def test_counting_sort_16():
    """Test counting_sort case 16."""
    assert solution.counting_sort([3, 26, 6, 8, 5, 2, 7]) == [2, 3, 5, 6, 7, 8, 26]

def test_counting_sort_17():
    """Test counting_sort case 17."""
    assert solution.counting_sort([5, 18, 8, 2, 8, 3, 5]) == [2, 3, 5, 5, 8, 8, 18]

def test_counting_sort_18():
    """Test counting_sort case 18."""
    assert solution.counting_sort([5, 22, 8, 3, 4, 12, 5]) == [3, 4, 5, 5, 8, 12, 22]

def test_counting_sort_19():
    """Test counting_sort case 19."""
    assert solution.counting_sort([3, 20, 3, 8, 6, 10, 13]) == [3, 3, 6, 8, 10, 13, 20]

def test_counting_sort_20():
    """Test counting_sort case 20."""
    assert solution.counting_sort([6, 23, 7, 1, 1, 10, 11]) == [1, 1, 6, 7, 10, 11, 23]

def test_counting_sort_21():
    """Test counting_sort case 21."""
    assert solution.counting_sort([4, 28, 7, 3, 11, 12, 11]) == [3, 4, 7, 11, 11, 12, 28]

def test_counting_sort_22():
    """Test counting_sort case 22."""
    assert solution.counting_sort([4, 28, 9, 3, 4, 4, 5]) == [3, 4, 4, 4, 5, 9, 28]

def test_counting_sort_23():
    """Test counting_sort case 23."""
    assert solution.counting_sort([6, 24, 7, 1, 10, 11, 9]) == [1, 6, 7, 9, 10, 11, 24]

def test_counting_sort_24():
    """Test counting_sort case 24."""
    assert solution.counting_sort([3, 23, 6, 1, 11, 11, 6]) == [1, 3, 6, 6, 11, 11, 23]

def test_counting_sort_25():
    """Test counting_sort case 25."""
    assert solution.counting_sort([3, 18, 9, 8, 2, 2, 7]) == [2, 2, 3, 7, 8, 9, 18]

def test_counting_sort_26():
    """Test counting_sort case 26."""
    assert solution.counting_sort([6, 21, 5, 4, 4, 9, 11]) == [4, 4, 5, 6, 9, 11, 21]

def test_counting_sort_27():
    """Test counting_sort case 27."""
    assert solution.counting_sort([4, 21, 1, 7, 6, 5, 5]) == [1, 4, 5, 5, 6, 7, 21]

def test_counting_sort_28():
    """Test counting_sort case 28."""
    assert solution.counting_sort([3, 21, 1, 6, 8, 4, 13]) == [1, 3, 4, 6, 8, 13, 21]

def test_counting_sort_29():
    """Test counting_sort case 29."""
    assert solution.counting_sort([2, 23, 8, 9, 1, 6, 12]) == [1, 2, 6, 8, 9, 12, 23]

def test_counting_sort_30():
    """Test counting_sort case 30."""
    assert solution.counting_sort([4, 19, 8, 9, 8, 11, 10]) == [4, 8, 8, 9, 10, 11, 19]

def test_counting_sort_31():
    """Test counting_sort case 31."""
    assert solution.counting_sort([3, 27, 8, 5, 2, 6, 13]) == [2, 3, 5, 6, 8, 13, 27]

def test_counting_sort_32():
    """Test counting_sort case 32."""
    assert solution.counting_sort([4, 20, 3, 7, 8, 10, 7]) == [3, 4, 7, 7, 8, 10, 20]

def test_counting_sort_33():
    """Test counting_sort case 33."""
    assert solution.counting_sort([4, 28, 4, 9, 1, 12, 12]) == [1, 4, 4, 9, 12, 12, 28]

def test_counting_sort_34():
    """Test counting_sort case 34."""
    assert solution.counting_sort([4, 22, 3, 4, 3, 10, 5]) == [3, 3, 4, 4, 5, 10, 22]

def test_counting_sort_35():
    """Test counting_sort case 35."""
    assert solution.counting_sort([6, 20, 1, 5, 3, 9, 10]) == [1, 3, 5, 6, 9, 10, 20]

def test_counting_sort_36():
    """Test counting_sort case 36."""
    assert solution.counting_sort([5, 24, 5, 10, 8, 12, 7]) == [5, 5, 7, 8, 10, 12, 24]

def test_counting_sort_37():
    """Test counting_sort case 37."""
    assert solution.counting_sort([15, 7, 25, 28, 68, 46]) == [7, 15, 25, 28, 46, 68]

def test_counting_sort_38():
    """Test counting_sort case 38."""
    assert solution.counting_sort([14, 10, 26, 30, 71, 41]) == [10, 14, 26, 30, 41, 71]

def test_counting_sort_39():
    """Test counting_sort case 39."""
    assert solution.counting_sort([7, 6, 30, 38, 69, 45]) == [6, 7, 30, 38, 45, 69]

def test_counting_sort_40():
    """Test counting_sort case 40."""
    assert solution.counting_sort([17, 13, 27, 28, 67, 40]) == [13, 17, 27, 28, 40, 67]

def test_counting_sort_41():
    """Test counting_sort case 41."""
    assert solution.counting_sort([8, 4, 23, 29, 71, 42]) == [4, 8, 23, 29, 42, 71]

def test_counting_sort_42():
    """Test counting_sort case 42."""
    assert solution.counting_sort([17, 6, 23, 38, 66, 50]) == [6, 17, 23, 38, 50, 66]

def test_counting_sort_43():
    """Test counting_sort case 43."""
    assert solution.counting_sort([13, 12, 28, 32, 69, 44]) == [12, 13, 28, 32, 44, 69]

def test_counting_sort_44():
    """Test counting_sort case 44."""
    assert solution.counting_sort([13, 13, 26, 37, 66, 41]) == [13, 13, 26, 37, 41, 66]

def test_counting_sort_45():
    """Test counting_sort case 45."""
    assert solution.counting_sort([14, 12, 31, 34, 73, 50]) == [12, 14, 31, 34, 50, 73]

def test_counting_sort_46():
    """Test counting_sort case 46."""
    assert solution.counting_sort([13, 6, 27, 29, 64, 42]) == [6, 13, 27, 29, 42, 64]

def test_counting_sort_47():
    """Test counting_sort case 47."""
    assert solution.counting_sort([12, 13, 27, 32, 71, 40]) == [12, 13, 27, 32, 40, 71]

def test_counting_sort_48():
    """Test counting_sort case 48."""
    assert solution.counting_sort([14, 5, 32, 36, 73, 47]) == [5, 14, 32, 36, 47, 73]

def test_counting_sort_49():
    """Test counting_sort case 49."""
    assert solution.counting_sort([15, 7, 27, 34, 71, 42]) == [7, 15, 27, 34, 42, 71]

def test_counting_sort_50():
    """Test counting_sort case 50."""
    assert solution.counting_sort([13, 8, 27, 35, 74, 44]) == [8, 13, 27, 35, 44, 74]

def test_counting_sort_51():
    """Test counting_sort case 51."""
    assert solution.counting_sort([8, 9, 29, 30, 64, 44]) == [8, 9, 29, 30, 44, 64]

def test_counting_sort_52():
    """Test counting_sort case 52."""
    assert solution.counting_sort([8, 10, 30, 32, 65, 41]) == [8, 10, 30, 32, 41, 65]

def test_counting_sort_53():
    """Test counting_sort case 53."""
    assert solution.counting_sort([13, 8, 24, 30, 74, 47]) == [8, 13, 24, 30, 47, 74]

def test_counting_sort_54():
    """Test counting_sort case 54."""
    assert solution.counting_sort([10, 6, 31, 38, 64, 48]) == [6, 10, 31, 38, 48, 64]

def test_counting_sort_55():
    """Test counting_sort case 55."""
    assert solution.counting_sort([8, 13, 24, 28, 67, 45]) == [8, 13, 24, 28, 45, 67]

def test_counting_sort_56():
    """Test counting_sort case 56."""
    assert solution.counting_sort([8, 8, 23, 30, 67, 42]) == [8, 8, 23, 30, 42, 67]

def test_counting_sort_57():
    """Test counting_sort case 57."""
    assert solution.counting_sort([13, 11, 28, 38, 64, 42]) == [11, 13, 28, 38, 42, 64]

def test_counting_sort_58():
    """Test counting_sort case 58."""
    assert solution.counting_sort([15, 13, 31, 29, 71, 48]) == [13, 15, 29, 31, 48, 71]

def test_counting_sort_59():
    """Test counting_sort case 59."""
    assert solution.counting_sort([13, 14, 32, 29, 72, 44]) == [13, 14, 29, 32, 44, 72]

def test_counting_sort_60():
    """Test counting_sort case 60."""
    assert solution.counting_sort([12, 10, 29, 32, 70, 47]) == [10, 12, 29, 32, 47, 70]

def test_counting_sort_61():
    """Test counting_sort case 61."""
    assert solution.counting_sort([9, 8, 32, 35, 74, 49]) == [8, 9, 32, 35, 49, 74]

def test_counting_sort_62():
    """Test counting_sort case 62."""
    assert solution.counting_sort([9, 11, 23, 30, 74, 43]) == [9, 11, 23, 30, 43, 74]

def test_counting_sort_63():
    """Test counting_sort case 63."""
    assert solution.counting_sort([8, 12, 32, 33, 66, 42]) == [8, 12, 32, 33, 42, 66]

def test_counting_sort_64():
    """Test counting_sort case 64."""
    assert solution.counting_sort([17, 14, 29, 32, 72, 45]) == [14, 17, 29, 32, 45, 72]

def test_counting_sort_65():
    """Test counting_sort case 65."""
    assert solution.counting_sort([10, 14, 28, 31, 64, 50]) == [10, 14, 28, 31, 50, 64]

def test_counting_sort_66():
    """Test counting_sort case 66."""
    assert solution.counting_sort([17, 7, 29, 38, 69, 48]) == [7, 17, 29, 38, 48, 69]

def test_counting_sort_67():
    """Test counting_sort case 67."""
    assert solution.counting_sort([8, 9, 30, 38, 71, 50]) == [8, 9, 30, 38, 50, 71]

def test_counting_sort_68():
    """Test counting_sort case 68."""
    assert solution.counting_sort([17, 13, 23, 37, 72, 46]) == [13, 17, 23, 37, 46, 72]

def test_counting_sort_69():
    """Test counting_sort case 69."""
    assert solution.counting_sort([17, 10, 31, 33, 74, 50]) == [10, 17, 31, 33, 50, 74]

def test_counting_sort_70():
    """Test counting_sort case 70."""
    assert solution.counting_sort([11, 1, 14, 4, 6, 2]) == [1, 2, 4, 6, 11, 14]

def test_counting_sort_71():
    """Test counting_sort case 71."""
    assert solution.counting_sort([11, 6, 14, 5, 7, 2]) == [2, 5, 6, 7, 11, 14]

def test_counting_sort_72():
    """Test counting_sort case 72."""
    assert solution.counting_sort([11, 1, 16, 1, 1, 6]) == [1, 1, 1, 6, 11, 16]

def test_counting_sort_73():
    """Test counting_sort case 73."""
    assert solution.counting_sort([12, 2, 15, 8, 6, 4]) == [2, 4, 6, 8, 12, 15]

def test_counting_sort_74():
    """Test counting_sort case 74."""
    assert solution.counting_sort([8, 8, 11, 3, 7, 4]) == [3, 4, 7, 8, 8, 11]

def test_counting_sort_75():
    """Test counting_sort case 75."""
    assert solution.counting_sort([12, 5, 12, 1, 3, 3]) == [1, 3, 3, 5, 12, 12]

def test_counting_sort_76():
    """Test counting_sort case 76."""
    assert solution.counting_sort([6, 8, 10, 4, 2, 3]) == [2, 3, 4, 6, 8, 10]

def test_counting_sort_77():
    """Test counting_sort case 77."""
    assert solution.counting_sort([6, 9, 12, 3, 7, 1]) == [1, 3, 6, 7, 9, 12]

def test_counting_sort_78():
    """Test counting_sort case 78."""
    assert solution.counting_sort([3, 4, 17, 8, 3, 3]) == [3, 3, 3, 4, 8, 17]

def test_counting_sort_79():
    """Test counting_sort case 79."""
    assert solution.counting_sort([11, 9, 13, 5, 3, 6]) == [3, 5, 6, 9, 11, 13]

def test_counting_sort_80():
    """Test counting_sort case 80."""
    assert solution.counting_sort([3, 9, 11, 4, 7, 4]) == [3, 4, 4, 7, 9, 11]

def test_counting_sort_81():
    """Test counting_sort case 81."""
    assert solution.counting_sort([5, 7, 11, 8, 3, 4]) == [3, 4, 5, 7, 8, 11]

def test_counting_sort_82():
    """Test counting_sort case 82."""
    assert solution.counting_sort([3, 9, 18, 4, 2, 5]) == [2, 3, 4, 5, 9, 18]

def test_counting_sort_83():
    """Test counting_sort case 83."""
    assert solution.counting_sort([8, 8, 9, 8, 4, 5]) == [4, 5, 8, 8, 8, 9]

def test_counting_sort_84():
    """Test counting_sort case 84."""
    assert solution.counting_sort([6, 6, 18, 3, 6, 1]) == [1, 3, 6, 6, 6, 18]

def test_counting_sort_85():
    """Test counting_sort case 85."""
    assert solution.counting_sort([4, 5, 19, 4, 5, 6]) == [4, 4, 5, 5, 6, 19]

def test_counting_sort_86():
    """Test counting_sort case 86."""
    assert solution.counting_sort([9, 6, 12, 8, 7, 3]) == [3, 6, 7, 8, 9, 12]

def test_counting_sort_87():
    """Test counting_sort case 87."""
    assert solution.counting_sort([4, 1, 9, 5, 5, 1]) == [1, 1, 4, 5, 5, 9]

def test_counting_sort_88():
    """Test counting_sort case 88."""
    assert solution.counting_sort([9, 5, 18, 1, 4, 2]) == [1, 2, 4, 5, 9, 18]

def test_counting_sort_89():
    """Test counting_sort case 89."""
    assert solution.counting_sort([5, 7, 10, 3, 7, 3]) == [3, 3, 5, 7, 7, 10]

def test_counting_sort_90():
    """Test counting_sort case 90."""
    assert solution.counting_sort([9, 5, 18, 5, 6, 2]) == [2, 5, 5, 6, 9, 18]

def test_counting_sort_91():
    """Test counting_sort case 91."""
    assert solution.counting_sort([13, 3, 12, 4, 2, 5]) == [2, 3, 4, 5, 12, 13]

def test_counting_sort_92():
    """Test counting_sort case 92."""
    assert solution.counting_sort([13, 3, 10, 1, 5, 3]) == [1, 3, 3, 5, 10, 13]

def test_counting_sort_93():
    """Test counting_sort case 93."""
    assert solution.counting_sort([6, 7, 12, 6, 7, 1]) == [1, 6, 6, 7, 7, 12]

def test_counting_sort_94():
    """Test counting_sort case 94."""
    assert solution.counting_sort([5, 8, 18, 7, 6, 5]) == [5, 5, 6, 7, 8, 18]

def test_counting_sort_95():
    """Test counting_sort case 95."""
    assert solution.counting_sort([8, 3, 14, 4, 1, 3]) == [1, 3, 3, 4, 8, 14]

def test_counting_sort_96():
    """Test counting_sort case 96."""
    assert solution.counting_sort([11, 7, 15, 4, 6, 3]) == [3, 4, 6, 7, 11, 15]

def test_counting_sort_97():
    """Test counting_sort case 97."""
    assert solution.counting_sort([3, 5, 10, 2, 6, 2]) == [2, 2, 3, 5, 6, 10]

def test_counting_sort_98():
    """Test counting_sort case 98."""
    assert solution.counting_sort([5, 5, 10, 7, 3, 5]) == [3, 5, 5, 5, 7, 10]

def test_counting_sort_99():
    """Test counting_sort case 99."""
    assert solution.counting_sort([4, 5, 18, 6, 2, 6]) == [2, 4, 5, 6, 6, 18]

def test_counting_sort_100():
    """Test counting_sort case 100."""
    assert solution.counting_sort([3, 8, 9, 2, 2, 1]) == [1, 2, 2, 3, 8, 9]

def test_counting_sort_101():
    """Test counting_sort case 101."""
    assert solution.counting_sort([6, 2, 10, 5, 4, 3]) == [2, 3, 4, 5, 6, 10]

def test_counting_sort_102():
    """Test counting_sort case 102."""
    assert solution.counting_sort([3, 7, 14, 2, 5, 4]) == [2, 3, 4, 5, 7, 14]
