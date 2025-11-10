"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_validity_triangle_1():
    """Test validity_triangle case 1."""
    assert solution.validity_triangle(60,50,90)==False

def test_validity_triangle_2():
    """Test validity_triangle case 2."""
    assert solution.validity_triangle(45,75,60)==True

def test_validity_triangle_3():
    """Test validity_triangle case 3."""
    assert solution.validity_triangle(30,50,100)==True

def test_validity_triangle_4():
    """Test validity_triangle case 4."""
    assert solution.validity_triangle(57, 45, 88) == False

def test_validity_triangle_5():
    """Test validity_triangle case 5."""
    assert solution.validity_triangle(55, 54, 94) == False

def test_validity_triangle_6():
    """Test validity_triangle case 6."""
    assert solution.validity_triangle(62, 45, 85) == False

def test_validity_triangle_7():
    """Test validity_triangle case 7."""
    assert solution.validity_triangle(64, 45, 87) == False

def test_validity_triangle_8():
    """Test validity_triangle case 8."""
    assert solution.validity_triangle(55, 50, 86) == False

def test_validity_triangle_9():
    """Test validity_triangle case 9."""
    assert solution.validity_triangle(64, 55, 95) == False

def test_validity_triangle_10():
    """Test validity_triangle case 10."""
    assert solution.validity_triangle(56, 55, 90) == False

def test_validity_triangle_11():
    """Test validity_triangle case 11."""
    assert solution.validity_triangle(57, 47, 95) == False

def test_validity_triangle_12():
    """Test validity_triangle case 12."""
    assert solution.validity_triangle(56, 53, 85) == False

def test_validity_triangle_13():
    """Test validity_triangle case 13."""
    assert solution.validity_triangle(58, 52, 95) == False

def test_validity_triangle_14():
    """Test validity_triangle case 14."""
    assert solution.validity_triangle(58, 45, 89) == False

def test_validity_triangle_15():
    """Test validity_triangle case 15."""
    assert solution.validity_triangle(56, 51, 92) == False

def test_validity_triangle_16():
    """Test validity_triangle case 16."""
    assert solution.validity_triangle(57, 49, 92) == False

def test_validity_triangle_17():
    """Test validity_triangle case 17."""
    assert solution.validity_triangle(58, 51, 91) == False

def test_validity_triangle_18():
    """Test validity_triangle case 18."""
    assert solution.validity_triangle(61, 51, 87) == False

def test_validity_triangle_19():
    """Test validity_triangle case 19."""
    assert solution.validity_triangle(63, 53, 85) == False

def test_validity_triangle_20():
    """Test validity_triangle case 20."""
    assert solution.validity_triangle(62, 45, 90) == False

def test_validity_triangle_21():
    """Test validity_triangle case 21."""
    assert solution.validity_triangle(63, 51, 94) == False

def test_validity_triangle_22():
    """Test validity_triangle case 22."""
    assert solution.validity_triangle(55, 46, 94) == False

def test_validity_triangle_23():
    """Test validity_triangle case 23."""
    assert solution.validity_triangle(59, 45, 85) == False

def test_validity_triangle_24():
    """Test validity_triangle case 24."""
    assert solution.validity_triangle(63, 54, 88) == False

def test_validity_triangle_25():
    """Test validity_triangle case 25."""
    assert solution.validity_triangle(55, 49, 94) == False

def test_validity_triangle_26():
    """Test validity_triangle case 26."""
    assert solution.validity_triangle(64, 55, 87) == False

def test_validity_triangle_27():
    """Test validity_triangle case 27."""
    assert solution.validity_triangle(58, 48, 87) == False

def test_validity_triangle_28():
    """Test validity_triangle case 28."""
    assert solution.validity_triangle(58, 46, 87) == False

def test_validity_triangle_29():
    """Test validity_triangle case 29."""
    assert solution.validity_triangle(63, 48, 92) == False

def test_validity_triangle_30():
    """Test validity_triangle case 30."""
    assert solution.validity_triangle(55, 55, 93) == False

def test_validity_triangle_31():
    """Test validity_triangle case 31."""
    assert solution.validity_triangle(61, 49, 94) == False

def test_validity_triangle_32():
    """Test validity_triangle case 32."""
    assert solution.validity_triangle(56, 54, 92) == False

def test_validity_triangle_33():
    """Test validity_triangle case 33."""
    assert solution.validity_triangle(64, 54, 88) == False

def test_validity_triangle_34():
    """Test validity_triangle case 34."""
    assert solution.validity_triangle(55, 54, 91) == False

