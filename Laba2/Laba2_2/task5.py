import functools

def cache(func):
    
    cache_dict = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
       
        key = (args, tuple(sorted(kwargs.items())))
        
        if key in cache_dict:
            print(f"Возвращаем результат из кэша для аргументов: {args}, {kwargs}")
            return cache_dict[key]
        
        
        print(f"Вычисляем результат для аргументов: {args}, {kwargs}")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        
        return result
    
    return wrapper

@cache
def multiply(a, b):
    return a * b

@cache
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("Тест функции multiply")
print(f"3 * 4 = {multiply(3, 4)}")
print(f"3 * 4 = {multiply(3, 4)}")
print(f"5 * 6 = {multiply(5, 6)}")

print("\nТест функции greet")
print(greet('Svyatoslav'))
print(greet('Svyatoslav'))
print(greet('Bob', greeting='Hi'))
print(greet('Bob', greeting='Hi')) 