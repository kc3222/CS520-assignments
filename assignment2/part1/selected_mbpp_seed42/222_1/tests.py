"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_check_type_1():
    """Test check_type case 1."""
    assert solution.check_type((5, 6, 7, 3, 5, 6) ) == True

def test_check_type_2():
    """Test check_type case 2."""
    assert solution.check_type((1, 2, "4") ) == False

def test_check_type_3():
    """Test check_type case 3."""
    assert solution.check_type((3, 2, 1, 4, 5) ) == True

def test_check_type_4():
    """Test check_type case 4."""
    assert solution.check_type((2, 1, 6, 2, 2, 3)) == True

def test_check_type_5():
    """Test check_type case 5."""
    assert solution.check_type((1, 7, 9, 8, 8, 1)) == True

def test_check_type_6():
    """Test check_type case 6."""
    assert solution.check_type((10, 11, 9, 2, 4, 3)) == True

def test_check_type_7():
    """Test check_type case 7."""
    assert solution.check_type((9, 1, 6, 7, 4, 4)) == True

def test_check_type_8():
    """Test check_type case 8."""
    assert solution.check_type((9, 9, 7, 4, 6, 3)) == True

def test_check_type_9():
    """Test check_type case 9."""
    assert solution.check_type((2, 10, 9, 4, 1, 7)) == True

def test_check_type_10():
    """Test check_type case 10."""
    assert solution.check_type((8, 9, 8, 2, 5, 5)) == True

def test_check_type_11():
    """Test check_type case 11."""
    assert solution.check_type((5, 10, 6, 8, 7, 9)) == True

def test_check_type_12():
    """Test check_type case 12."""
    assert solution.check_type((5, 5, 4, 1, 3, 6)) == True

def test_check_type_13():
    """Test check_type case 13."""
    assert solution.check_type((5, 8, 10, 4, 7, 1)) == True

def test_check_type_14():
    """Test check_type case 14."""
    assert solution.check_type((8, 9, 3, 5, 4, 1)) == True

def test_check_type_15():
    """Test check_type case 15."""
    assert solution.check_type((9, 8, 5, 6, 10, 1)) == True

def test_check_type_16():
    """Test check_type case 16."""
    assert solution.check_type((8, 5, 9, 8, 1, 5)) == True

def test_check_type_17():
    """Test check_type case 17."""
    assert solution.check_type((1, 2, 3, 2, 3, 3)) == True

def test_check_type_18():
    """Test check_type case 18."""
    assert solution.check_type((1, 2, 12, 7, 1, 10)) == True

def test_check_type_19():
    """Test check_type case 19."""
    assert solution.check_type((8, 11, 12, 1, 5, 4)) == True

def test_check_type_20():
    """Test check_type case 20."""
    assert solution.check_type((6, 1, 3, 2, 7, 8)) == True

def test_check_type_21():
    """Test check_type case 21."""
    assert solution.check_type((7, 3, 11, 3, 2, 11)) == True

def test_check_type_22():
    """Test check_type case 22."""
    assert solution.check_type((2, 1, 5, 5, 7, 3)) == True

def test_check_type_23():
    """Test check_type case 23."""
    assert solution.check_type((8, 7, 8, 2, 2, 4)) == True

def test_check_type_24():
    """Test check_type case 24."""
    assert solution.check_type((1, 3, 12, 8, 2, 3)) == True

def test_check_type_25():
    """Test check_type case 25."""
    assert solution.check_type((3, 3, 4, 5, 6, 11)) == True

def test_check_type_26():
    """Test check_type case 26."""
    assert solution.check_type((4, 3, 5, 6, 5, 9)) == True

def test_check_type_27():
    """Test check_type case 27."""
    assert solution.check_type((3, 7, 3, 1, 4, 10)) == True

def test_check_type_28():
    """Test check_type case 28."""
    assert solution.check_type((8, 10, 4, 2, 10, 1)) == True

def test_check_type_29():
    """Test check_type case 29."""
    assert solution.check_type((4, 9, 8, 3, 7, 6)) == True

def test_check_type_30():
    """Test check_type case 30."""
    assert solution.check_type((5, 2, 8, 8, 8, 2)) == True

def test_check_type_31():
    """Test check_type case 31."""
    assert solution.check_type((10, 2, 6, 8, 10, 3)) == True

