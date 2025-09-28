import datetime
import functools

def log_calls(filename):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
           
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     # получаем текущее время
            
            # формируем строку с аргументами
            args_str = ", ".join([repr(arg) for arg in args])
            kwargs_str = ", ".join([f"{key}={repr(value)}" for key, value in kwargs.items()])
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))
            
            # записываем в файл
            with open(filename, 'a', encoding='utf-8') as f:
                log_line = f"[{current_time}] {func.__name__}({all_args})\n"
                f.write(log_line)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("function_calls.log")
def sum(a, b):
    return a + b

@log_calls("function_calls.log")
def composition(a, b):
    return a * b

# тестируем
if __name__ == "__main__":
    sum(5, 3)
    composition(5, 3)
    sum(10, 20)
    composition(10, 20)
    sum(1, 2)