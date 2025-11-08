"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_min_val_1():
    """Test min_val case 1."""
    assert solution.min_val(['Python', 3, 2, 4, 5, 'version'])==2

def test_min_val_2():
    """Test min_val case 2."""
    assert solution.min_val(['Python', 15, 20, 25])==15

def test_min_val_3():
    """Test min_val case 3."""
    assert solution.min_val(['Python', 30, 20, 40, 50, 'version'])==20

def test_min_val_4():
    """Test min_val case 4."""
    assert solution.min_val(['Hzgn', 8, 2, 6, 3, 'rnjxdg']) == 2

def test_min_val_5():
    """Test min_val case 5."""
    assert solution.min_val(['smGoJ', 3, 6, 6, 3, 'orvw']) == 3

def test_min_val_6():
    """Test min_val case 6."""
    assert solution.min_val(['hJXuNEvHE', 2, 5, 7, 9, 'hbn']) == 2

def test_min_val_7():
    """Test min_val case 7."""
    assert solution.min_val(['HstmSajZT', 2, 4, 4, 9, 'qsfmpgliekx']) == 2

def test_min_val_8():
    """Test min_val case 8."""
    assert solution.min_val(['LDsJJQbL', 3, 2, 6, 8, 'weptakuf']) == 2

def test_min_val_9():
    """Test min_val case 9."""
    assert solution.min_val(['QIrO', 2, 1, 7, 2, 'dictnghn']) == 1

def test_min_val_10():
    """Test min_val case 10."""
    assert solution.min_val(['wAUEw', 4, 6, 9, 8, 'ofeau']) == 4

def test_min_val_11():
    """Test min_val case 11."""
    assert solution.min_val(['XISeqgLUeu', 5, 1, 7, 2, 'bkyy']) == 1

def test_min_val_12():
    """Test min_val case 12."""
    assert solution.min_val(['OjJCC', 1, 6, 6, 1, 'xldewi']) == 1

def test_min_val_13():
    """Test min_val case 13."""
    assert solution.min_val(['LUeFL', 1, 5, 5, 7, 'uqxlqznrv']) == 1

def test_min_val_14():
    """Test min_val case 14."""
    assert solution.min_val(['syHRbRpq', 5, 5, 2, 8, 'siyxhciiskhc']) == 2

def test_min_val_15():
    """Test min_val case 15."""
    assert solution.min_val(['HeHgPo', 6, 3, 1, 8, 'fge']) == 1

def test_min_val_16():
    """Test min_val case 16."""
    assert solution.min_val(['Lno', 4, 1, 9, 6, 'gfz']) == 1

def test_min_val_17():
    """Test min_val case 17."""
    assert solution.min_val(['eUjaqNfdsfZV', 6, 7, 5, 7, 'aehukfbtua']) == 5

def test_min_val_18():
    """Test min_val case 18."""
    assert solution.min_val(['FlXZOMZQ', 3, 2, 9, 2, 'gkuvqyh']) == 2

def test_min_val_19():
    """Test min_val case 19."""
    assert solution.min_val(['ICNIULJ', 7, 2, 6, 5, 'hscazrhrlxqt']) == 2

def test_min_val_20():
    """Test min_val case 20."""
    assert solution.min_val(['KQYa', 1, 5, 5, 4, 'iesmreyufgf']) == 1

def test_min_val_21():
    """Test min_val case 21."""
    assert solution.min_val(['kSYdtspqDG', 4, 4, 4, 2, 'llofkv']) == 2

def test_min_val_22():
    """Test min_val case 22."""
    assert solution.min_val(['vYqB', 3, 4, 3, 2, 'otixcfybon']) == 2

def test_min_val_23():
    """Test min_val case 23."""
    assert solution.min_val(['LwDZ', 2, 1, 6, 1, 'bpddrpprasw']) == 1

def test_min_val_24():
    """Test min_val case 24."""
    assert solution.min_val(['KliVODcNIbJc', 3, 3, 9, 6, 'henrl']) == 3

def test_min_val_25():
    """Test min_val case 25."""
    assert solution.min_val(['OYPlumF', 3, 3, 8, 6, 'iliy']) == 3

