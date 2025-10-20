'''chatgpt'''
'''cot'''
import math

def min_val(listval):
    m = None
    for x in listval:
        if isinstance(x, bool):
            continue
        if isinstance(x, (int, float)):
            if isinstance(x, float) and math.isnan(x):
                continue
            if m is None or x < m:
                m = x
    return m

import math

def min_val(listval):
    m = None
    for x in listval:
        if isinstance(x, bool):
            continue
        if isinstance(x, (int, float)):
            if isinstance(x, float) and math.isnan(x):
                continue
            if m is None or x < m:
                m = x
    return m

import math

def min_val(listval):
    m = None
    for x in listval:
        if isinstance(x, bool):
            continue
        if isinstance(x, (int, float)):
            if isinstance(x, float) and math.isnan(x):
                continue
            if m is None or x < m:
                m = x
    return m

'''self-planning'''
def min_val(listval):
    nums = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return min(nums) if nums else None

def min_val(listval):
    nums = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return min(nums) if nums else None

def min_val(listval):
    nums = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return min(nums) if nums else None

'''claude'''
'''cot'''
def min_val(listval):
    numeric_values = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    if not numeric_values:
        return None
    return min(numeric_values)

def min_val(listval):
    numeric_values = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    if not numeric_values:
        return None
    return min(numeric_values)

def min_val(listval):
    numeric_values = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    if not numeric_values:
        return None
    return min(numeric_values)

'''self-planning'''
def min_val(listval):
    numeric_values = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return min(numeric_values) if numeric_values else None

def min_val(listval):
    numeric_values = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return min(numeric_values) if numeric_values else None