def test_check_type_32():
    """Test check_type case 32."""
    assert solution.check_type((5, 6, 12, 7, 9, 11)) == True

def test_check_type_33():
    """Test check_type case 33."""
    assert solution.check_type((2, 4, 8, 3, 1, 7)) == True

def test_check_type_34():
    """Test check_type case 34."""
    assert solution.check_type((7, 3, 12, 4, 10, 6)) == True

def test_check_type_35():
    """Test check_type case 35."""
    assert solution.check_type((5, 6, 4, 6, 3, 1)) == True

def test_check_type_36():
    """Test check_type case 36."""
    assert solution.check_type((8, 3, 4, 7, 9, 4)) == True

def test_check_type_37():
    """Test check_type case 37."""
    assert solution.check_type((6, 5, '3')) == False

def test_check_type_38():
    """Test check_type case 38."""
    assert solution.check_type((6, 2, '0')) == False

def test_check_type_39():
    """Test check_type case 39."""
    assert solution.check_type((5, 4, '3')) == False

def test_check_type_40():
    """Test check_type case 40."""
    assert solution.check_type((3, 7, '5')) == False

def test_check_type_41():
    """Test check_type case 41."""
    assert solution.check_type((2, 6, '6')) == False

def test_check_type_42():
    """Test check_type case 42."""
    assert solution.check_type((4, 6, '0')) == False

def test_check_type_43():
    """Test check_type case 43."""
    assert solution.check_type((5, 4, '3')) == False

def test_check_type_44():
    """Test check_type case 44."""
    assert solution.check_type((5, 4, '1')) == False

def test_check_type_45():
    """Test check_type case 45."""
    assert solution.check_type((1, 7, '0')) == False

def test_check_type_46():
    """Test check_type case 46."""
    assert solution.check_type((3, 1, '5')) == False

def test_check_type_47():
    """Test check_type case 47."""
    assert solution.check_type((4, 5, '7')) == False

def test_check_type_48():
    """Test check_type case 48."""
    assert solution.check_type((6, 2, '3')) == False

def test_check_type_49():
    """Test check_type case 49."""
    assert solution.check_type((6, 3, '4')) == False

def test_check_type_50():
    """Test check_type case 50."""
    assert solution.check_type((4, 7, '3')) == False

def test_check_type_51():
    """Test check_type case 51."""
    assert solution.check_type((5, 2, '4')) == False

def test_check_type_52():
    """Test check_type case 52."""
    assert solution.check_type((2, 6, '3')) == False

def test_check_type_53():
    """Test check_type case 53."""
    assert solution.check_type((2, 2, '8')) == False

def test_check_type_54():
    """Test check_type case 54."""
    assert solution.check_type((3, 3, '4')) == False

def test_check_type_55():
    """Test check_type case 55."""
    assert solution.check_type((1, 6, '4')) == False

def test_check_type_56():
    """Test check_type case 56."""
    assert solution.check_type((4, 7, '3')) == False

def test_check_type_57():
    """Test check_type case 57."""
    assert solution.check_type((2, 1, '6')) == False

def test_check_type_58():
    """Test check_type case 58."""
    assert solution.check_type((3, 7, '3')) == False

def test_check_type_59():
    """Test check_type case 59."""
    assert solution.check_type((3, 2, '6')) == False

def test_check_type_60():
    """Test check_type case 60."""
    assert solution.check_type((4, 7, '7')) == False

def test_check_type_61():
    """Test check_type case 61."""
    assert solution.check_type((2, 4, '9')) == False

def test_check_type_62():
    """Test check_type case 62."""
    assert solution.check_type((3, 7, '0')) == False

def test_check_type_63():
    """Test check_type case 63."""
    assert solution.check_type((6, 4, '6')) == False

def test_check_type_64():
    """Test check_type case 64."""
    assert solution.check_type((2, 6, '5')) == False

def test_check_type_65():
    """Test check_type case 65."""
    assert solution.check_type((2, 5, '0')) == False

def test_check_type_66():
    """Test check_type case 66."""
    assert solution.check_type((3, 6, '9')) == False

def test_check_type_67():
    """Test check_type case 67."""
    assert solution.check_type((6, 6, '3')) == False

def test_check_type_68():
    """Test check_type case 68."""
    assert solution.check_type((4, 3, '3')) == False

