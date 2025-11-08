"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_max_length_1():
    """Test max_length case 1."""
    assert solution.max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])

def test_max_length_2():
    """Test max_length case 2."""
    assert solution.max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])

def test_max_length_3():
    """Test max_length case 3."""
    assert solution.max_length([[5], [15,20,25]])==(3, [15,20,25])

def test_max_length_4():
    """Test max_length case 4."""
    assert solution.max_length([[3], [1, 6], [3, 8], [10, 7], [14, 14, 19]]) == (3, [14, 14, 19])

def test_max_length_5():
    """Test max_length case 5."""
    assert solution.max_length([[1], [2, 8], [2, 9], [8, 12], [12, 19, 13]]) == (3, [12, 19, 13])

def test_max_length_6():
    """Test max_length case 6."""
    assert solution.max_length([[3], [5, 6], [9, 4], [10, 11], [10, 17, 18]]) == (3, [10, 17, 18])

def test_max_length_7():
    """Test max_length case 7."""
    assert solution.max_length([[1], [2, 5], [10, 4], [13, 6], [10, 10, 21]]) == (3, [13, 6])

def test_max_length_8():
    """Test max_length case 8."""
    assert solution.max_length([[2], [4, 3], [6, 4], [11, 11], [9, 20, 18]]) == (3, [11, 11])

def test_max_length_9():
    """Test max_length case 9."""
    assert solution.max_length([[4], [1, 5], [4, 9], [4, 10], [14, 20, 13]]) == (3, [14, 20, 13])

def test_max_length_10():
    """Test max_length case 10."""
    assert solution.max_length([[5], [4, 5], [1, 10], [10, 11], [10, 15, 13]]) == (3, [10, 15, 13])

def test_max_length_11():
    """Test max_length case 11."""
    assert solution.max_length([[4], [4, 6], [9, 9], [5, 8], [9, 18, 19]]) == (3, [9, 18, 19])

def test_max_length_12():
    """Test max_length case 12."""
    assert solution.max_length([[4], [5, 3], [8, 8], [4, 16], [18, 14, 17]]) == (3, [18, 14, 17])

def test_max_length_13():
    """Test max_length case 13."""
    assert solution.max_length([[5], [1, 4], [7, 6], [9, 12], [17, 17, 17]]) == (3, [17, 17, 17])

def test_max_length_14():
    """Test max_length case 14."""
    assert solution.max_length([[1], [4, 2], [3, 3], [11, 12], [14, 11, 14]]) == (3, [14, 11, 14])

def test_max_length_15():
    """Test max_length case 15."""
    assert solution.max_length([[4], [5, 6], [7, 8], [8, 10], [16, 13, 20]]) == (3, [16, 13, 20])

def test_max_length_16():
    """Test max_length case 16."""
    assert solution.max_length([[3], [2, 7], [9, 7], [13, 16], [12, 17, 19]]) == (3, [13, 16])

def test_max_length_17():
    """Test max_length case 17."""
    assert solution.max_length([[3], [4, 3], [4, 5], [4, 12], [15, 18, 12]]) == (3, [15, 18, 12])

def test_max_length_18():
    """Test max_length case 18."""
    assert solution.max_length([[1], [4, 7], [1, 5], [9, 6], [14, 17, 22]]) == (3, [14, 17, 22])

def test_max_length_19():
    """Test max_length case 19."""
    assert solution.max_length([[4], [2, 1], [8, 12], [11, 8], [16, 20, 13]]) == (3, [16, 20, 13])

def test_max_length_20():
    """Test max_length case 20."""
    assert solution.max_length([[4], [4, 5], [6, 8], [14, 13], [9, 10, 18]]) == (3, [14, 13])

def test_max_length_21():
    """Test max_length case 21."""
    assert solution.max_length([[1], [5, 7], [4, 11], [9, 14], [13, 14, 21]]) == (3, [13, 14, 21])

def test_max_length_22():
    """Test max_length case 22."""
    assert solution.max_length([[2], [2, 8], [1, 9], [9, 8], [13, 10, 18]]) == (3, [13, 10, 18])

def test_max_length_23():
    """Test max_length case 23."""
    assert solution.max_length([[1], [1, 3], [9, 10], [14, 12], [15, 18, 12]]) == (3, [15, 18, 12])

def test_max_length_24():
    """Test max_length case 24."""
    assert solution.max_length([[5], [2, 4], [2, 4], [9, 8], [18, 16, 14]]) == (3, [18, 16, 14])