def test_min_val_26():
    """Test min_val case 26."""
    assert solution.min_val(['sQu', 1, 4, 4, 9, 'vkgfidlmzy']) == 1

def test_min_val_27():
    """Test min_val case 27."""
    assert solution.min_val(['OmaC', 7, 6, 2, 5, 'zgxokgnuisi']) == 2

def test_min_val_28():
    """Test min_val case 28."""
    assert solution.min_val(['fCttsVY', 4, 6, 1, 8, 'xecsbkn']) == 1

def test_min_val_29():
    """Test min_val case 29."""
    assert solution.min_val(['XQjWs', 1, 1, 7, 10, 'heqam']) == 1

def test_min_val_30():
    """Test min_val case 30."""
    assert solution.min_val(['adRuGajh', 6, 1, 2, 2, 'tijocjzucq']) == 1

def test_min_val_31():
    """Test min_val case 31."""
    assert solution.min_val(['xbnshYBm', 1, 3, 3, 4, 'pbefhjlb']) == 1

def test_min_val_32():
    """Test min_val case 32."""
    assert solution.min_val(['ywS', 2, 2, 1, 2, 'tryknyj']) == 1

def test_min_val_33():
    """Test min_val case 33."""
    assert solution.min_val(['vKysfe', 1, 3, 8, 5, 'azng']) == 1

def test_min_val_34():
    """Test min_val case 34."""
    assert solution.min_val(['HgTnglhornr', 7, 3, 8, 10, 'wic']) == 3

def test_min_val_35():
    """Test min_val case 35."""
    assert solution.min_val(['NwqdqjBBPk', 5, 4, 3, 9, 'pgi']) == 3

def test_min_val_36():
    """Test min_val case 36."""
    assert solution.min_val(['Nln', 2, 6, 8, 1, 'hnf']) == 1

def test_min_val_37():
    """Test min_val case 37."""
    assert solution.min_val(['yzCjPw', 10, 19, 21]) == 10

def test_min_val_38():
    """Test min_val case 38."""
    assert solution.min_val(['ddckbcme', 18, 25, 30]) == 18

def test_min_val_39():
    """Test min_val case 39."""
    assert solution.min_val(['enHpxvrPUEN', 10, 21, 28]) == 10

def test_min_val_40():
    """Test min_val case 40."""
    assert solution.min_val(['xIdWszWpgsh', 12, 16, 21]) == 12

def test_min_val_41():
    """Test min_val case 41."""
    assert solution.min_val(['oDwGWudYKK', 13, 15, 26]) == 13

def test_min_val_42():
    """Test min_val case 42."""
    assert solution.min_val(['eYfVp', 12, 16, 22]) == 12

def test_min_val_43():
    """Test min_val case 43."""
    assert solution.min_val(['jhm', 12, 22, 24]) == 12

def test_min_val_44():
    """Test min_val case 44."""
    assert solution.min_val(['IeEkrONOEmC', 11, 21, 20]) == 11

def test_min_val_45():
    """Test min_val case 45."""
    assert solution.min_val(['ItK', 20, 23, 22]) == 20

def test_min_val_46():
    """Test min_val case 46."""
    assert solution.min_val(['NplgFGF', 19, 21, 25]) == 19

def test_min_val_47():
    """Test min_val case 47."""
    assert solution.min_val(['gRSQJYRQHkmC', 17, 15, 21]) == 15

def test_min_val_48():
    """Test min_val case 48."""
    assert solution.min_val(['hgVNQkpShHJ', 11, 21, 20]) == 11

def test_min_val_49():
    """Test min_val case 49."""
    assert solution.min_val(['RSCovmS', 20, 25, 28]) == 20

def test_min_val_50():
    """Test min_val case 50."""
    assert solution.min_val(['bjTZS', 11, 15, 22]) == 11

def test_min_val_51():
    """Test min_val case 51."""
    assert solution.min_val(['iieGpcJ', 18, 16, 29]) == 16

