from datetime import datetime
import functools

def log_calls(filename):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
           
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")     # получаем текущее время
            
            # формируем строку с аргументами
            args_str = ", ".join([str(arg) for arg in args])
            kwargs_str = ", ".join([f"{key}={str(value)}" for key, value in kwargs.items()])
            all_args = ", ".join([args_str, kwargs_str])
            
            # записываем в файл
            with open(filename, 'a', encoding='utf-8') as file:
                log_line = f"[{current_time}] {func.__name__}({all_args})\n"
                file.write(log_line)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("function_calls.log")
def sum(*args):
    return sum(args)

@log_calls("function_calls.log")
def composition(a, b):
    return a * b

sum(5, 3)
composition(5, 3)
sum(10, 20)
composition(10, 20)
sum(1, 2)