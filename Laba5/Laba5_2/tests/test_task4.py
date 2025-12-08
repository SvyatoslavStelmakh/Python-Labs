import pytest

from task4 import are_anagrams

@pytest.mark.parametrize("word1, word2, expected", [
    ("listen", "silent", True),
    ("triangle", "integral", True),
    ("debit card", "bad credit", True),
    ("dormitory", "dirty room", True),
    ("the eyes", "they see", True),
    
    ("hello", "world", False),
    ("python", "java", False),
    ("test", "best", False),
    ("apple", "pale", False),
    
    ("Listen", "Silent", True),
    ("ABC", "cba", True),
    ("Hello", "Olleh", True),
    
    ("799", "997", True),
    ("12345", "54321", True),
    ("979", "9976", False),

    ("", "", True),
    ("a", "a", True),
    ("a", "b", False),
    ("ab", "ba", True),
    ("abc", "abcd", False),
])
def test_are_anagrams_parametrized(word1, word2, expected):
    assert are_anagrams(word1, word2) == expected