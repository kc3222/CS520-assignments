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


#iteration 1
def test_empty_k_line_then_valid(monkeypatch, capsys):
    """Test when k_line is empty, then reads valid k."""
    input_str = 'abc\n\n3\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == '0\n', f'Expected 0\n, got {captured.out!r}'


def test_multiple_empty_lines(monkeypatch, capsys):
    """Test with empty line before k."""
    # 'xyz' has 3 distinct chars, k=3, so output is 0
    input_str = 'xyz\n\n3\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == '0\n', f'Expected 0\n, got {captured.out!r}'


def test_k_equals_length(monkeypatch, capsys):
    """Test when k equals string length (boundary case)."""
    input_str = 'abc\n3\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == '0\n', f'Expected 0\n, got {captured.out!r}'


def test_k_one_less_than_length(monkeypatch, capsys):
    """Test when k is one less than string length."""
    input_str = 'abcd\n3\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == '0\n', f'Expected 0\n, got {captured.out!r}'


def test_k_one_more_than_length(monkeypatch, capsys):
    """Test when k is one more than string length (impossible)."""
    input_str = 'abc\n4\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == 'impossible\n', f'Expected impossible\n, got {captured.out!r}'


def test_all_same_characters(monkeypatch, capsys):
    """Test with all same characters."""
    input_str = 'aaaaa\n3\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == '2\n', f'Expected 2\n, got {captured.out!r}'


def test_max_distinct_chars(monkeypatch, capsys):
    """Test with maximum distinct characters."""
    input_str = 'abcdefghijklmnopqrstuvwxyz\n26\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == '0\n', f'Expected 0\n, got {captured.out!r}'


def test_max_distinct_plus_one(monkeypatch, capsys):
    """Test with k one more than distinct characters."""
    input_str = 'abc\n4\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == 'impossible\n', f'Expected impossible\n, got {captured.out!r}'


def test_single_char_k_one(monkeypatch, capsys):
    """Test single character with k=1."""
    input_str = 'a\n1\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == '0\n', f'Expected 0\n, got {captured.out!r}'


def test_single_char_k_two(monkeypatch, capsys):
    """Test single character with k=2."""
    input_str = 'a\n2\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == 'impossible\n', f'Expected impossible\n, got {captured.out!r}'


def test_long_string_small_k(monkeypatch, capsys):
    """Test long string with small k."""
    input_str = 'abcdefghijklmnopqrstuvwxyz\n5\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == '0\n', f'Expected 0\n, got {captured.out!r}'


def test_repeated_pattern(monkeypatch, capsys):
    """Test with repeated pattern."""
    input_str = 'abababab\n5\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    assert captured.out == '3\n', f'Expected 3\n, got {captured.out!r}'


def test_whitespace_in_string(monkeypatch, capsys):
    """Test with string that may have whitespace (though strip() handles it)."""
    input_str = '  test  \n4\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))
    VqfyF()
    captured = capsys.readouterr()
    # After strip(), 'test' has 4 distinct chars, k=4, so output is 0
    assert captured.out == '1\n', f'Expected 1\n, got {captured.out!r}'

