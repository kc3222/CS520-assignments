"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_is_coprime_1():
    """Test is_coprime case 1."""
    assert solution.is_coprime(17,13) == True

def test_is_coprime_2():
    """Test is_coprime case 2."""
    assert solution.is_coprime(15,21) == False

def test_is_coprime_3():
    """Test is_coprime case 3."""
    assert solution.is_coprime(25,45) == False

def test_is_coprime_4():
    """Test is_coprime case 4."""
    assert solution.is_coprime(14, 12) == False

def test_is_coprime_5():
    """Test is_coprime case 5."""
    assert solution.is_coprime(18, 8) == False

def test_is_coprime_6():
    """Test is_coprime case 6."""
    assert solution.is_coprime(17, 14) == True

def test_is_coprime_7():
    """Test is_coprime case 7."""
    assert solution.is_coprime(17, 15) == True

def test_is_coprime_8():
    """Test is_coprime case 8."""
    assert solution.is_coprime(12, 17) == True

def test_is_coprime_9():
    """Test is_coprime case 9."""
    assert solution.is_coprime(17, 13) == True

def test_is_coprime_10():
    """Test is_coprime case 10."""
    assert solution.is_coprime(13, 18) == True

def test_is_coprime_11():
    """Test is_coprime case 11."""
    assert solution.is_coprime(12, 11) == True

def test_is_coprime_12():
    """Test is_coprime case 12."""
    assert solution.is_coprime(18, 10) == False

def test_is_coprime_13():
    """Test is_coprime case 13."""
    assert solution.is_coprime(16, 11) == True

def test_is_coprime_14():
    """Test is_coprime case 14."""
    assert solution.is_coprime(13, 12) == True

def test_is_coprime_15():
    """Test is_coprime case 15."""
    assert solution.is_coprime(15, 13) == True

def test_is_coprime_16():
    """Test is_coprime case 16."""
    assert solution.is_coprime(13, 17) == True

def test_is_coprime_17():
    """Test is_coprime case 17."""
    assert solution.is_coprime(19, 17) == True

def test_is_coprime_18():
    """Test is_coprime case 18."""
    assert solution.is_coprime(14, 9) == True

def test_is_coprime_19():
    """Test is_coprime case 19."""
    assert solution.is_coprime(15, 10) == False

def test_is_coprime_20():
    """Test is_coprime case 20."""
    assert solution.is_coprime(15, 9) == False

def test_is_coprime_21():
    """Test is_coprime case 21."""
    assert solution.is_coprime(15, 9) == False

def test_is_coprime_22():
    """Test is_coprime case 22."""
    assert solution.is_coprime(15, 13) == True

def test_is_coprime_23():
    """Test is_coprime case 23."""
    assert solution.is_coprime(13, 13) == False

def test_is_coprime_24():
    """Test is_coprime case 24."""
    assert solution.is_coprime(21, 12) == False

def test_is_coprime_25():
    """Test is_coprime case 25."""
    assert solution.is_coprime(16, 14) == False

def test_is_coprime_26():
    """Test is_coprime case 26."""
    assert solution.is_coprime(22, 14) == False

def test_is_coprime_27():
    """Test is_coprime case 27."""
    assert solution.is_coprime(14, 8) == False

def test_is_coprime_28():
    """Test is_coprime case 28."""
    assert solution.is_coprime(16, 17) == True

def test_is_coprime_29():
    """Test is_coprime case 29."""
    assert solution.is_coprime(13, 8) == True

def test_is_coprime_30():
    """Test is_coprime case 30."""
    assert solution.is_coprime(16, 11) == True

def test_is_coprime_31():
    """Test is_coprime case 31."""
    assert solution.is_coprime(16, 16) == False

def test_is_coprime_32():
    """Test is_coprime case 32."""
    assert solution.is_coprime(15, 15) == False

def test_is_coprime_33():
    """Test is_coprime case 33."""
    assert solution.is_coprime(20, 12) == False

def test_is_coprime_34():
    """Test is_coprime case 34."""
    assert solution.is_coprime(16, 14) == False