def test_min_val_52():
    """Test min_val case 52."""
    assert solution.min_val(['ZmyzUt', 19, 22, 26]) == 19

def test_min_val_53():
    """Test min_val case 53."""
    assert solution.min_val(['CMrKdMZ', 14, 15, 28]) == 14

def test_min_val_54():
    """Test min_val case 54."""
    assert solution.min_val(['HiArCxFqGQa', 20, 20, 24]) == 20

def test_min_val_55():
    """Test min_val case 55."""
    assert solution.min_val(['zzfTT', 19, 21, 20]) == 19

def test_min_val_56():
    """Test min_val case 56."""
    assert solution.min_val(['pifcDG', 18, 16, 28]) == 16

def test_min_val_57():
    """Test min_val case 57."""
    assert solution.min_val(['ObgMOaZ', 12, 21, 20]) == 12

def test_min_val_58():
    """Test min_val case 58."""
    assert solution.min_val(['waqsmrdE', 14, 15, 23]) == 14

def test_min_val_59():
    """Test min_val case 59."""
    assert solution.min_val(['MEvpcqBbU', 10, 16, 29]) == 10

def test_min_val_60():
    """Test min_val case 60."""
    assert solution.min_val(['tmcki', 10, 21, 24]) == 10

def test_min_val_61():
    """Test min_val case 61."""
    assert solution.min_val(['rIIL', 10, 24, 30]) == 10

def test_min_val_62():
    """Test min_val case 62."""
    assert solution.min_val(['swrqQjhFI', 19, 21, 26]) == 19

def test_min_val_63():
    """Test min_val case 63."""
    assert solution.min_val(['jOUPHMJF', 14, 20, 26]) == 14

def test_min_val_64():
    """Test min_val case 64."""
    assert solution.min_val(['pTmgisJ', 16, 16, 24]) == 16

def test_min_val_65():
    """Test min_val case 65."""
    assert solution.min_val(['LVFJrqSdssnW', 15, 18, 20]) == 15

def test_min_val_66():
    """Test min_val case 66."""
    assert solution.min_val(['JmDbU', 18, 18, 22]) == 18

def test_min_val_67():
    """Test min_val case 67."""
    assert solution.min_val(['qwAWZCugaJC', 13, 15, 22]) == 13

def test_min_val_68():
    """Test min_val case 68."""
    assert solution.min_val(['vbqAzmgz', 12, 23, 25]) == 12

def test_min_val_69():
    """Test min_val case 69."""
    assert solution.min_val(['CPqeBdZXAk', 14, 20, 21]) == 14

def test_min_val_70():
    """Test min_val case 70."""
    assert solution.min_val(['xEOyOomyj', 25, 17, 45, 46, 'kpdel']) == 17

def test_min_val_71():
    """Test min_val case 71."""
    assert solution.min_val(['PSyADv', 32, 17, 37, 51, 'nunr']) == 17

def test_min_val_72():
    """Test min_val case 72."""
    assert solution.min_val(['CVVVVsOQFC', 28, 21, 37, 54, 'mvyr']) == 21

def test_min_val_73():
    """Test min_val case 73."""
    assert solution.min_val(['pUBa', 33, 20, 42, 50, 'ydmbrvqjdx']) == 20

def test_min_val_74():
    """Test min_val case 74."""
    assert solution.min_val(['ybFzwIJmTWWu', 30, 19, 37, 54, 'mlbqatrlpqe']) == 19

def test_min_val_75():
    """Test min_val case 75."""
    assert solution.min_val(['tMRDsoemtNs', 26, 15, 45, 51, 'ltboc']) == 15

def test_min_val_76():
    """Test min_val case 76."""
    assert solution.min_val(['COKgtcbO', 25, 16, 45, 52, 'uvrjqagw']) == 16

def test_min_val_77():
    """Test min_val case 77."""
    assert solution.min_val(['fPqdiORl', 32, 19, 41, 50, 'ghyt']) == 19

def test_min_val_78():
    """Test min_val case 78."""
    assert solution.min_val(['SXfumPE', 34, 19, 35, 55, 'wkecied']) == 19

