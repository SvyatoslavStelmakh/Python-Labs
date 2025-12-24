import random

def cache(func):
    cache = {}
    def wrapper():
        code = func()
        print(f"Сгенерированный номер: {code}")

        if cache.get(code, 0):
            TypeError(f"Данный код уже существует: {code}")
        else:
            cache[code] = 1
        return code

    return wrapper


@cache
def generate_code():
    numbers = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    letters = "ABCDEHKMNP"
    two_letters = letters[random.randint(0,9)] + letters[random.randint(0,9)]
    last_number = str(random.randint(1,8))

    code = numbers + " " + two_letters + " " + last_number
    return code

generate_code()
generate_code()
generate_code()
generate_code()
generate_code()
generate_code()
generate_code()
generate_code()
generate_code()
generate_code()
        

        