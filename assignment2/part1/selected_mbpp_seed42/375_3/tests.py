"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_round_num_1():
    """Test round_num case 1."""
    assert solution.round_num(4722,10)==4720

def test_round_num_2():
    """Test round_num case 2."""
    assert solution.round_num(1111,5)==1110

def test_round_num_3():
    """Test round_num case 3."""
    assert solution.round_num(219,2)==218

def test_round_num_4():
    """Test round_num case 4."""
    assert solution.round_num(5091, 9) == 5094

def test_round_num_5():
    """Test round_num case 5."""
    assert solution.round_num(5326, 8) == 5328

def test_round_num_6():
    """Test round_num case 6."""
    assert solution.round_num(5141, 11) == 5137

def test_round_num_7():
    """Test round_num case 7."""
    assert solution.round_num(4194, 9) == 4194

def test_round_num_8():
    """Test round_num case 8."""
    assert solution.round_num(4406, 9) == 4410

def test_round_num_9():
    """Test round_num case 9."""
    assert solution.round_num(4821, 7) == 4823

def test_round_num_10():
    """Test round_num case 10."""
    assert solution.round_num(4141, 13) == 4147

def test_round_num_11():
    """Test round_num case 11."""
    assert solution.round_num(4945, 11) == 4950

def test_round_num_12():
    """Test round_num case 12."""
    assert solution.round_num(5182, 6) == 5184

def test_round_num_13():
    """Test round_num case 13."""
    assert solution.round_num(4787, 6) == 4788

def test_round_num_14():
    """Test round_num case 14."""
    assert solution.round_num(4099, 12) == 4104

def test_round_num_15():
    """Test round_num case 15."""
    assert solution.round_num(5152, 11) == 5148

def test_round_num_16():
    """Test round_num case 16."""
    assert solution.round_num(5669, 13) == 5668

def test_round_num_17():
    """Test round_num case 17."""
    assert solution.round_num(4550, 12) == 4548

def test_round_num_18():
    """Test round_num case 18."""
    assert solution.round_num(4959, 7) == 4956

def test_round_num_19():
    """Test round_num case 19."""
    assert solution.round_num(5318, 9) == 5319

def test_round_num_20():
    """Test round_num case 20."""
    assert solution.round_num(4914, 11) == 4917

def test_round_num_21():
    """Test round_num case 21."""
    assert solution.round_num(4006, 5) == 4005

def test_round_num_22():
    """Test round_num case 22."""
    assert solution.round_num(4834, 14) == 4830

def test_round_num_23():
    """Test round_num case 23."""
    assert solution.round_num(5003, 13) == 5005

def test_round_num_24():
    """Test round_num case 24."""
    assert solution.round_num(4989, 15) == 4995

def test_round_num_25():
    """Test round_num case 25."""
    assert solution.round_num(4787, 5) == 4785

def test_round_num_26():
    """Test round_num case 26."""
    assert solution.round_num(5581, 15) == 5580

def test_round_num_27():
    """Test round_num case 27."""
    assert solution.round_num(3947, 12) == 3948

def test_round_num_28():
    """Test round_num case 28."""
    assert solution.round_num(5208, 6) == 5208

def test_round_num_29():
    """Test round_num case 29."""
    assert solution.round_num(4300, 9) == 4302

def test_round_num_30():
    """Test round_num case 30."""
    assert solution.round_num(4308, 14) == 4312

def test_round_num_31():
    """Test round_num case 31."""
    assert solution.round_num(5583, 9) == 5580

def test_round_num_32():
    """Test round_num case 32."""
    assert solution.round_num(3800, 9) == 3798

def test_round_num_33():
    """Test round_num case 33."""
    assert solution.round_num(4179, 13) == 4173

def test_round_num_34():
    """Test round_num case 34."""
    assert solution.round_num(3719, 15) == 3720

def test_round_num_35():
    """Test round_num case 35."""
    assert solution.round_num(4335, 13) == 4329

def test_round_num_36():
    """Test round_num case 36."""
    assert solution.round_num(4846, 15) == 4845

def test_round_num_37():
    """Test round_num case 37."""
    assert solution.round_num(120, 4) == 120

def test_round_num_38():
    """Test round_num case 38."""
    assert solution.round_num(2064, 9) == 2061

def test_round_num_39():
    """Test round_num case 39."""
    assert solution.round_num(1603, 7) == 1603

def test_round_num_40():
    """Test round_num case 40."""
    assert solution.round_num(1338, 6) == 1338

def test_round_num_41():
    """Test round_num case 41."""
    assert solution.round_num(337, 8) == 336

def test_round_num_42():
    """Test round_num case 42."""
    assert solution.round_num(1352, 5) == 1350

def test_round_num_43():
    """Test round_num case 43."""
    assert solution.round_num(1713, 5) == 1715

def test_round_num_44():
    """Test round_num case 44."""
    assert solution.round_num(1057, 10) == 1060

def test_round_num_45():
    """Test round_num case 45."""
    assert solution.round_num(437, 7) == 434

def test_round_num_46():
    """Test round_num case 46."""
    assert solution.round_num(1821, 6) == 1818

def test_round_num_47():
    """Test round_num case 47."""
    assert solution.round_num(1486, 2) == 1486

def test_round_num_48():
    """Test round_num case 48."""
    assert solution.round_num(1134, 4) == 1132

def test_round_num_49():
    """Test round_num case 49."""
    assert solution.round_num(106, 9) == 108

def test_round_num_50():
    """Test round_num case 50."""
    assert solution.round_num(1399, 9) == 1395