def test_min_val_79():
    """Test min_val case 79."""
    assert solution.min_val(['zTTb', 31, 15, 39, 52, 'pajlvyuro']) == 15

def test_min_val_80():
    """Test min_val case 80."""
    assert solution.min_val(['PRjVeWrL', 30, 23, 42, 51, 'rfwkocnozzje']) == 23

def test_min_val_81():
    """Test min_val case 81."""
    assert solution.min_val(['YJYmbl', 35, 15, 38, 46, 'qjfszjxzz']) == 15

def test_min_val_82():
    """Test min_val case 82."""
    assert solution.min_val(['HBXGT', 33, 19, 45, 46, 'quonxqs']) == 19

def test_min_val_83():
    """Test min_val case 83."""
    assert solution.min_val(['vDn', 31, 25, 45, 51, 'qzhlkv']) == 25

def test_min_val_84():
    """Test min_val case 84."""
    assert solution.min_val(['tJcROflN', 33, 15, 37, 47, 'dotfngwccik']) == 15

def test_min_val_85():
    """Test min_val case 85."""
    assert solution.min_val(['XmbWokQfuv', 28, 15, 44, 53, 'wqayvfvpri']) == 15

def test_min_val_86():
    """Test min_val case 86."""
    assert solution.min_val(['EEy', 35, 15, 41, 51, 'rckhsmmby']) == 15

def test_min_val_87():
    """Test min_val case 87."""
    assert solution.min_val(['lRCN', 25, 20, 40, 55, 'fauxpepj']) == 20

def test_min_val_88():
    """Test min_val case 88."""
    assert solution.min_val(['xiJOQSdiIqpg', 26, 15, 41, 47, 'dbdgiuiist']) == 15

def test_min_val_89():
    """Test min_val case 89."""
    assert solution.min_val(['VbLKXdli', 30, 20, 43, 54, 'urvg']) == 20

def test_min_val_90():
    """Test min_val case 90."""
    assert solution.min_val(['lSaabdATFKe', 35, 20, 40, 55, 'enhlv']) == 20

def test_min_val_91():
    """Test min_val case 91."""
    assert solution.min_val(['FZUMTCTX', 33, 19, 40, 52, 'wrao']) == 19

def test_min_val_92():
    """Test min_val case 92."""
    assert solution.min_val(['qizItX', 33, 21, 39, 50, 'jtjp']) == 21

def test_min_val_93():
    """Test min_val case 93."""
    assert solution.min_val(['DcNmOF', 28, 15, 35, 54, 'qvlbjqopzu']) == 15

def test_min_val_94():
    """Test min_val case 94."""
    assert solution.min_val(['MxccVMwPrLMz', 28, 15, 36, 55, 'uhduvjppqlh']) == 15

def test_min_val_95():
    """Test min_val case 95."""
    assert solution.min_val(['paamd', 34, 16, 42, 54, 'wfsaafyu']) == 16

def test_min_val_96():
    """Test min_val case 96."""
    assert solution.min_val(['dPZvtpI', 29, 16, 45, 47, 'iszqs']) == 16

def test_min_val_97():
    """Test min_val case 97."""
    assert solution.min_val(['Sua', 30, 24, 42, 48, 'qneek']) == 24

def test_min_val_98():
    """Test min_val case 98."""
    assert solution.min_val(['CcQeyPtva', 32, 24, 37, 50, 'fyzg']) == 24

def test_min_val_99():
    """Test min_val case 99."""
    assert solution.min_val(['nWZSJvIqyvQ', 35, 19, 37, 49, 'mhyvvdas']) == 19

def test_min_val_100():
    """Test min_val case 100."""
    assert solution.min_val(['NgjVlijoj', 26, 23, 40, 45, 'ivoqgxtmumcs']) == 23

def test_min_val_101():
    """Test min_val case 101."""
    assert solution.min_val(['TYNHbzm', 29, 16, 44, 46, 'nlaltmiw']) == 16

def test_min_val_102():
    """Test min_val case 102."""
    assert solution.min_val(['zGWj', 35, 21, 35, 46, 'cemxckmva']) == 21
