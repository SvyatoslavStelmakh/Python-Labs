import pytest

from task1 import count_words

@pytest.mark.parametrize("sentence, result",
    [("Простое предложение", 2),
    ("Это тестовое предложение из нескольких слов", 6),
    
    # Крайние случаи
    ("", 0),
    ("   ", 0),
    ("\t\n", 0),
    
    # Одно слово
    ("1", 1),
    ("  Слово  ", 1),
    
    # Множественные пробелы
    ("Много   пробелов   здесь", 3),
    ("  Начало  и  конец  ", 3),
    
    # Специальные символы и числа
    ("123 456 789", 3),
    ("a b c d e f", 6),
    ("test@example.com", 1),  # email считается одним словом
    
    # Пунктуация
    ("Привет, мир!", 2),
    ("Что? Где? Когда?", 3),]
)
def test_count_words(sentence, result):
    assert count_words(sentence) == result