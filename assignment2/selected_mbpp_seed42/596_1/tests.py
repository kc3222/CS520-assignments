"""Test cases using pytest."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent))
import solution

def test_tuple_size_1():
    """Test tuple_size case 1."""
    assert solution.tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))

def test_tuple_size_2():
    """Test tuple_size case 2."""
    assert solution.tuple_size((1, "Raju", 2, "Nikhil", 3, "Deepanshu") ) == sys.getsizeof((1, "Raju", 2, "Nikhil", 3, "Deepanshu"))

def test_tuple_size_3():
    """Test tuple_size case 3."""
    assert solution.tuple_size(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))  ) == sys.getsizeof(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")))

def test_tuple_size_4():
    """Test tuple_size case 4."""
    assert solution.tuple_size(('F', 1, 'X', 3, 'J', 2)) == 88

def test_tuple_size_5():
    """Test tuple_size case 5."""
    assert solution.tuple_size(('K', 4, 'J', 2, 'D', 3)) == 88

def test_tuple_size_6():
    """Test tuple_size case 6."""
    assert solution.tuple_size(('I', 1, 'U', 3, 'S', 7)) == 88

def test_tuple_size_7():
    """Test tuple_size case 7."""
    assert solution.tuple_size(('M', 4, 'D', 2, 'P', 8)) == 88

def test_tuple_size_8():
    """Test tuple_size case 8."""
    assert solution.tuple_size(('N', 6, 'F', 2, 'W', 1)) == 88

def test_tuple_size_9():
    """Test tuple_size case 9."""
    assert solution.tuple_size(('E', 3, 'S', 3, 'M', 3)) == 88

def test_tuple_size_10():
    """Test tuple_size case 10."""
    assert solution.tuple_size(('F', 5, 'I', 6, 'O', 3)) == 88

def test_tuple_size_11():
    """Test tuple_size case 11."""
    assert solution.tuple_size(('E', 4, 'F', 3, 'R', 3)) == 88

def test_tuple_size_12():
    """Test tuple_size case 12."""
    assert solution.tuple_size(('S', 4, 'M', 1, 'D', 7)) == 88

def test_tuple_size_13():
    """Test tuple_size case 13."""
    assert solution.tuple_size(('H', 2, 'O', 3, 'G', 4)) == 88

def test_tuple_size_14():
    """Test tuple_size case 14."""
    assert solution.tuple_size(('N', 2, 'V', 3, 'L', 1)) == 88

def test_tuple_size_15():
    """Test tuple_size case 15."""
    assert solution.tuple_size(('A', 4, 'Y', 5, 'K', 1)) == 88

def test_tuple_size_16():
    """Test tuple_size case 16."""
    assert solution.tuple_size(('H', 5, 'M', 4, 'B', 3)) == 88

def test_tuple_size_17():
    """Test tuple_size case 17."""
    assert solution.tuple_size(('L', 4, 'K', 7, 'W', 5)) == 88

def test_tuple_size_18():
    """Test tuple_size case 18."""
    assert solution.tuple_size(('U', 4, 'O', 1, 'Y', 3)) == 88

def test_tuple_size_19():
    """Test tuple_size case 19."""
    assert solution.tuple_size(('L', 3, 'A', 2, 'B', 5)) == 88

def test_tuple_size_20():
    """Test tuple_size case 20."""
    assert solution.tuple_size(('F', 4, 'H', 4, 'R', 2)) == 88

def test_tuple_size_21():
    """Test tuple_size case 21."""
    assert solution.tuple_size(('X', 6, 'S', 1, 'Q', 3)) == 88

def test_tuple_size_22():
    """Test tuple_size case 22."""
    assert solution.tuple_size(('M', 4, 'W', 2, 'U', 7)) == 88

def test_tuple_size_23():
    """Test tuple_size case 23."""
    assert solution.tuple_size(('D', 6, 'A', 5, 'J', 3)) == 88

def test_tuple_size_24():
    """Test tuple_size case 24."""
    assert solution.tuple_size(('Y', 4, 'M', 5, 'T', 8)) == 88

def test_tuple_size_25():
    """Test tuple_size case 25."""
    assert solution.tuple_size(('L', 1, 'J', 1, 'Z', 5)) == 88

def test_tuple_size_26():
    """Test tuple_size case 26."""
    assert solution.tuple_size(('A', 5, 'H', 2, 'D', 3)) == 88

def test_tuple_size_27():
    """Test tuple_size case 27."""
    assert solution.tuple_size(('U', 1, 'V', 6, 'U', 5)) == 88

def test_tuple_size_28():
    """Test tuple_size case 28."""
    assert solution.tuple_size(('I', 4, 'Z', 2, 'L', 4)) == 88

def test_tuple_size_29():
    """Test tuple_size case 29."""
    assert solution.tuple_size(('C', 3, 'M', 4, 'K', 8)) == 88

def test_tuple_size_30():
    """Test tuple_size case 30."""
    assert solution.tuple_size(('I', 2, 'U', 4, 'M', 2)) == 88

def test_tuple_size_31():
    """Test tuple_size case 31."""
    assert solution.tuple_size(('F', 2, 'L', 4, 'N', 4)) == 88

def test_tuple_size_32():
    """Test tuple_size case 32."""
    assert solution.tuple_size(('G', 1, 'U', 6, 'P', 2)) == 88

def test_tuple_size_33():
    """Test tuple_size case 33."""
    assert solution.tuple_size(('Y', 6, 'P', 6, 'A', 8)) == 88

def test_tuple_size_34():
    """Test tuple_size case 34."""
    assert solution.tuple_size(('K', 3, 'N', 7, 'X', 6)) == 88

def test_tuple_size_35():
    """Test tuple_size case 35."""
    assert solution.tuple_size(('U', 2, 'S', 7, 'U', 7)) == 88

def test_tuple_size_36():
    """Test tuple_size case 36."""
    assert solution.tuple_size(('X', 6, 'W', 7, 'J', 6)) == 88

def test_tuple_size_37():
    """Test tuple_size case 37."""
    assert solution.tuple_size((1, 'VfvTtfeBr', 1, 'GFOmhdZEawD', 4, 'gFGYZR')) == 88

def test_tuple_size_38():
    """Test tuple_size case 38."""
    assert solution.tuple_size((2, 'eaxzWi', 5, 'BBhdWSmcPKWW', 5, 'icvdRkGQuDFo')) == 88

def test_tuple_size_39():
    """Test tuple_size case 39."""
    assert solution.tuple_size((2, 'EfGbQXkRq', 1, 'fyh', 2, 'gJlAJe')) == 88

def test_tuple_size_40():
    """Test tuple_size case 40."""
    assert solution.tuple_size((3, 'kfOA', 1, 'dpPpDYDBnP', 1, 'NuwkmxilqF')) == 88

def test_tuple_size_41():
    """Test tuple_size case 41."""
    assert solution.tuple_size((6, 'dUEYlju', 5, 'lLmetbfHzULs', 4, 'CwcYCKj')) == 88

def test_tuple_size_42():
    """Test tuple_size case 42."""
    assert solution.tuple_size((2, 'ATbiT', 5, 'vEKNzRGMYYy', 4, 'SmlvExBO')) == 88

def test_tuple_size_43():
    """Test tuple_size case 43."""
    assert solution.tuple_size((1, 'IYMu', 4, 'JpNtU', 7, 'iCrJpSka')) == 88

def test_tuple_size_44():
    """Test tuple_size case 44."""
    assert solution.tuple_size((4, 'YDvdiKQ', 5, 'foMie', 4, 'okNgkniSnfOHTmd')) == 88

def test_tuple_size_45():
    """Test tuple_size case 45."""
    assert solution.tuple_size((3, 'fey', 4, 'eLJap', 6, 'EpglLbuMMWDZ')) == 88

def test_tuple_size_46():
    """Test tuple_size case 46."""
    assert solution.tuple_size((4, 'nNaSKEAv', 2, 'bSEJ', 8, 'PhoWmYms')) == 88

def test_tuple_size_47():
    """Test tuple_size case 47."""
    assert solution.tuple_size((2, 'YIFGFcA', 7, 'dTK', 2, 'QSqSCZeeIVWD')) == 88

def test_tuple_size_48():
    """Test tuple_size case 48."""
    assert solution.tuple_size((1, 'KEd', 4, 'oDiNrsqAnLYO', 4, 'qATLmuo')) == 88

def test_tuple_size_49():
    """Test tuple_size case 49."""
    assert solution.tuple_size((5, 'CEYddSo', 3, 'AzoPcVpCo', 1, 'repSUMMV')) == 88

def test_tuple_size_50():
    """Test tuple_size case 50."""
    assert solution.tuple_size((5, 'MVRnMMi', 3, 'Aqvawda', 1, 'djYTVWrIvymOzMs')) == 88

def test_tuple_size_51():
    """Test tuple_size case 51."""
    assert solution.tuple_size((4, 'wPlZ', 1, 'aQDLkj', 1, 'VaAiqxDIOwjLy')) == 88

def test_tuple_size_52():
    """Test tuple_size case 52."""
    assert solution.tuple_size((6, 'TsmLf', 4, 'fGU', 5, 'xMwkxVtltXpAfZ')) == 88

def test_tuple_size_53():
    """Test tuple_size case 53."""
    assert solution.tuple_size((5, 'kOa', 4, 'qEDklItxsQbJ', 3, 'xqspTtnL')) == 88

def test_tuple_size_54():
    """Test tuple_size case 54."""
    assert solution.tuple_size((1, 'etwbdAi', 1, 'iGdKXaHByH', 3, 'mgFbfXcms')) == 88

def test_tuple_size_55():
    """Test tuple_size case 55."""
    assert solution.tuple_size((4, 'jDjfGG', 7, 'bNqgIHLY', 6, 'BUBcMWVNlaKs')) == 88

def test_tuple_size_56():
    """Test tuple_size case 56."""
    assert solution.tuple_size((5, 'DrnETjIE', 5, 'XYGtydtl', 4, 'fuFTmzHoeR')) == 88

def test_tuple_size_57():
    """Test tuple_size case 57."""
    assert solution.tuple_size((4, 'PIjsxd', 2, 'SDxFkGluM', 4, 'XfubjxI')) == 88

def test_tuple_size_58():
    """Test tuple_size case 58."""
    assert solution.tuple_size((4, 'CVZcfJGbe', 2, 'wOwnGZQFNKl', 6, 'SqSqNtKzrafa')) == 88

def test_tuple_size_59():
    """Test tuple_size case 59."""
    assert solution.tuple_size((1, 'DenxP', 4, 'dBviqU', 5, 'JLJbBGNOfuAJu')) == 88

def test_tuple_size_60():
    """Test tuple_size case 60."""
    assert solution.tuple_size((3, 'tcpYVAxQ', 3, 'wrHOTmKNd', 4, 'WKcCmBVk')) == 88

def test_tuple_size_61():
    """Test tuple_size case 61."""
    assert solution.tuple_size((5, 'pKIvQ', 7, 'MBvRHJK', 7, 'ithZUtr')) == 88

def test_tuple_size_62():
    """Test tuple_size case 62."""
    assert solution.tuple_size((2, 'VEttMU', 1, 'YJAdZhPD', 6, 'JqDgEqZdsTJO')) == 88

def test_tuple_size_63():
    """Test tuple_size case 63."""
    assert solution.tuple_size((2, 'avAKG', 3, 'tSidpJb', 2, 'xdHfefJRMdHT')) == 88

def test_tuple_size_64():
    """Test tuple_size case 64."""
    assert solution.tuple_size((6, 'fGhO', 4, 'TaNtOxFMsc', 6, 'BDGjbixXJNICux')) == 88

def test_tuple_size_65():
    """Test tuple_size case 65."""
    assert solution.tuple_size((3, 'AphfwyzD', 4, 'hRsDPvKjyR', 4, 'QUWhyiihirXI')) == 88

def test_tuple_size_66():
    """Test tuple_size case 66."""
    assert solution.tuple_size((5, 'JHozm', 2, 'kaQtHhevVtGz', 8, 'HLaWBfFTxM')) == 88

def test_tuple_size_67():
    """Test tuple_size case 67."""
    assert solution.tuple_size((2, 'guPst', 7, 'EcBGO', 5, 'jYoaGsvG')) == 88

def test_tuple_size_68():
    """Test tuple_size case 68."""
    assert solution.tuple_size((5, 'vbgL', 2, 'igPzyFfdN', 5, 'LSmONfS')) == 88

def test_tuple_size_69():
    """Test tuple_size case 69."""
    assert solution.tuple_size((2, 'XAPuQ', 2, 'QFsc', 4, 'OuYEQIMkiDB')) == 88

def test_tuple_size_70():
    """Test tuple_size case 70."""
    assert solution.tuple_size(((4, 'ewaZSjVtH'), (5, 'DUMQwyY'), (5, 'PsExP'), (2, 'JJEOKbCB'))) == 72

def test_tuple_size_71():
    """Test tuple_size case 71."""
    assert solution.tuple_size(((4, 'YRFCH'), (5, 'MzTb'), (2, 'DGZEA'), (5, 'AutwFltD'))) == 72

def test_tuple_size_72():
    """Test tuple_size case 72."""
    assert solution.tuple_size(((6, 'AFD'), (4, 'dMei'), (3, 'LlFgTfRnM'), (6, 'aLibgHkr'))) == 72

def test_tuple_size_73():
    """Test tuple_size case 73."""
    assert solution.tuple_size(((5, 'ElUVSKv'), (4, 'cyr'), (2, 'UDgkGJFP'), (7, 'conYhLVT'))) == 72

def test_tuple_size_74():
    """Test tuple_size case 74."""
    assert solution.tuple_size(((2, 'akfVlBi'), (5, 'plI'), (8, 'wwlJcTh'), (6, 'LgpiXnUD'))) == 72

def test_tuple_size_75():
    """Test tuple_size case 75."""
    assert solution.tuple_size(((6, 'dKsoS'), (5, 'vLG'), (2, 'FqGAVA'), (6, 'JRWwNL'))) == 72

def test_tuple_size_76():
    """Test tuple_size case 76."""
    assert solution.tuple_size(((1, 'MxMflsE'), (5, 'OOPDuXQG'), (7, 'QDr'), (2, 'OxMgEc'))) == 72

def test_tuple_size_77():
    """Test tuple_size case 77."""
    assert solution.tuple_size(((6, 'AAMe'), (5, 'azto'), (7, 'uLGSEWYLz'), (4, 'eeBc'))) == 72

def test_tuple_size_78():
    """Test tuple_size case 78."""
    assert solution.tuple_size(((3, 'FRjUG'), (1, 'WUtA'), (4, 'PDhnTGpa'), (1, 'KfPNoaQs'))) == 72

def test_tuple_size_79():
    """Test tuple_size case 79."""
    assert solution.tuple_size(((1, 'ugxHB'), (2, 'VJUnKIn'), (6, 'kopaANJCh'), (6, 'vFfTwtZr'))) == 72

def test_tuple_size_80():
    """Test tuple_size case 80."""
    assert solution.tuple_size(((5, 'hiMxCp'), (7, 'FjTFR'), (1, 'nTNEtVgn'), (7, 'tdECh'))) == 72

def test_tuple_size_81():
    """Test tuple_size case 81."""
    assert solution.tuple_size(((4, 'PDfhkTox'), (5, 'WwBvw'), (6, 'UaqVPzm'), (5, 'Cdr'))) == 72

def test_tuple_size_82():
    """Test tuple_size case 82."""
    assert solution.tuple_size(((4, 'DRBtNbap'), (5, 'tQJCxj'), (2, 'TCxtQ'), (7, 'TCLasImyq'))) == 72

def test_tuple_size_83():
    """Test tuple_size case 83."""
    assert solution.tuple_size(((1, 'otri'), (3, 'MYZWZ'), (8, 'SqQ'), (7, 'rTJJZNkjk'))) == 72

def test_tuple_size_84():
    """Test tuple_size case 84."""
    assert solution.tuple_size(((3, 'SSvmYcV'), (1, 'yGgkx'), (8, 'zSpWCn'), (5, 'GbKXiDYB'))) == 72

def test_tuple_size_85():
    """Test tuple_size case 85."""
    assert solution.tuple_size(((4, 'UIPzR'), (1, 'gaKQyGaA'), (4, 'PCpCkNGRJ'), (6, 'XjGeG'))) == 72

def test_tuple_size_86():
    """Test tuple_size case 86."""
    assert solution.tuple_size(((2, 'jJmEbiRq'), (2, 'DeYCYi'), (6, 'ZTkiXd'), (1, 'IxFon'))) == 72

def test_tuple_size_87():
    """Test tuple_size case 87."""
    assert solution.tuple_size(((2, 'mnZx'), (7, 'hnVjeXts'), (1, 'zRSSgG'), (3, 'XNzkYuQtZ'))) == 72

def test_tuple_size_88():
    """Test tuple_size case 88."""
    assert solution.tuple_size(((1, 'KkUoaNTR'), (4, 'YZqpRUk'), (5, 'hFSRbTJxX'), (4, 'rdZziC'))) == 72

def test_tuple_size_89():
    """Test tuple_size case 89."""
    assert solution.tuple_size(((2, 'GEh'), (4, 'MqKy'), (1, 'kRjtiy'), (2, 'MfEriv'))) == 72

def test_tuple_size_90():
    """Test tuple_size case 90."""
    assert solution.tuple_size(((1, 'vZb'), (6, 'IRExUOOcx'), (5, 'OmJUpbu'), (9, 'eTmbFlm'))) == 72

def test_tuple_size_91():
    """Test tuple_size case 91."""
    assert solution.tuple_size(((1, 'bWbeX'), (4, 'WaL'), (3, 'eef'), (2, 'ZkS'))) == 72

def test_tuple_size_92():
    """Test tuple_size case 92."""
    assert solution.tuple_size(((5, 'YrAdp'), (3, 'awZFTF'), (1, 'boeXmxrH'), (8, 'ZDCwgfy'))) == 72

def test_tuple_size_93():
    """Test tuple_size case 93."""
    assert solution.tuple_size(((5, 'fyFO'), (3, 'qNB'), (2, 'rczqsL'), (8, 'FkBh'))) == 72

def test_tuple_size_94():
    """Test tuple_size case 94."""
    assert solution.tuple_size(((6, 'YGaJ'), (1, 'tRp'), (3, 'QPf'), (6, 'LcgCb'))) == 72

def test_tuple_size_95():
    """Test tuple_size case 95."""
    assert solution.tuple_size(((3, 'PvGARhk'), (4, 'tBkyB'), (5, 'NxmGU'), (4, 'zWkvThl'))) == 72

def test_tuple_size_96():
    """Test tuple_size case 96."""
    assert solution.tuple_size(((2, 'ocGxd'), (7, 'KCNTdRA'), (7, 'nxxeTcfA'), (4, 'pcZnfNa'))) == 72

def test_tuple_size_97():
    """Test tuple_size case 97."""
    assert solution.tuple_size(((4, 'daCudS'), (3, 'gRf'), (5, 'yFTJb'), (3, 'UGSFpYXv'))) == 72

def test_tuple_size_98():
    """Test tuple_size case 98."""
    assert solution.tuple_size(((3, 'itMXtUw'), (4, 'WnqhU'), (4, 'yqIr'), (4, 'uofMtM'))) == 72

def test_tuple_size_99():
    """Test tuple_size case 99."""
    assert solution.tuple_size(((1, 'tgVm'), (5, 'DlcdNYIgu'), (6, 'Nwat'), (1, 'RzNoSGM'))) == 72

def test_tuple_size_100():
    """Test tuple_size case 100."""
    assert solution.tuple_size(((3, 'BfQomrtY'), (7, 'dRB'), (3, 'eEeEHA'), (6, 'BOXNwNf'))) == 72

def test_tuple_size_101():
    """Test tuple_size case 101."""
    assert solution.tuple_size(((5, 'ZqWoc'), (7, 'WZeBze'), (6, 'HkowjYrKi'), (2, 'ovHD'))) == 72

def test_tuple_size_102():
    """Test tuple_size case 102."""
    assert solution.tuple_size(((3, 'AIrUzb'), (2, 'icXOhjbO'), (2, 'abe'), (1, 'WosMYDQ'))) == 72