def test_max_length_25():
    """Test max_length case 25."""
    assert solution.max_length([[3], [3, 4], [5, 8], [4, 14], [18, 10, 14]]) == (3, [18, 10, 14])

def test_max_length_26():
    """Test max_length case 26."""
    assert solution.max_length([[4], [2, 8], [4, 12], [8, 13], [10, 18, 15]]) == (3, [10, 18, 15])

def test_max_length_27():
    """Test max_length case 27."""
    assert solution.max_length([[4], [1, 7], [6, 10], [13, 14], [15, 12, 17]]) == (3, [15, 12, 17])

def test_max_length_28():
    """Test max_length case 28."""
    assert solution.max_length([[1], [5, 4], [3, 12], [11, 13], [16, 14, 14]]) == (3, [16, 14, 14])

def test_max_length_29():
    """Test max_length case 29."""
    assert solution.max_length([[3], [4, 8], [7, 12], [8, 8], [16, 12, 17]]) == (3, [16, 12, 17])

def test_max_length_30():
    """Test max_length case 30."""
    assert solution.max_length([[3], [2, 2], [1, 9], [6, 15], [16, 10, 16]]) == (3, [16, 10, 16])

def test_max_length_31():
    """Test max_length case 31."""
    assert solution.max_length([[3], [4, 7], [9, 5], [6, 16], [18, 15, 15]]) == (3, [18, 15, 15])

def test_max_length_32():
    """Test max_length case 32."""
    assert solution.max_length([[4], [6, 2], [3, 5], [13, 10], [18, 12, 14]]) == (3, [18, 12, 14])

def test_max_length_33():
    """Test max_length case 33."""
    assert solution.max_length([[2], [2, 4], [5, 11], [9, 16], [13, 19, 15]]) == (3, [13, 19, 15])

def test_max_length_34():
    """Test max_length case 34."""
    assert solution.max_length([[5], [3, 2], [6, 9], [12, 14], [15, 12, 12]]) == (3, [15, 12, 12])

def test_max_length_35():
    """Test max_length case 35."""
    assert solution.max_length([[3], [5, 2], [2, 10], [13, 6], [12, 14, 15]]) == (3, [13, 6])

def test_max_length_36():
    """Test max_length case 36."""
    assert solution.max_length([[4], [6, 6], [3, 8], [13, 9], [8, 20, 15]]) == (3, [13, 9])

def test_max_length_37():
    """Test max_length case 37."""
    assert solution.max_length([[6], [1, 7], [15, 9, 17, 19]]) == (4, [15, 9, 17, 19])

def test_max_length_38():
    """Test max_length case 38."""
    assert solution.max_length([[6], [10, 9], [12, 13, 16, 17]]) == (4, [12, 13, 16, 17])

def test_max_length_39():
    """Test max_length case 39."""
    assert solution.max_length([[5], [6, 4], [7, 13, 14, 19]]) == (4, [7, 13, 14, 19])

def test_max_length_40():
    """Test max_length case 40."""
    assert solution.max_length([[6], [1, 11], [6, 17, 11, 20]]) == (4, [6, 17, 11, 20])

def test_max_length_41():
    """Test max_length case 41."""
    assert solution.max_length([[3], [10, 4], [10, 13, 15, 19]]) == (4, [10, 13, 15, 19])

def test_max_length_42():
    """Test max_length case 42."""
    assert solution.max_length([[6], [6, 11], [7, 17, 14, 14]]) == (4, [7, 17, 14, 14])

def test_max_length_43():
    """Test max_length case 43."""
    assert solution.max_length([[4], [6, 11], [9, 15, 17, 13]]) == (4, [9, 15, 17, 13])

def test_max_length_44():
    """Test max_length case 44."""
    assert solution.max_length([[6], [6, 10], [14, 14, 16, 13]]) == (4, [14, 14, 16, 13])

def test_max_length_45():
    """Test max_length case 45."""
    assert solution.max_length([[5], [1, 9], [11, 11, 10, 16]]) == (4, [11, 11, 10, 16])

def test_max_length_46():
    """Test max_length case 46."""
    assert solution.max_length([[2], [10, 11], [9, 8, 17, 10]]) == (4, [10, 11])

def test_max_length_47():
    """Test max_length case 47."""
    assert solution.max_length([[2], [1, 6], [7, 17, 9, 16]]) == (4, [7, 17, 9, 16])

def test_max_length_48():
    """Test max_length case 48."""
    assert solution.max_length([[5], [3, 4], [7, 14, 13, 11]]) == (4, [7, 14, 13, 11])