def test_validity_triangle_35():
    """Test validity_triangle case 35."""
    assert solution.validity_triangle(58, 45, 93) == False

def test_validity_triangle_36():
    """Test validity_triangle case 36."""
    assert solution.validity_triangle(58, 52, 91) == False

def test_validity_triangle_37():
    """Test validity_triangle case 37."""
    assert solution.validity_triangle(42, 70, 58) == False

def test_validity_triangle_38():
    """Test validity_triangle case 38."""
    assert solution.validity_triangle(49, 78, 65) == False

def test_validity_triangle_39():
    """Test validity_triangle case 39."""
    assert solution.validity_triangle(41, 70, 57) == False

def test_validity_triangle_40():
    """Test validity_triangle case 40."""
    assert solution.validity_triangle(45, 73, 65) == False

def test_validity_triangle_41():
    """Test validity_triangle case 41."""
    assert solution.validity_triangle(47, 74, 62) == False

def test_validity_triangle_42():
    """Test validity_triangle case 42."""
    assert solution.validity_triangle(43, 73, 61) == False

def test_validity_triangle_43():
    """Test validity_triangle case 43."""
    assert solution.validity_triangle(40, 79, 65) == False

def test_validity_triangle_44():
    """Test validity_triangle case 44."""
    assert solution.validity_triangle(50, 74, 65) == False

def test_validity_triangle_45():
    """Test validity_triangle case 45."""
    assert solution.validity_triangle(50, 78, 57) == False

def test_validity_triangle_46():
    """Test validity_triangle case 46."""
    assert solution.validity_triangle(48, 77, 62) == False

def test_validity_triangle_47():
    """Test validity_triangle case 47."""
    assert solution.validity_triangle(40, 70, 65) == False

def test_validity_triangle_48():
    """Test validity_triangle case 48."""
    assert solution.validity_triangle(44, 70, 59) == False

def test_validity_triangle_49():
    """Test validity_triangle case 49."""
    assert solution.validity_triangle(50, 75, 63) == False

def test_validity_triangle_50():
    """Test validity_triangle case 50."""
    assert solution.validity_triangle(47, 80, 58) == False

def test_validity_triangle_51():
    """Test validity_triangle case 51."""
    assert solution.validity_triangle(49, 77, 56) == False

def test_validity_triangle_52():
    """Test validity_triangle case 52."""
    assert solution.validity_triangle(50, 73, 63) == False

def test_validity_triangle_53():
    """Test validity_triangle case 53."""
    assert solution.validity_triangle(42, 75, 62) == False

def test_validity_triangle_54():
    """Test validity_triangle case 54."""
    assert solution.validity_triangle(46, 80, 63) == False

def test_validity_triangle_55():
    """Test validity_triangle case 55."""
    assert solution.validity_triangle(41, 80, 61) == False

def test_validity_triangle_56():
    """Test validity_triangle case 56."""
    assert solution.validity_triangle(44, 74, 56) == False

def test_validity_triangle_57():
    """Test validity_triangle case 57."""
    assert solution.validity_triangle(48, 78, 62) == False

def test_validity_triangle_58():
    """Test validity_triangle case 58."""
    assert solution.validity_triangle(49, 72, 65) == False

def test_validity_triangle_59():
    """Test validity_triangle case 59."""
    assert solution.validity_triangle(45, 71, 63) == False

def test_validity_triangle_60():
    """Test validity_triangle case 60."""
    assert solution.validity_triangle(41, 71, 62) == False

def test_validity_triangle_61():
    """Test validity_triangle case 61."""
    assert solution.validity_triangle(44, 73, 56) == False

def test_validity_triangle_62():
    """Test validity_triangle case 62."""
    assert solution.validity_triangle(43, 73, 60) == False

def test_validity_triangle_63():
    """Test validity_triangle case 63."""
    assert solution.validity_triangle(48, 75, 59) == False

def test_validity_triangle_64():
    """Test validity_triangle case 64."""
    assert solution.validity_triangle(49, 74, 57) == True

def test_validity_triangle_65():
    """Test validity_triangle case 65."""
    assert solution.validity_triangle(44, 78, 57) == False

def test_validity_triangle_66():
    """Test validity_triangle case 66."""
    assert solution.validity_triangle(44, 73, 60) == False

def test_validity_triangle_67():
    """Test validity_triangle case 67."""
    assert solution.validity_triangle(41, 73, 65) == False

def test_validity_triangle_68():
    """Test validity_triangle case 68."""
    assert solution.validity_triangle(40, 79, 58) == False

