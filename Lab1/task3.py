password = input('Введите пароль: \n')
if len(password)<16:
    print('Пароль слишком короткий')
elif password.isalpha() or password.isdigit():
    print('Слабый пароль')
else:
    print('Надежный пароль')