def test_max_length_49():
    """Test max_length case 49."""
    assert solution.max_length([[3], [7, 9], [15, 15, 16, 20]]) == (4, [15, 15, 16, 20])

def test_max_length_50():
    """Test max_length case 50."""
    assert solution.max_length([[3], [2, 6], [9, 14, 11, 15]]) == (4, [9, 14, 11, 15])

def test_max_length_51():
    """Test max_length case 51."""
    assert solution.max_length([[3], [10, 9], [8, 8, 17, 18]]) == (4, [10, 9])

def test_max_length_52():
    """Test max_length case 52."""
    assert solution.max_length([[6], [1, 7], [10, 16, 10, 15]]) == (4, [10, 16, 10, 15])

def test_max_length_53():
    """Test max_length case 53."""
    assert solution.max_length([[3], [7, 7], [12, 14, 9, 17]]) == (4, [12, 14, 9, 17])

def test_max_length_54():
    """Test max_length case 54."""
    assert solution.max_length([[1], [3, 12], [5, 13, 17, 16]]) == (4, [5, 13, 17, 16])

def test_max_length_55():
    """Test max_length case 55."""
    assert solution.max_length([[4], [7, 3], [9, 15, 9, 18]]) == (4, [9, 15, 9, 18])

def test_max_length_56():
    """Test max_length case 56."""
    assert solution.max_length([[4], [7, 3], [12, 16, 10, 10]]) == (4, [12, 16, 10, 10])

def test_max_length_57():
    """Test max_length case 57."""
    assert solution.max_length([[5], [1, 8], [9, 7, 9, 20]]) == (4, [9, 7, 9, 20])

def test_max_length_58():
    """Test max_length case 58."""
    assert solution.max_length([[2], [8, 6], [7, 12, 10, 16]]) == (4, [8, 6])

def test_max_length_59():
    """Test max_length case 59."""
    assert solution.max_length([[2], [4, 8], [10, 14, 10, 19]]) == (4, [10, 14, 10, 19])

def test_max_length_60():
    """Test max_length case 60."""
    assert solution.max_length([[6], [4, 3], [6, 11, 15, 12]]) == (4, [6, 11, 15, 12])

def test_max_length_61():
    """Test max_length case 61."""
    assert solution.max_length([[1], [1, 12], [12, 16, 9, 16]]) == (4, [12, 16, 9, 16])

def test_max_length_62():
    """Test max_length case 62."""
    assert solution.max_length([[3], [8, 4], [10, 14, 18, 15]]) == (4, [10, 14, 18, 15])

def test_max_length_63():
    """Test max_length case 63."""
    assert solution.max_length([[1], [10, 3], [6, 9, 12, 10]]) == (4, [10, 3])

def test_max_length_64():
    """Test max_length case 64."""
    assert solution.max_length([[1], [1, 10], [14, 12, 13, 14]]) == (4, [14, 12, 13, 14])

def test_max_length_65():
    """Test max_length case 65."""
    assert solution.max_length([[3], [2, 8], [14, 16, 12, 10]]) == (4, [14, 16, 12, 10])

def test_max_length_66():
    """Test max_length case 66."""
    assert solution.max_length([[2], [4, 5], [8, 11, 10, 19]]) == (4, [8, 11, 10, 19])

def test_max_length_67():
    """Test max_length case 67."""
    assert solution.max_length([[4], [10, 12], [13, 10, 18, 12]]) == (4, [13, 10, 18, 12])

def test_max_length_68():
    """Test max_length case 68."""
    assert solution.max_length([[4], [3, 6], [10, 11, 9, 13]]) == (4, [10, 11, 9, 13])

def test_max_length_69():
    """Test max_length case 69."""
    assert solution.max_length([[4], [3, 2], [8, 11, 10, 18]]) == (4, [8, 11, 10, 18])

def test_max_length_70():
    """Test max_length case 70."""
    assert solution.max_length([[3], [16, 21, 21]]) == (3, [16, 21, 21])

def test_max_length_71():
    """Test max_length case 71."""
    assert solution.max_length([[5], [17, 20, 30]]) == (3, [17, 20, 30])

def test_max_length_72():
    """Test max_length case 72."""
    assert solution.max_length([[2], [17, 21, 23]]) == (3, [17, 21, 23])

def test_max_length_73():
    """Test max_length case 73."""
    assert solution.max_length([[9], [14, 15, 22]]) == (3, [14, 15, 22])

