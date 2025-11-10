import pytest
from io import StringIO
import sys
from solution import VqfyF


@pytest.mark.parametrize("input_str,expected", [
    ('yandex\n6\n', '0\n'),
    ('yahoo\n5\n', '1\n'),
    ('google\n7\n', 'impossible\n'),
    ('a\n1\n', '0\n'),
    ('z\n2\n', 'impossible\n'),
    ('fwgfrwgkuwghfiruhewgirueguhergiqrbvgrgf\n26\n', '14\n'),
    ('nfevghreuoghrueighoqghbnebvnejbvnbgneluqe\n26\n', '12\n'),
    ('a\n3\n', 'impossible\n'),
    ('smaxpqplaqqbxuqxalqmbmmgubbpspxhawbxsuqhhegpmmpebqmqpbbeplwaepxmsahuepuhuhwxeqmmlgqubuaxehwuwasgxpqmugbmuawuhwqlswllssueglbxepbmwgs\n1\n', '0\n'),
    ('cuguccgcugcugucgggggcgcgucgucugcuuuccccuugccg\n4\n', '1\n'),
    ('fcfccfcfccfcfcffcffffffcfccfccfcffccccfcffffccfccfcffcfcccccffcfffcccffcfccfffffcccfccffffffccfccccf\n20\n', '18\n'),
    ('swmkwaruyv\n5\n', '0\n'),
    ('tnbqpsuhkczmejirvyfdolxwga\n22\n', '0\n'),
    ('abcde\n3\n', '0\n'),
    ('abb\n1\n', '0\n'),
    ('aaaa\n1\n', '0\n'),
    ('abcde\n2\n', '0\n'),
    ('yandex\n4\n', '0\n'),
    ('aaabbbccc\n1\n', '0\n'),
    ('abcd\n2\n', '0\n'),
    ('asdfgh\n2\n', '0\n'),
    ('aab\n1\n', '0\n'),
    ('mynameissako\n5\n', '0\n'),
    ('abcde\n1\n', '0\n'),
    ('abcd\n3\n', '0\n'),
    ('abcdef\n2\n', '0\n'),
    ('abcdefg\n4\n', '0\n'),
    ('abc\n1\n', '0\n'),
    ('asdafjsgljdllgjdgkl\n5\n', '0\n'),
    ('yaay\n3\n', '1\n'),
    ('yaay\n4\n', '2\n'),
    ('zzzzzz\n2\n', '1\n'),
])
def test_solution(input_str, expected, monkeypatch, capsys):
    """Test VqfyF function with various inputs."""
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == expected, f'Expected {expected!r}, got {captured.out!r}'

