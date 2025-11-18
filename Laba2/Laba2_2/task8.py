import time
import functools

def timing(func):
   
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        
        # вычисляем время выполнения в миллисекундах
        execution_time = (end_time - start_time) * 1000  # преобразуем в миллисекунды
        
        print(f"Функция '{func.__name__}' выполнилась за {execution_time:.2f} мс")
        
        return result
    
    return wrapper

@timing
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Тестирование декоратора @timing")
print("\n Тест Fibonacci:")
result1 = fibonacci(10)
print(f"Результат: {result1}")