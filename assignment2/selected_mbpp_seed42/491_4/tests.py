"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_sum_gp_1():
    """Test sum_gp case 1."""
    assert solution.sum_gp(1,5,2)==31

def test_sum_gp_2():
    """Test sum_gp case 2."""
    assert solution.sum_gp(1,5,4)==341

def test_sum_gp_3():
    """Test sum_gp case 3."""
    assert solution.sum_gp(2,6,3)==728

def test_sum_gp_4():
    """Test sum_gp case 4."""
    assert solution.sum_gp(1, 4, 4) == 85.0

def test_sum_gp_5():
    """Test sum_gp case 5."""
    assert solution.sum_gp(6, 4, 7) == 2400.0

def test_sum_gp_6():
    """Test sum_gp case 6."""
    assert solution.sum_gp(3, 2, 6) == 21.0

def test_sum_gp_7():
    """Test sum_gp case 7."""
    assert solution.sum_gp(6, 2, 4) == 30.0

def test_sum_gp_8():
    """Test sum_gp case 8."""
    assert solution.sum_gp(5, 3, 2) == 35.0

def test_sum_gp_9():
    """Test sum_gp case 9."""
    assert solution.sum_gp(1, 4, 6) == 259.0

def test_sum_gp_10():
    """Test sum_gp case 10."""
    assert solution.sum_gp(6, 4, 2) == 90.0

def test_sum_gp_11():
    """Test sum_gp case 11."""
    assert solution.sum_gp(2, 2, 7) == 16.0

def test_sum_gp_12():
    """Test sum_gp case 12."""
    assert solution.sum_gp(1, 3, 4) == 21.0

def test_sum_gp_13():
    """Test sum_gp case 13."""
    assert solution.sum_gp(5, 3, 2) == 35.0

def test_sum_gp_14():
    """Test sum_gp case 14."""
    assert solution.sum_gp(4, 6, 3) == 1456.0

def test_sum_gp_15():
    """Test sum_gp case 15."""
    assert solution.sum_gp(6, 5, 6) == 9330.0

def test_sum_gp_16():
    """Test sum_gp case 16."""
    assert solution.sum_gp(4, 7, 2) == 508.0

def test_sum_gp_17():
    """Test sum_gp case 17."""
    assert solution.sum_gp(3, 10, 3) == 88572.0

def test_sum_gp_18():
    """Test sum_gp case 18."""
    assert solution.sum_gp(6, 3, 6) == 258.0

def test_sum_gp_19():
    """Test sum_gp case 19."""
    assert solution.sum_gp(1, 5, 2) == 31.0

def test_sum_gp_20():
    """Test sum_gp case 20."""
    assert solution.sum_gp(2, 2, 5) == 12.0

def test_sum_gp_21():
    """Test sum_gp case 21."""
    assert solution.sum_gp(4, 9, 6) == 8062156.0

def test_sum_gp_22():
    """Test sum_gp case 22."""
    assert solution.sum_gp(3, 10, 5) == 7324218.0

def test_sum_gp_23():
    """Test sum_gp case 23."""
    assert solution.sum_gp(4, 9, 7) == 26902404.0

def test_sum_gp_24():
    """Test sum_gp case 24."""
    assert solution.sum_gp(5, 10, 2) == 5115.0

def test_sum_gp_25():
    """Test sum_gp case 25."""
    assert solution.sum_gp(5, 9, 4) == 436905.0

def test_sum_gp_26():
    """Test sum_gp case 26."""
    assert solution.sum_gp(2, 3, 2) == 14.0

def test_sum_gp_27():
    """Test sum_gp case 27."""
    assert solution.sum_gp(4, 6, 3) == 1456.0

def test_sum_gp_28():
    """Test sum_gp case 28."""
    assert solution.sum_gp(2, 6, 7) == 39216.0

def test_sum_gp_29():
    """Test sum_gp case 29."""
    assert solution.sum_gp(4, 5, 7) == 11204.0

def test_sum_gp_30():
    """Test sum_gp case 30."""
    assert solution.sum_gp(2, 10, 4) == 699050.0

def test_sum_gp_31():
    """Test sum_gp case 31."""
    assert solution.sum_gp(3, 7, 6) == 167961.0

def test_sum_gp_32():
    """Test sum_gp case 32."""
    assert solution.sum_gp(1, 10, 2) == 1023.0

def test_sum_gp_33():
    """Test sum_gp case 33."""
    assert solution.sum_gp(1, 5, 5) == 781.0

def test_sum_gp_34():
    """Test sum_gp case 34."""
    assert solution.sum_gp(4, 2, 2) == 12.0