def test_max_length_74():
    """Test max_length case 74."""
    assert solution.max_length([[10], [15, 25, 30]]) == (3, [15, 25, 30])

def test_max_length_75():
    """Test max_length case 75."""
    assert solution.max_length([[8], [19, 15, 27]]) == (3, [19, 15, 27])

def test_max_length_76():
    """Test max_length case 76."""
    assert solution.max_length([[4], [15, 21, 20]]) == (3, [15, 21, 20])

def test_max_length_77():
    """Test max_length case 77."""
    assert solution.max_length([[1], [16, 16, 30]]) == (3, [16, 16, 30])

def test_max_length_78():
    """Test max_length case 78."""
    assert solution.max_length([[7], [15, 23, 22]]) == (3, [15, 23, 22])

def test_max_length_79():
    """Test max_length case 79."""
    assert solution.max_length([[8], [17, 20, 28]]) == (3, [17, 20, 28])

def test_max_length_80():
    """Test max_length case 80."""
    assert solution.max_length([[7], [10, 23, 30]]) == (3, [10, 23, 30])

def test_max_length_81():
    """Test max_length case 81."""
    assert solution.max_length([[6], [10, 21, 28]]) == (3, [10, 21, 28])

def test_max_length_82():
    """Test max_length case 82."""
    assert solution.max_length([[2], [12, 21, 26]]) == (3, [12, 21, 26])

def test_max_length_83():
    """Test max_length case 83."""
    assert solution.max_length([[3], [17, 25, 26]]) == (3, [17, 25, 26])

def test_max_length_84():
    """Test max_length case 84."""
    assert solution.max_length([[4], [12, 19, 29]]) == (3, [12, 19, 29])

def test_max_length_85():
    """Test max_length case 85."""
    assert solution.max_length([[3], [15, 23, 26]]) == (3, [15, 23, 26])

def test_max_length_86():
    """Test max_length case 86."""
    assert solution.max_length([[6], [14, 15, 26]]) == (3, [14, 15, 26])

def test_max_length_87():
    """Test max_length case 87."""
    assert solution.max_length([[6], [17, 18, 27]]) == (3, [17, 18, 27])

def test_max_length_88():
    """Test max_length case 88."""
    assert solution.max_length([[4], [16, 18, 20]]) == (3, [16, 18, 20])

def test_max_length_89():
    """Test max_length case 89."""
    assert solution.max_length([[1], [13, 17, 20]]) == (3, [13, 17, 20])

def test_max_length_90():
    """Test max_length case 90."""
    assert solution.max_length([[5], [18, 24, 21]]) == (3, [18, 24, 21])

def test_max_length_91():
    """Test max_length case 91."""
    assert solution.max_length([[2], [18, 24, 24]]) == (3, [18, 24, 24])

def test_max_length_92():
    """Test max_length case 92."""
    assert solution.max_length([[8], [10, 22, 24]]) == (3, [10, 22, 24])

def test_max_length_93():
    """Test max_length case 93."""
    assert solution.max_length([[9], [12, 22, 26]]) == (3, [12, 22, 26])

def test_max_length_94():
    """Test max_length case 94."""
    assert solution.max_length([[10], [10, 23, 20]]) == (3, [10, 23, 20])

def test_max_length_95():
    """Test max_length case 95."""
    assert solution.max_length([[6], [20, 17, 25]]) == (3, [20, 17, 25])

def test_max_length_96():
    """Test max_length case 96."""
    assert solution.max_length([[2], [16, 22, 30]]) == (3, [16, 22, 30])

def test_max_length_97():
    """Test max_length case 97."""
    assert solution.max_length([[4], [10, 24, 23]]) == (3, [10, 24, 23])

def test_max_length_98():
    """Test max_length case 98."""
    assert solution.max_length([[6], [14, 25, 20]]) == (3, [14, 25, 20])

def test_max_length_99():
    """Test max_length case 99."""
    assert solution.max_length([[7], [11, 20, 25]]) == (3, [11, 20, 25])

def test_max_length_100():
    """Test max_length case 100."""
    assert solution.max_length([[4], [20, 16, 30]]) == (3, [20, 16, 30])

def test_max_length_101():
    """Test max_length case 101."""
    assert solution.max_length([[7], [19, 20, 20]]) == (3, [19, 20, 20])

def test_max_length_102():
    """Test max_length case 102."""
    assert solution.max_length([[5], [13, 18, 29]]) == (3, [13, 18, 29])
