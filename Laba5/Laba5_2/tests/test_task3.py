import pytest

from task3 import is_palindrome

@pytest.mark.parametrize("input_value,expected", [
    # Строки-палиндромы
    ("radar", True),
    ("level", True),
    ("deified", True),
    ("a", True),
    ("", True),
    ("12321", True),
    
    # Строки не палиндромы
    ("hello", False),
    ("world", False),
    ("python", False),
    ("12345", False),
    
    # Числа-палиндромы
    (121, True),
    (1221, True),
    (12321, True),
    (1, True),
    (0, True),
    (111, True),
    
    # Числа не палиндромы
    (123, False),
    (1234, False),
    (10, False),
    (12345, False),
    
    # Граничные случаи
    (" ", True),
    ("  ", True),
    ("\t", True),
])
def test_is_palindrome_parametrized(input_value, expected):
    assert is_palindrome(input_value) == expected

def test_long_palindrome():
    long_palindrome = "a" * 1000 + "b" + "a" * 1000
    assert is_palindrome(long_palindrome) == True

def test_case_insensitive():
    assert is_palindrome("Racecar", case_sensitive=False) == True
    assert is_palindrome("Aba", case_sensitive=False) == True
    assert is_palindrome("mADam", case_sensitive=True) == False
    assert is_palindrome("Level", case_sensitive=False) == True