def test_sum_gp_35():
    """Test sum_gp case 35."""
    assert solution.sum_gp(6, 4, 6) == 1554.0

def test_sum_gp_36():
    """Test sum_gp case 36."""
    assert solution.sum_gp(4, 3, 6) == 172.0

def test_sum_gp_37():
    """Test sum_gp case 37."""
    assert solution.sum_gp(2, 10, 3) == 59048.0

def test_sum_gp_38():
    """Test sum_gp case 38."""
    assert solution.sum_gp(4, 4, 8) == 2340.0

def test_sum_gp_39():
    """Test sum_gp case 39."""
    assert solution.sum_gp(4, 5, 5) == 3124.0

def test_sum_gp_40():
    """Test sum_gp case 40."""
    assert solution.sum_gp(1, 6, 6) == 9331.0

def test_sum_gp_41():
    """Test sum_gp case 41."""
    assert solution.sum_gp(3, 5, 5) == 2343.0

def test_sum_gp_42():
    """Test sum_gp case 42."""
    assert solution.sum_gp(3, 5, 3) == 363.0

def test_sum_gp_43():
    """Test sum_gp case 43."""
    assert solution.sum_gp(4, 8, 6) == 1343692.0

def test_sum_gp_44():
    """Test sum_gp case 44."""
    assert solution.sum_gp(2, 6, 8) == 74898.0

def test_sum_gp_45():
    """Test sum_gp case 45."""
    assert solution.sum_gp(1, 10, 5) == 2441406.0

def test_sum_gp_46():
    """Test sum_gp case 46."""
    assert solution.sum_gp(3, 1, 5) == 3.0

def test_sum_gp_47():
    """Test sum_gp case 47."""
    assert solution.sum_gp(3, 7, 4) == 16383.0

def test_sum_gp_48():
    """Test sum_gp case 48."""
    assert solution.sum_gp(2, 9, 9) == 96855122.0

def test_sum_gp_49():
    """Test sum_gp case 49."""
    assert solution.sum_gp(5, 7, 8) == 1497965.0

def test_sum_gp_50():
    """Test sum_gp case 50."""
    assert solution.sum_gp(1, 9, 2) == 511.0

def test_sum_gp_51():
    """Test sum_gp case 51."""
    assert solution.sum_gp(4, 10, 7) == 188316832.0

def test_sum_gp_52():
    """Test sum_gp case 52."""
    assert solution.sum_gp(6, 8, 2) == 1530.0

def test_sum_gp_53():
    """Test sum_gp case 53."""
    assert solution.sum_gp(5, 6, 2) == 315.0

def test_sum_gp_54():
    """Test sum_gp case 54."""
    assert solution.sum_gp(4, 9, 5) == 1953124.0

def test_sum_gp_55():
    """Test sum_gp case 55."""
    assert solution.sum_gp(5, 1, 9) == 5.0

def test_sum_gp_56():
    """Test sum_gp case 56."""
    assert solution.sum_gp(1, 5, 3) == 121.0

def test_sum_gp_57():
    """Test sum_gp case 57."""
    assert solution.sum_gp(4, 10, 3) == 118096.0

def test_sum_gp_58():
    """Test sum_gp case 58."""
    assert solution.sum_gp(2, 1, 2) == 2.0

def test_sum_gp_59():
    """Test sum_gp case 59."""
    assert solution.sum_gp(2, 1, 5) == 2.0

def test_sum_gp_60():
    """Test sum_gp case 60."""
    assert solution.sum_gp(5, 7, 9) == 2989355.0

def test_sum_gp_61():
    """Test sum_gp case 61."""
    assert solution.sum_gp(1, 5, 7) == 2801.0

def test_sum_gp_62():
    """Test sum_gp case 62."""
    assert solution.sum_gp(3, 7, 6) == 167961.0

def test_sum_gp_63():
    """Test sum_gp case 63."""
    assert solution.sum_gp(4, 1, 9) == 4.0

def test_sum_gp_64():
    """Test sum_gp case 64."""
    assert solution.sum_gp(1, 6, 7) == 19608.0

def test_sum_gp_65():
    """Test sum_gp case 65."""
    assert solution.sum_gp(6, 5, 8) == 28086.0

def test_sum_gp_66():
    """Test sum_gp case 66."""
    assert solution.sum_gp(1, 9, 2) == 511.0

def test_sum_gp_67():
    """Test sum_gp case 67."""
    assert solution.sum_gp(3, 7, 3) == 3279.0

def test_sum_gp_68():
    """Test sum_gp case 68."""
    assert solution.sum_gp(4, 2, 4) == 20.0

