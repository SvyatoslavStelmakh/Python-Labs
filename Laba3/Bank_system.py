import random

class InsufficientFundsError(Exception):
    pass

class bank():
    def __init__(self):
        last_name = input("Введите вашу фамалию: ")
        first_name = input("Введите ваше имя: ")
        first_name = input("Введите ваше отчество: ")
    

class bank_account():
    def __init__(self, currency, client_id):
        self.account_id = str(randint())  # создаём уникальный ID для счета
        self.client_id = client_id
        self.currency = currency
        self.__balance = 0.0  # Баланс, скрытый для прямого изменения

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        """Пополняет счет."""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.__balance += amount
        print(f"Счет {self.account_id} ({self.currency.name}): Пополнение на {amount:.2f}. Новый баланс: {self.__balance:.2f}")

    def withdraw(self, amount: float):
        """Снимает сумму со счета."""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.__balance:
            raise InsufficientFundsError(
                f"Недостаточно средств на счете {self.account_id} ({self.currency.name}). "
                f"Баланс: {self.__balance:.2f}, Запрошено: {amount:.2f}"
            )
        self.__balance -= amount
        print(f"Счет {self.account_id} ({self.currency.name}): Снятие на {amount:.2f}. Новый баланс: {self.__balance:.2f}")
    

        
class client():
    pass