def test_is_coprime_35():
    """Test is_coprime case 35."""
    assert solution.is_coprime(12, 10) == False

def test_is_coprime_36():
    """Test is_coprime case 36."""
    assert solution.is_coprime(16, 17) == True

def test_is_coprime_37():
    """Test is_coprime case 37."""
    assert solution.is_coprime(16, 25) == True

def test_is_coprime_38():
    """Test is_coprime case 38."""
    assert solution.is_coprime(15, 21) == False

def test_is_coprime_39():
    """Test is_coprime case 39."""
    assert solution.is_coprime(17, 26) == True

def test_is_coprime_40():
    """Test is_coprime case 40."""
    assert solution.is_coprime(20, 16) == False

def test_is_coprime_41():
    """Test is_coprime case 41."""
    assert solution.is_coprime(18, 18) == False

def test_is_coprime_42():
    """Test is_coprime case 42."""
    assert solution.is_coprime(17, 23) == True

def test_is_coprime_43():
    """Test is_coprime case 43."""
    assert solution.is_coprime(18, 24) == False

def test_is_coprime_44():
    """Test is_coprime case 44."""
    assert solution.is_coprime(14, 16) == False

def test_is_coprime_45():
    """Test is_coprime case 45."""
    assert solution.is_coprime(10, 18) == False

def test_is_coprime_46():
    """Test is_coprime case 46."""
    assert solution.is_coprime(14, 26) == False

def test_is_coprime_47():
    """Test is_coprime case 47."""
    assert solution.is_coprime(12, 21) == False

def test_is_coprime_48():
    """Test is_coprime case 48."""
    assert solution.is_coprime(13, 20) == True

def test_is_coprime_49():
    """Test is_coprime case 49."""
    assert solution.is_coprime(18, 18) == False

def test_is_coprime_50():
    """Test is_coprime case 50."""
    assert solution.is_coprime(17, 16) == True

def test_is_coprime_51():
    """Test is_coprime case 51."""
    assert solution.is_coprime(11, 18) == True

def test_is_coprime_52():
    """Test is_coprime case 52."""
    assert solution.is_coprime(16, 24) == False

def test_is_coprime_53():
    """Test is_coprime case 53."""
    assert solution.is_coprime(16, 21) == True

def test_is_coprime_54():
    """Test is_coprime case 54."""
    assert solution.is_coprime(19, 21) == True

def test_is_coprime_55():
    """Test is_coprime case 55."""
    assert solution.is_coprime(16, 18) == False

def test_is_coprime_56():
    """Test is_coprime case 56."""
    assert solution.is_coprime(13, 19) == True

def test_is_coprime_57():
    """Test is_coprime case 57."""
    assert solution.is_coprime(11, 17) == True

def test_is_coprime_58():
    """Test is_coprime case 58."""
    assert solution.is_coprime(14, 23) == True

def test_is_coprime_59():
    """Test is_coprime case 59."""
    assert solution.is_coprime(10, 17) == True

def test_is_coprime_60():
    """Test is_coprime case 60."""
    assert solution.is_coprime(16, 21) == True

def test_is_coprime_61():
    """Test is_coprime case 61."""
    assert solution.is_coprime(18, 23) == True

def test_is_coprime_62():
    """Test is_coprime case 62."""
    assert solution.is_coprime(15, 16) == True

def test_is_coprime_63():
    """Test is_coprime case 63."""
    assert solution.is_coprime(14, 17) == True

def test_is_coprime_64():
    """Test is_coprime case 64."""
    assert solution.is_coprime(10, 18) == False

def test_is_coprime_65():
    """Test is_coprime case 65."""
    assert solution.is_coprime(12, 17) == True

def test_is_coprime_66():
    """Test is_coprime case 66."""
    assert solution.is_coprime(20, 21) == True

def test_is_coprime_67():
    """Test is_coprime case 67."""
    assert solution.is_coprime(17, 17) == False

def test_is_coprime_68():
    """Test is_coprime case 68."""
    assert solution.is_coprime(18, 24) == False