def min_val(listval):
    numeric_values = [x for x in listval if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return min(numeric_values) if numeric_values else None

assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
assert min_val(['Python', 15, 20, 25])==15
assert min_val(['Python', 30, 20, 40, 50, 'version'])==20
assert min_val(['Hzgn', 8, 2, 6, 3, 'rnjxdg']) == 2
assert min_val(['smGoJ', 3, 6, 6, 3, 'orvw']) == 3
assert min_val(['hJXuNEvHE', 2, 5, 7, 9, 'hbn']) == 2
assert min_val(['HstmSajZT', 2, 4, 4, 9, 'qsfmpgliekx']) == 2
assert min_val(['LDsJJQbL', 3, 2, 6, 8, 'weptakuf']) == 2
assert min_val(['QIrO', 2, 1, 7, 2, 'dictnghn']) == 1
assert min_val(['wAUEw', 4, 6, 9, 8, 'ofeau']) == 4
assert min_val(['XISeqgLUeu', 5, 1, 7, 2, 'bkyy']) == 1
assert min_val(['OjJCC', 1, 6, 6, 1, 'xldewi']) == 1
assert min_val(['LUeFL', 1, 5, 5, 7, 'uqxlqznrv']) == 1
assert min_val(['syHRbRpq', 5, 5, 2, 8, 'siyxhciiskhc']) == 2
assert min_val(['HeHgPo', 6, 3, 1, 8, 'fge']) == 1
assert min_val(['Lno', 4, 1, 9, 6, 'gfz']) == 1
assert min_val(['eUjaqNfdsfZV', 6, 7, 5, 7, 'aehukfbtua']) == 5
assert min_val(['FlXZOMZQ', 3, 2, 9, 2, 'gkuvqyh']) == 2
assert min_val(['ICNIULJ', 7, 2, 6, 5, 'hscazrhrlxqt']) == 2
assert min_val(['KQYa', 1, 5, 5, 4, 'iesmreyufgf']) == 1
assert min_val(['kSYdtspqDG', 4, 4, 4, 2, 'llofkv']) == 2
assert min_val(['vYqB', 3, 4, 3, 2, 'otixcfybon']) == 2
assert min_val(['LwDZ', 2, 1, 6, 1, 'bpddrpprasw']) == 1
assert min_val(['KliVODcNIbJc', 3, 3, 9, 6, 'henrl']) == 3
assert min_val(['OYPlumF', 3, 3, 8, 6, 'iliy']) == 3
assert min_val(['sQu', 1, 4, 4, 9, 'vkgfidlmzy']) == 1
assert min_val(['OmaC', 7, 6, 2, 5, 'zgxokgnuisi']) == 2
assert min_val(['fCttsVY', 4, 6, 1, 8, 'xecsbkn']) == 1
assert min_val(['XQjWs', 1, 1, 7, 10, 'heqam']) == 1
assert min_val(['adRuGajh', 6, 1, 2, 2, 'tijocjzucq']) == 1
assert min_val(['xbnshYBm', 1, 3, 3, 4, 'pbefhjlb']) == 1
assert min_val(['ywS', 2, 2, 1, 2, 'tryknyj']) == 1
assert min_val(['vKysfe', 1, 3, 8, 5, 'azng']) == 1
assert min_val(['HgTnglhornr', 7, 3, 8, 10, 'wic']) == 3
assert min_val(['NwqdqjBBPk', 5, 4, 3, 9, 'pgi']) == 3
assert min_val(['Nln', 2, 6, 8, 1, 'hnf']) == 1
assert min_val(['yzCjPw', 10, 19, 21]) == 10
assert min_val(['ddckbcme', 18, 25, 30]) == 18
assert min_val(['enHpxvrPUEN', 10, 21, 28]) == 10
assert min_val(['xIdWszWpgsh', 12, 16, 21]) == 12
assert min_val(['oDwGWudYKK', 13, 15, 26]) == 13
assert min_val(['eYfVp', 12, 16, 22]) == 12
assert min_val(['jhm', 12, 22, 24]) == 12
assert min_val(['IeEkrONOEmC', 11, 21, 20]) == 11
assert min_val(['ItK', 20, 23, 22]) == 20
assert min_val(['NplgFGF', 19, 21, 25]) == 19
assert min_val(['gRSQJYRQHkmC', 17, 15, 21]) == 15
assert min_val(['hgVNQkpShHJ', 11, 21, 20]) == 11
assert min_val(['RSCovmS', 20, 25, 28]) == 20
assert min_val(['bjTZS', 11, 15, 22]) == 11
assert min_val(['iieGpcJ', 18, 16, 29]) == 16
assert min_val(['ZmyzUt', 19, 22, 26]) == 19
assert min_val(['CMrKdMZ', 14, 15, 28]) == 14
assert min_val(['HiArCxFqGQa', 20, 20, 24]) == 20
assert min_val(['zzfTT', 19, 21, 20]) == 19
assert min_val(['pifcDG', 18, 16, 28]) == 16
assert min_val(['ObgMOaZ', 12, 21, 20]) == 12
assert min_val(['waqsmrdE', 14, 15, 23]) == 14
assert min_val(['MEvpcqBbU', 10, 16, 29]) == 10
assert min_val(['tmcki', 10, 21, 24]) == 10
assert min_val(['rIIL', 10, 24, 30]) == 10
assert min_val(['swrqQjhFI', 19, 21, 26]) == 19
assert min_val(['jOUPHMJF', 14, 20, 26]) == 14
assert min_val(['pTmgisJ', 16, 16, 24]) == 16
assert min_val(['LVFJrqSdssnW', 15, 18, 20]) == 15
assert min_val(['JmDbU', 18, 18, 22]) == 18
assert min_val(['qwAWZCugaJC', 13, 15, 22]) == 13
assert min_val(['vbqAzmgz', 12, 23, 25]) == 12
assert min_val(['CPqeBdZXAk', 14, 20, 21]) == 14
assert min_val(['xEOyOomyj', 25, 17, 45, 46, 'kpdel']) == 17
assert min_val(['PSyADv', 32, 17, 37, 51, 'nunr']) == 17
assert min_val(['CVVVVsOQFC', 28, 21, 37, 54, 'mvyr']) == 21
assert min_val(['pUBa', 33, 20, 42, 50, 'ydmbrvqjdx']) == 20
assert min_val(['ybFzwIJmTWWu', 30, 19, 37, 54, 'mlbqatrlpqe']) == 19
assert min_val(['tMRDsoemtNs', 26, 15, 45, 51, 'ltboc']) == 15
assert min_val(['COKgtcbO', 25, 16, 45, 52, 'uvrjqagw']) == 16
assert min_val(['fPqdiORl', 32, 19, 41, 50, 'ghyt']) == 19
assert min_val(['SXfumPE', 34, 19, 35, 55, 'wkecied']) == 19
assert min_val(['zTTb', 31, 15, 39, 52, 'pajlvyuro']) == 15
assert min_val(['PRjVeWrL', 30, 23, 42, 51, 'rfwkocnozzje']) == 23
assert min_val(['YJYmbl', 35, 15, 38, 46, 'qjfszjxzz']) == 15
assert min_val(['HBXGT', 33, 19, 45, 46, 'quonxqs']) == 19
assert min_val(['vDn', 31, 25, 45, 51, 'qzhlkv']) == 25
assert min_val(['tJcROflN', 33, 15, 37, 47, 'dotfngwccik']) == 15
assert min_val(['XmbWokQfuv', 28, 15, 44, 53, 'wqayvfvpri']) == 15
assert min_val(['EEy', 35, 15, 41, 51, 'rckhsmmby']) == 15
assert min_val(['lRCN', 25, 20, 40, 55, 'fauxpepj']) == 20
assert min_val(['xiJOQSdiIqpg', 26, 15, 41, 47, 'dbdgiuiist']) == 15
assert min_val(['VbLKXdli', 30, 20, 43, 54, 'urvg']) == 20
assert min_val(['lSaabdATFKe', 35, 20, 40, 55, 'enhlv']) == 20
assert min_val(['FZUMTCTX', 33, 19, 40, 52, 'wrao']) == 19
assert min_val(['qizItX', 33, 21, 39, 50, 'jtjp']) == 21
assert min_val(['DcNmOF', 28, 15, 35, 54, 'qvlbjqopzu']) == 15
assert min_val(['MxccVMwPrLMz', 28, 15, 36, 55, 'uhduvjppqlh']) == 15
assert min_val(['paamd', 34, 16, 42, 54, 'wfsaafyu']) == 16
assert min_val(['dPZvtpI', 29, 16, 45, 47, 'iszqs']) == 16
assert min_val(['Sua', 30, 24, 42, 48, 'qneek']) == 24
assert min_val(['CcQeyPtva', 32, 24, 37, 50, 'fyzg']) == 24
assert min_val(['nWZSJvIqyvQ', 35, 19, 37, 49, 'mhyvvdas']) == 19
assert min_val(['NgjVlijoj', 26, 23, 40, 45, 'ivoqgxtmumcs']) == 23
assert min_val(['TYNHbzm', 29, 16, 44, 46, 'nlaltmiw']) == 16
assert min_val(['zGWj', 35, 21, 35, 46, 'cemxckmva']) == 21