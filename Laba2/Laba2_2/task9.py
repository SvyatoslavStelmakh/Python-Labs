import functools

def type_check(*expected_types):
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            # Проверяем позиционные аргументы
            for i in range(min(len(args), len(expected_types))):
                arg = args[i]
                expected_type = expected_types[i]
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Аргумент {i + 1} ({arg}) имеет тип {type(arg).__name__}, "
                        f"но ожидается {expected_type.__name__}"
                    )
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def sum(*args):
    return sum(args)

print("Проверка декоратора @type_check")

print(f"sum(3, 2) = {sum(3, 2)}")
print(f"sum(3, [1, 2, 3]) = {sum(3, [1, 2, 3])}")