def test_validity_triangle_69():
    """Test validity_triangle case 69."""
    assert solution.validity_triangle(44, 77, 63) == False

def test_validity_triangle_70():
    """Test validity_triangle case 70."""
    assert solution.validity_triangle(33, 46, 100) == False

def test_validity_triangle_71():
    """Test validity_triangle case 71."""
    assert solution.validity_triangle(33, 50, 105) == False

def test_validity_triangle_72():
    """Test validity_triangle case 72."""
    assert solution.validity_triangle(30, 54, 103) == False

def test_validity_triangle_73():
    """Test validity_triangle case 73."""
    assert solution.validity_triangle(32, 50, 96) == False

def test_validity_triangle_74():
    """Test validity_triangle case 74."""
    assert solution.validity_triangle(31, 52, 99) == False

def test_validity_triangle_75():
    """Test validity_triangle case 75."""
    assert solution.validity_triangle(28, 48, 102) == False

def test_validity_triangle_76():
    """Test validity_triangle case 76."""
    assert solution.validity_triangle(33, 51, 99) == False

def test_validity_triangle_77():
    """Test validity_triangle case 77."""
    assert solution.validity_triangle(30, 49, 102) == False

def test_validity_triangle_78():
    """Test validity_triangle case 78."""
    assert solution.validity_triangle(35, 53, 95) == False

def test_validity_triangle_79():
    """Test validity_triangle case 79."""
    assert solution.validity_triangle(33, 46, 101) == True

def test_validity_triangle_80():
    """Test validity_triangle case 80."""
    assert solution.validity_triangle(25, 46, 102) == False

def test_validity_triangle_81():
    """Test validity_triangle case 81."""
    assert solution.validity_triangle(31, 55, 101) == False

def test_validity_triangle_82():
    """Test validity_triangle case 82."""
    assert solution.validity_triangle(33, 54, 99) == False

def test_validity_triangle_83():
    """Test validity_triangle case 83."""
    assert solution.validity_triangle(29, 48, 97) == False

def test_validity_triangle_84():
    """Test validity_triangle case 84."""
    assert solution.validity_triangle(30, 50, 95) == False

def test_validity_triangle_85():
    """Test validity_triangle case 85."""
    assert solution.validity_triangle(26, 49, 103) == False

def test_validity_triangle_86():
    """Test validity_triangle case 86."""
    assert solution.validity_triangle(29, 53, 96) == False

def test_validity_triangle_87():
    """Test validity_triangle case 87."""
    assert solution.validity_triangle(35, 48, 96) == False

def test_validity_triangle_88():
    """Test validity_triangle case 88."""
    assert solution.validity_triangle(26, 47, 98) == False

def test_validity_triangle_89():
    """Test validity_triangle case 89."""
    assert solution.validity_triangle(28, 55, 98) == False

def test_validity_triangle_90():
    """Test validity_triangle case 90."""
    assert solution.validity_triangle(27, 47, 104) == False

def test_validity_triangle_91():
    """Test validity_triangle case 91."""
    assert solution.validity_triangle(25, 49, 101) == False

def test_validity_triangle_92():
    """Test validity_triangle case 92."""
    assert solution.validity_triangle(25, 54, 98) == False

def test_validity_triangle_93():
    """Test validity_triangle case 93."""
    assert solution.validity_triangle(27, 45, 104) == False

def test_validity_triangle_94():
    """Test validity_triangle case 94."""
    assert solution.validity_triangle(27, 46, 103) == False

def test_validity_triangle_95():
    """Test validity_triangle case 95."""
    assert solution.validity_triangle(26, 48, 97) == False

def test_validity_triangle_96():
    """Test validity_triangle case 96."""
    assert solution.validity_triangle(28, 54, 97) == False

def test_validity_triangle_97():
    """Test validity_triangle case 97."""
    assert solution.validity_triangle(31, 53, 99) == False

def test_validity_triangle_98():
    """Test validity_triangle case 98."""
    assert solution.validity_triangle(30, 50, 98) == False

def test_validity_triangle_99():
    """Test validity_triangle case 99."""
    assert solution.validity_triangle(35, 49, 101) == False

def test_validity_triangle_100():
    """Test validity_triangle case 100."""
    assert solution.validity_triangle(27, 47, 102) == False

def test_validity_triangle_101():
    """Test validity_triangle case 101."""
    assert solution.validity_triangle(27, 47, 99) == False

def test_validity_triangle_102():
    """Test validity_triangle case 102."""
    assert solution.validity_triangle(31, 52, 101) == False