def test_round_num_51():
    """Test round_num case 51."""
    assert solution.round_num(779, 2) == 778

def test_round_num_52():
    """Test round_num case 52."""
    assert solution.round_num(890, 5) == 890

def test_round_num_53():
    """Test round_num case 53."""
    assert solution.round_num(959, 6) == 960

def test_round_num_54():
    """Test round_num case 54."""
    assert solution.round_num(1189, 6) == 1188

def test_round_num_55():
    """Test round_num case 55."""
    assert solution.round_num(1587, 8) == 1584

def test_round_num_56():
    """Test round_num case 56."""
    assert solution.round_num(657, 10) == 660

def test_round_num_57():
    """Test round_num case 57."""
    assert solution.round_num(1804, 8) == 1800

def test_round_num_58():
    """Test round_num case 58."""
    assert solution.round_num(1016, 9) == 1017

def test_round_num_59():
    """Test round_num case 59."""
    assert solution.round_num(850, 4) == 848

def test_round_num_60():
    """Test round_num case 60."""
    assert solution.round_num(1862, 10) == 1860

def test_round_num_61():
    """Test round_num case 61."""
    assert solution.round_num(1860, 4) == 1860

def test_round_num_62():
    """Test round_num case 62."""
    assert solution.round_num(488, 7) == 490

def test_round_num_63():
    """Test round_num case 63."""
    assert solution.round_num(582, 10) == 580

def test_round_num_64():
    """Test round_num case 64."""
    assert solution.round_num(375, 7) == 378

def test_round_num_65():
    """Test round_num case 65."""
    assert solution.round_num(1624, 6) == 1626

def test_round_num_66():
    """Test round_num case 66."""
    assert solution.round_num(908, 10) == 910

def test_round_num_67():
    """Test round_num case 67."""
    assert solution.round_num(747, 2) == 746

def test_round_num_68():
    """Test round_num case 68."""
    assert solution.round_num(1637, 7) == 1638

def test_round_num_69():
    """Test round_num case 69."""
    assert solution.round_num(106, 10) == 110

def test_round_num_70():
    """Test round_num case 70."""
    assert solution.round_num(215, 3) == 216

def test_round_num_71():
    """Test round_num case 71."""
    assert solution.round_num(222, 6) == 222

def test_round_num_72():
    """Test round_num case 72."""
    assert solution.round_num(219, 3) == 219

def test_round_num_73():
    """Test round_num case 73."""
    assert solution.round_num(222, 1) == 222

def test_round_num_74():
    """Test round_num case 74."""
    assert solution.round_num(219, 1) == 219

def test_round_num_75():
    """Test round_num case 75."""
    assert solution.round_num(218, 4) == 216

def test_round_num_76():
    """Test round_num case 76."""
    assert solution.round_num(221, 2) == 220

def test_round_num_77():
    """Test round_num case 77."""
    assert solution.round_num(220, 2) == 220

def test_round_num_78():
    """Test round_num case 78."""
    assert solution.round_num(214, 4) == 212

def test_round_num_79():
    """Test round_num case 79."""
    assert solution.round_num(214, 5) == 215

def test_round_num_80():
    """Test round_num case 80."""
    assert solution.round_num(223, 1) == 223

def test_round_num_81():
    """Test round_num case 81."""
    assert solution.round_num(219, 3) == 219

def test_round_num_82():
    """Test round_num case 82."""
    assert solution.round_num(221, 5) == 220

def test_round_num_83():
    """Test round_num case 83."""
    assert solution.round_num(219, 1) == 219

def test_round_num_84():
    """Test round_num case 84."""
    assert solution.round_num(218, 5) == 220

def test_round_num_85():
    """Test round_num case 85."""
    assert solution.round_num(217, 3) == 216

def test_round_num_86():
    """Test round_num case 86."""
    assert solution.round_num(221, 1) == 221

def test_round_num_87():
    """Test round_num case 87."""
    assert solution.round_num(219, 2) == 218

def test_round_num_88():
    """Test round_num case 88."""
    assert solution.round_num(223, 6) == 222

def test_round_num_89():
    """Test round_num case 89."""
    assert solution.round_num(223, 2) == 222

def test_round_num_90():
    """Test round_num case 90."""
    assert solution.round_num(217, 1) == 217

def test_round_num_91():
    """Test round_num case 91."""
    assert solution.round_num(222, 6) == 222

def test_round_num_92():
    """Test round_num case 92."""
    assert solution.round_num(216, 4) == 216

def test_round_num_93():
    """Test round_num case 93."""
    assert solution.round_num(219, 4) == 220

def test_round_num_94():
    """Test round_num case 94."""
    assert solution.round_num(221, 5) == 220

def test_round_num_95():
    """Test round_num case 95."""
    assert solution.round_num(217, 4) == 216

def test_round_num_96():
    """Test round_num case 96."""
    assert solution.round_num(222, 7) == 224

def test_round_num_97():
    """Test round_num case 97."""
    assert solution.round_num(215, 6) == 216

def test_round_num_98():
    """Test round_num case 98."""
    assert solution.round_num(215, 1) == 215

def test_round_num_99():
    """Test round_num case 99."""
    assert solution.round_num(221, 3) == 222

def test_round_num_100():
    """Test round_num case 100."""
    assert solution.round_num(217, 5) == 215

def test_round_num_101():
    """Test round_num case 101."""
    assert solution.round_num(214, 2) == 214

def test_round_num_102():
    """Test round_num case 102."""
    assert solution.round_num(216, 6) == 216
