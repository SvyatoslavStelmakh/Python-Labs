import random

class AccountNotFoundError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class AccountExistsError(Exception):
    pass

class Bank():
    def __init__(self):
        last_name = input("Введите вашу фамалию: ")
        first_name = input("Введите ваше имя: ")
        first_name = input("Введите ваше отчество: ")
    
    clients_ID = {}
    

class Bank_account():
    
    def __init__(self, currency, client_id):
        self.client_id = client_id
        self.client_accounts = {}     # словарь, который представляет собой счета. Ключ-валюта, значение-баланс 
        self.client_accounts[currency] = 0
        # self.__balance = 0.0  # Баланс, скрытый для прямого изменения

    @property
    # Метод для проверки баланса
    def balance(self, currency):
        if currency not in self.client_accounts:
            raise AccountNotFoundError("Счета в данной валюте не существует.")

        return self.client_accounts[currency]

    # Метод для пополнения баланса
    def deposit(self, currency, amount):
        if currency not in self.client_accounts:
            raise AccountNotFoundError("Счета в данной валюте не существует.")
        elif amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.client_accounts[currency] += amount
        print(f"Счет ({currency}): Пополнение на {amount:.2f}. Новый баланс: {self.client_accounts[currency]:.2f}")

    # Метод для снятия средств со счёта
    def withdraw(self, currency, amount):
        if currency not in self.client_accounts:
            raise AccountNotFoundError("Счета в данной валюте не существует.")
        elif amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        elif amount > self.client_accounts[currency]:
            raise InsufficientFundsError(
                f"Недостаточно средств на счете ({currency}). "
                f"Баланс: {self.client_accounts[currency]:.2f}, Запрошено: {amount:.2f}"
            )
        
        self.client_accounts[currency] -= amount
        print(f"Счет ({currency}): Снятие на {amount:.2f}. Новый баланс: {self.client_accounts[currency]:.2f}")
    

class Client():
    
    def __init__(self, name):
        self.name = name

        while True:
            self.client_id = str(random.randint(100, 999))
            if self.client_id in client_ID.values():
                pass
            else:
                client_ID[self.name] = self.client_id
                break

        self.accounts_currency = [] # Список, который хранит валюты уже существующих счетов

    # Метод для создания счета
    def add_account(self, input_currency):
        if input_currency in self.accounts_currency:
            raise AccountExistsError(f"У клиента {self.name} уже есть счет в валюте {input_currency}.")
        
        self.accounts_currency.append(input_currency)


    def get_account(self, currency):
        if currency not in self.accounts_currency:
            raise AccountNotFoundError(f"Счет в валюте {currency.name} не найден для клиента {self.name}.")
        return self.accounts_currency[currency]

    def get_summary_balance(self) -> float:
        # Перебираем словарь, в котором хранятся счета клиента
        for key, value in client_accounts.items():
            if key == "BYN":
                summary_balance += value
            elif key == "RUB":
                summary_balance += value * 0.0368
            elif key == "USD":
                summary_balance += value * 2.987
            elif key == "EUR":
                summary_balance += value * 3.491
        return summary_balance

    def __repr__(self):
        return f"Client(ID={self.client_id}, Name={self.name}, Accounts={len(self.accounts_currency)})"
    pass