def test_check_type_69():
    """Test check_type case 69."""
    assert solution.check_type((6, 7, '5')) == False

def test_check_type_70():
    """Test check_type case 70."""
    assert solution.check_type((1, 1, 3, 5, 7)) == True

def test_check_type_71():
    """Test check_type case 71."""
    assert solution.check_type((4, 7, 2, 3, 7)) == True

def test_check_type_72():
    """Test check_type case 72."""
    assert solution.check_type((1, 4, 2, 4, 6)) == True

def test_check_type_73():
    """Test check_type case 73."""
    assert solution.check_type((5, 1, 2, 3, 10)) == True

def test_check_type_74():
    """Test check_type case 74."""
    assert solution.check_type((1, 3, 2, 2, 2)) == True

def test_check_type_75():
    """Test check_type case 75."""
    assert solution.check_type((8, 1, 2, 2, 6)) == True

def test_check_type_76():
    """Test check_type case 76."""
    assert solution.check_type((3, 7, 1, 6, 5)) == True

def test_check_type_77():
    """Test check_type case 77."""
    assert solution.check_type((5, 6, 1, 9, 10)) == True

def test_check_type_78():
    """Test check_type case 78."""
    assert solution.check_type((5, 2, 1, 3, 6)) == True

def test_check_type_79():
    """Test check_type case 79."""
    assert solution.check_type((5, 2, 4, 2, 3)) == True

def test_check_type_80():
    """Test check_type case 80."""
    assert solution.check_type((3, 6, 4, 1, 5)) == True

def test_check_type_81():
    """Test check_type case 81."""
    assert solution.check_type((8, 2, 3, 4, 1)) == True

def test_check_type_82():
    """Test check_type case 82."""
    assert solution.check_type((8, 2, 1, 1, 9)) == True

def test_check_type_83():
    """Test check_type case 83."""
    assert solution.check_type((8, 1, 4, 8, 1)) == True

def test_check_type_84():
    """Test check_type case 84."""
    assert solution.check_type((5, 3, 2, 5, 7)) == True

def test_check_type_85():
    """Test check_type case 85."""
    assert solution.check_type((4, 6, 6, 5, 9)) == True

def test_check_type_86():
    """Test check_type case 86."""
    assert solution.check_type((6, 7, 2, 3, 1)) == True

def test_check_type_87():
    """Test check_type case 87."""
    assert solution.check_type((6, 3, 2, 4, 5)) == True

def test_check_type_88():
    """Test check_type case 88."""
    assert solution.check_type((7, 3, 2, 2, 1)) == True

def test_check_type_89():
    """Test check_type case 89."""
    assert solution.check_type((3, 1, 4, 1, 3)) == True

def test_check_type_90():
    """Test check_type case 90."""
    assert solution.check_type((2, 5, 6, 6, 8)) == True

def test_check_type_91():
    """Test check_type case 91."""
    assert solution.check_type((3, 2, 3, 3, 7)) == True

def test_check_type_92():
    """Test check_type case 92."""
    assert solution.check_type((3, 3, 5, 3, 3)) == True

def test_check_type_93():
    """Test check_type case 93."""
    assert solution.check_type((7, 4, 5, 8, 3)) == True

def test_check_type_94():
    """Test check_type case 94."""
    assert solution.check_type((3, 1, 5, 6, 7)) == True

def test_check_type_95():
    """Test check_type case 95."""
    assert solution.check_type((8, 7, 5, 8, 6)) == True

def test_check_type_96():
    """Test check_type case 96."""
    assert solution.check_type((4, 6, 5, 1, 10)) == True

def test_check_type_97():
    """Test check_type case 97."""
    assert solution.check_type((1, 6, 2, 8, 8)) == True

def test_check_type_98():
    """Test check_type case 98."""
    assert solution.check_type((8, 7, 4, 8, 6)) == True

def test_check_type_99():
    """Test check_type case 99."""
    assert solution.check_type((5, 2, 4, 1, 2)) == True

def test_check_type_100():
    """Test check_type case 100."""
    assert solution.check_type((4, 5, 6, 9, 4)) == True

def test_check_type_101():
    """Test check_type case 101."""
    assert solution.check_type((1, 2, 5, 7, 1)) == True

def test_check_type_102():
    """Test check_type case 102."""
    assert solution.check_type((7, 1, 5, 4, 6)) == True
