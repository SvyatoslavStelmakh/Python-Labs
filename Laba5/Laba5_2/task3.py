def is_palindrome(value, case_sensitive=True):

    str_value = str(value)
    if not case_sensitive:
        str_value = str_value.lower()
    
    # Сравниваем строку с её обратной версией
    return str_value == str_value[::-1]