def test_is_coprime_69():
    """Test is_coprime case 69."""
    assert solution.is_coprime(15, 25) == False

def test_is_coprime_70():
    """Test is_coprime case 70."""
    assert solution.is_coprime(22, 40) == False

def test_is_coprime_71():
    """Test is_coprime case 71."""
    assert solution.is_coprime(24, 41) == True

def test_is_coprime_72():
    """Test is_coprime case 72."""
    assert solution.is_coprime(24, 44) == False

def test_is_coprime_73():
    """Test is_coprime case 73."""
    assert solution.is_coprime(21, 50) == True

def test_is_coprime_74():
    """Test is_coprime case 74."""
    assert solution.is_coprime(23, 47) == True

def test_is_coprime_75():
    """Test is_coprime case 75."""
    assert solution.is_coprime(21, 46) == True

def test_is_coprime_76():
    """Test is_coprime case 76."""
    assert solution.is_coprime(27, 48) == False

def test_is_coprime_77():
    """Test is_coprime case 77."""
    assert solution.is_coprime(27, 47) == True

def test_is_coprime_78():
    """Test is_coprime case 78."""
    assert solution.is_coprime(27, 46) == True

def test_is_coprime_79():
    """Test is_coprime case 79."""
    assert solution.is_coprime(22, 41) == True

def test_is_coprime_80():
    """Test is_coprime case 80."""
    assert solution.is_coprime(22, 45) == True

def test_is_coprime_81():
    """Test is_coprime case 81."""
    assert solution.is_coprime(25, 41) == True

def test_is_coprime_82():
    """Test is_coprime case 82."""
    assert solution.is_coprime(22, 40) == False

def test_is_coprime_83():
    """Test is_coprime case 83."""
    assert solution.is_coprime(23, 45) == True

def test_is_coprime_84():
    """Test is_coprime case 84."""
    assert solution.is_coprime(20, 41) == True

def test_is_coprime_85():
    """Test is_coprime case 85."""
    assert solution.is_coprime(20, 45) == False

def test_is_coprime_86():
    """Test is_coprime case 86."""
    assert solution.is_coprime(29, 47) == True

def test_is_coprime_87():
    """Test is_coprime case 87."""
    assert solution.is_coprime(27, 41) == True

def test_is_coprime_88():
    """Test is_coprime case 88."""
    assert solution.is_coprime(20, 49) == True

def test_is_coprime_89():
    """Test is_coprime case 89."""
    assert solution.is_coprime(24, 44) == False

def test_is_coprime_90():
    """Test is_coprime case 90."""
    assert solution.is_coprime(22, 48) == False

def test_is_coprime_91():
    """Test is_coprime case 91."""
    assert solution.is_coprime(28, 46) == False

def test_is_coprime_92():
    """Test is_coprime case 92."""
    assert solution.is_coprime(26, 44) == False

def test_is_coprime_93():
    """Test is_coprime case 93."""
    assert solution.is_coprime(24, 41) == True

def test_is_coprime_94():
    """Test is_coprime case 94."""
    assert solution.is_coprime(27, 41) == True

def test_is_coprime_95():
    """Test is_coprime case 95."""
    assert solution.is_coprime(23, 43) == True

def test_is_coprime_96():
    """Test is_coprime case 96."""
    assert solution.is_coprime(22, 50) == False

def test_is_coprime_97():
    """Test is_coprime case 97."""
    assert solution.is_coprime(28, 43) == True

def test_is_coprime_98():
    """Test is_coprime case 98."""
    assert solution.is_coprime(24, 44) == False

def test_is_coprime_99():
    """Test is_coprime case 99."""
    assert solution.is_coprime(25, 44) == True

def test_is_coprime_100():
    """Test is_coprime case 100."""
    assert solution.is_coprime(21, 40) == True

def test_is_coprime_101():
    """Test is_coprime case 101."""
    assert solution.is_coprime(21, 40) == True

def test_is_coprime_102():
    """Test is_coprime case 102."""
    assert solution.is_coprime(25, 42) == True