def test_sum_gp_69():
    """Test sum_gp case 69."""
    assert solution.sum_gp(3, 1, 7) == 3.0

def test_sum_gp_70():
    """Test sum_gp case 70."""
    assert solution.sum_gp(5, 1, 5) == 5.0

def test_sum_gp_71():
    """Test sum_gp case 71."""
    assert solution.sum_gp(6, 11, 5) == 73242186.0

def test_sum_gp_72():
    """Test sum_gp case 72."""
    assert solution.sum_gp(2, 9, 5) == 976562.0

def test_sum_gp_73():
    """Test sum_gp case 73."""
    assert solution.sum_gp(3, 6, 6) == 27993.0

def test_sum_gp_74():
    """Test sum_gp case 74."""
    assert solution.sum_gp(3, 1, 6) == 3.0

def test_sum_gp_75():
    """Test sum_gp case 75."""
    assert solution.sum_gp(5, 3, 6) == 215.0

def test_sum_gp_76():
    """Test sum_gp case 76."""
    assert solution.sum_gp(2, 11, 7) == 659108914.0

def test_sum_gp_77():
    """Test sum_gp case 77."""
    assert solution.sum_gp(1, 4, 6) == 259.0

def test_sum_gp_78():
    """Test sum_gp case 78."""
    assert solution.sum_gp(4, 3, 6) == 172.0

def test_sum_gp_79():
    """Test sum_gp case 79."""
    assert solution.sum_gp(2, 9, 4) == 174762.0

def test_sum_gp_80():
    """Test sum_gp case 80."""
    assert solution.sum_gp(2, 2, 3) == 8.0

def test_sum_gp_81():
    """Test sum_gp case 81."""
    assert solution.sum_gp(1, 1, 7) == 1.0

def test_sum_gp_82():
    """Test sum_gp case 82."""
    assert solution.sum_gp(3, 9, 3) == 29523.0

def test_sum_gp_83():
    """Test sum_gp case 83."""
    assert solution.sum_gp(5, 1, 5) == 5.0

def test_sum_gp_84():
    """Test sum_gp case 84."""
    assert solution.sum_gp(5, 2, 2) == 15.0

def test_sum_gp_85():
    """Test sum_gp case 85."""
    assert solution.sum_gp(4, 6, 8) == 149796.0

def test_sum_gp_86():
    """Test sum_gp case 86."""
    assert solution.sum_gp(6, 9, 2) == 3066.0

def test_sum_gp_87():
    """Test sum_gp case 87."""
    assert solution.sum_gp(7, 2, 8) == 63.0

def test_sum_gp_88():
    """Test sum_gp case 88."""
    assert solution.sum_gp(7, 2, 8) == 63.0

def test_sum_gp_89():
    """Test sum_gp case 89."""
    assert solution.sum_gp(1, 1, 4) == 1.0

def test_sum_gp_90():
    """Test sum_gp case 90."""
    assert solution.sum_gp(4, 4, 6) == 1036.0

def test_sum_gp_91():
    """Test sum_gp case 91."""
    assert solution.sum_gp(3, 10, 6) == 36279705.0

def test_sum_gp_92():
    """Test sum_gp case 92."""
    assert solution.sum_gp(5, 10, 2) == 5115.0

def test_sum_gp_93():
    """Test sum_gp case 93."""
    assert solution.sum_gp(2, 10, 2) == 2046.0

def test_sum_gp_94():
    """Test sum_gp case 94."""
    assert solution.sum_gp(3, 4, 5) == 468.0

def test_sum_gp_95():
    """Test sum_gp case 95."""
    assert solution.sum_gp(5, 9, 5) == 2441405.0

def test_sum_gp_96():
    """Test sum_gp case 96."""
    assert solution.sum_gp(3, 10, 4) == 1048575.0

def test_sum_gp_97():
    """Test sum_gp case 97."""
    assert solution.sum_gp(7, 5, 3) == 847.0

def test_sum_gp_98():
    """Test sum_gp case 98."""
    assert solution.sum_gp(3, 3, 6) == 129.0

def test_sum_gp_99():
    """Test sum_gp case 99."""
    assert solution.sum_gp(4, 9, 5) == 1953124.0

def test_sum_gp_100():
    """Test sum_gp case 100."""
    assert solution.sum_gp(6, 6, 7) == 117648.0

def test_sum_gp_101():
    """Test sum_gp case 101."""
    assert solution.sum_gp(6, 8, 8) == 14380470.0

def test_sum_gp_102():
    """Test sum_gp case 102."""
    assert solution.sum_gp(2, 11, 3) == 177146.0
