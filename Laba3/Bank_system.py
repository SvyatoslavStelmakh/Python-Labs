from datetime import datetime

class AccountNotFoundError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class AccountExistsError(Exception):
    pass

class ClientNotFoundError(Exception):
    pass

class PermissionError(Exception):
    pass

class TransferError(Exception):
    pass

class Bank_account():
    
    def __init__(self, account_id, client_id, currency, balance = 0.0):
        self.account_id = account_id
        self.client_id = client_id
        self.balance = balance
        self.currency = currency
        self.transactions = []
    
    
    # Метод для пополнения баланса
    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        
        self.balance += amount
        
        self.transactions.append({
            'тип': 'депозит',
            'время': datetime.now().strftime("%d.%m.%Y %H:%M"),
            'сумма': amount})
        
    # Метод для снятия средств со счёта
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        elif amount > self.balance:
            raise InsufficientFundsError(
                f"Недостаточно средств на счете ({self.currency}). "
                f"Баланс: {self.balance:.2f}, Запрошено: {amount:.2f}"
            )
        
        self.transactions.append({
            'тип': 'снятие средств',
            'время': datetime.now().strftime("%d.%m.%Y %H:%M"),
            'сумма': amount})

        self.balance -= amount
    
    # Метод для перевода на другой счет
    def transfer(self, target_account, amount):
        
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")
        
        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств для перевода")
        
        # Снимаем с текущего счета
        self.balance -= amount
        self.transactions.append({
            'тип': 'перевод',
            'время': datetime.now().strftime("%d.%m.%Y %H:%M"),
            'сумма перевода': amount,
            'счет получателя': target_account.account_id
        })
        
        # Зачисляем на целевой счет
        target_account.balance += amount
        target_account.transactions.append({
            'тип': 'поступление',
            'время': datetime.now().strftime("%d.%m.%Y %H:%M"),
            'сумма': amount,
            'счет оправителя': self.account_id
        })

class Client():
    
      def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.accounts = []      # список который хранит ID счетов клиента
        
class Bank():
    def __init__(self, name):
        self.name = name
        self.accounts = {}      # словарь, который будет хранить счета всех клиентов
        self.clients = {}       # словарь, который будет хранить всех клиентов банка
        self.next_account_id = 1
        self.next_client_id = 1

    # Метод для регистрации нового клиента
    def registr_client(self, name):

        client_id = self.next_client_id
        self.clients[client_id] = Client(client_id, name)
        self.next_client_id += 1
        return client_id
           
    # Метод для открытия счета для клиента
    def open_account(self, client_id, currency):
        if client_id not in self.clients:
            raise ClientNotFoundError("Клиент не найден")
        
        client = self.clients[client_id]
        
        # Проверяем, нет ли уже счета в этой валюте
        for account_id in client.accounts:
            if self.accounts[account_id].currency == currency:
                raise AccountExistsError(f"У клиента уже есть счет в валюте {currency}")
        
        account_id = self.next_account_id

        account = Bank_account(account_id, client_id, currency)
        
        self.accounts[account_id] = account     # добавляем в словарь ID счета в виде ключа и объект класса Bank_account
        client.accounts.append(account_id)      # добавляем в список который хранит IDшники счетов айди нового счета
        self.next_account_id += 1
        
        return account_id
    
    # Метод для закрытия счета клиента
    def close_account(self, client_id, account_id):
        if client_id not in self.clients:
            raise ClientNotFoundError("Клиент не найден")
        
        if account_id not in self.accounts:
            raise AccountNotFoundError("Счет не найден")
        
        account = self.accounts[account_id]
        
        # Проверяем, что счет принадлежит клиенту
        if account.client_id != client_id:
            raise PermissionError("Счет не принадлежит данному клиенту")
        
        # Проверяем, что баланс не равен 0
        if account.balance > 0:
            raise ValueError("Нельзя закрыть счет с положительным балансом")
        
        # Удаляем счет
        client = self.clients[client_id]
        client.accounts.remove(account_id)
        del self.accounts[account_id]
    
    # Метод для поиска счета клиента по валюте
    def find_account_by_currency(self, client_id, currency):
        
        accounts = self.get_client_accounts(client_id)      #получаем список со счетами клиента
        for account in accounts:
            if account.currency == currency:
                return account
        return None
    
    # Метод для пополнение счета
    def deposit_to_account(self, client_id, account_id, amount):
        
        if account_id not in self.accounts:
            raise AccountNotFoundError("Счет не найден")
        
        account = self.accounts[account_id]
        
        if account.client_id != client_id:
            raise PermissionError("Счет не принадлежит данному клиенту")
        
        account.deposit(amount)


    # Метод для cнятие со счета средств
    def withdraw_from_account(self, client_id, account_id, amount):
        
        if account_id not in self.accounts:
            raise AccountNotFoundError("Счет не найден")
        
        account = self.accounts[account_id]
        
        if account.client_id != client_id:
            raise PermissionError("Счет не принадлежит данному клиенту")
        
        account.withdraw(amount)

    # Метод для перевода между счетами
    def transfer_between_accounts(self, client_id, from_account_id, to_account_id, amount):
        
        if from_account_id not in self.accounts:
            raise AccountNotFoundError("Счет отправителя не найден")
        
        if to_account_id not in self.accounts:
            raise AccountNotFoundError("Счет получателя не найден")
                
        from_account = self.accounts[from_account_id]
        to_account = self.accounts[to_account_id]
        
        if from_account.currency != to_account.currency:
            raise TransferError("Невозможно перевести средства на счет в другой валюте")
        
        if from_account.client_id == to_account.client_id:
            raise TransferError("Невозможно перевести средства на свой же счет")
        
        if from_account.client_id != client_id:
            raise PermissionError("Счет отправителя не принадлежит данному клиенту")
        
        from_account.transfer(to_account, amount)

    # Метод для получение всех счетов клиента
    def get_client_accounts(self, client_id):
        if client_id not in self.clients:
            raise ClientNotFoundError("Клиент не найден")
        
        client_accounts = []        # список для счетов клиента
        for account_id in self.clients[client_id].accounts:
            client_accounts.append(self.accounts[account_id])
        
        return client_accounts

    # Метод для создания выписки по всем счетам пользователя
    def generate_account_statement(self, client_id):
    
        if client_id not in self.clients:
            raise ClientNotFoundError("Клиент не найден")
        
        client_accounts = self.get_client_accounts(client_id)
        client = self.clients[client_id]
        
        print(f"ID клиента: {client.client_id}")
        print(f"Имя клиента: {client.name}")
        print("Счета клиента")
        if len(client.accounts) == 0:
            print("У вас нет открытых счетов")
        else:
            for acc_id in client.accounts:
                print(acc_id, end = ' ')
        
        for account in client_accounts:
            print(f"\nID счета: {account.account_id}")
            print(f"Валюта: {account.currency}")
            print(f"Баланс: {account.balance}")
            print("История транзакций")
            for transaction in account.transactions:
                print(transaction)

           
# Функция для вывода счетов пользователя
def display_accounts(bank, client_id):
    
    accounts = bank.get_client_accounts(client_id)
    
    if not accounts:
        print("У вас нет открытых счетов.")
        return
    
    print("\nВАШИ СЧЕТА")
    for account in accounts:
        print(f"Счет №{account.account_id}: {account.balance:.2f} {account.currency}")

def main():
    bank = Bank("MMM")
    current_client_id = None
    current_client_name = None
    
    print("Добро пожаловать в банковскую систему!")
    
    while True:
        if current_client_id is None:
            # Главное меню для неавторизованного пользователя

            print("=" * 50)
            print("           БАНКОВСКАЯ СИСТЕМА")
            print("=" * 50)
            print("1. Войти в систему")
            print("2. Зарегистрироваться")
            print("3. Выйти из программы")
            print("=" * 50)
             
            choice = input("Выберите действие: ")
               
            if choice == "1":
                # Вход в систему
                print("ВХОД В СИСТЕМУ")
                try:
                    client_id = int(input("Введите ваш ID клиента: ").strip())
                    if client_id in bank.clients:
                        current_client_id = client_id
                        current_client_name = bank.clients[client_id].name
                        print(f"\nВход выполнен успешно! Добро пожаловать, {current_client_name}!")
                        input("Нажмите Enter для продолжения...")
                    else:
                        print("Ошибка: клиент с таким ID не найден.")
                        input("Нажмите Enter для продолжения...")
                except ValueError:
                    print("Ошибка: ID должен быть числом.")
                    input("Нажмите Enter для продолжения...")
                
            elif choice == "2":
                # Регистрация
                print("РЕГИСТРАЦИЯ")
                name = input("Введите ваше полное имя: ")
                    
                if not name:
                    print("Ошибка: имя не может быть пустым.")
                    input("Нажмите Enter для продолжения...")
                else:
                    client_id = bank.registr_client(name)
                    print(f"\nРегистрация успешна!")
                    print(f"Ваш ID клиента: {client_id}")
                    print("Запомните этот ID для входа в систему!")
                    input("Нажмите Enter для продолжения...")
                
            elif choice == "3":
                print("\nДо свидания!")
                break
                
            else:
                print("Неверный выбор. Попробуйте снова.")
                input("Нажмите Enter для продолжения...")               
            
        else:
            # Меню клиента (авторизованный пользователь)
            print("=" * 50)
            print(f"Добро пожаловать, {current_client_name}!")
            print("=" * 50)
            print("1. Открыть новый счет")
            print("2. Закрыть счет")
            print("3. Пополнить счет")
            print("4. Снять со счета")
            print("5. Перевести деньги между счетами")
            print("6. Показать мои счета")
            print("7. Показать выписку по счетам")
            print("8. Выйти из системы")
            print("=" * 50)
                
            choice = input("Выберите действие (1-8): ")
                
            if choice == "1":
                # Открытие счета
                print("ОТКРЫТИЕ НОВОГО СЧЕТА")
                print("Доступные валюты: BYN, RUB, USD, EUR")
                currency = input("Введите валюту счета: ").strip().upper()
                    
                if currency not in ["BYN", "RUB", "USD", "EUR"]:
                    print("Ошибка: счет можно открыть только в BYN, RUB, USD, EUR.")
                    input("Нажмите Enter для продолжения...")
                else:
                    try:
                        account_id = bank.open_account(current_client_id, currency)
                        print(f"\nСчет успешно открыт!")
                        print(f"Номер счета: {account_id}")
                        print(f"Валюта: {currency}")
                        input("\nНажмите Enter для продолжения...")
                    except (ValueError, AccountExistsError) as e:
                        print(f"Ошибка: {e}")
                        input("Нажмите Enter для продолжения...")
                
            elif choice == "2":
                # Закрытие счета
                print("ЗАКРЫТИЕ СЧЕТА")
                display_accounts(bank, current_client_id)
                    
                try:
                    account_id = int(input("\nВведите номер счета для закрытия: "))
                    bank.close_account(current_client_id, account_id)
                    print(f"\nСчет №{account_id} успешно закрыт!")
                    input("Нажмите Enter для продолжения...")
                except (PermissionError, AccountNotFoundError) as e:
                    print(f"Ошибка: {e}")
                    input("Нажмите Enter для продолжения...")
                except ValueError:
                    print("Ошибка: Номер счета должен быть числом.")
                    input("Нажмите Enter для продолжения...")
                
            elif choice == "3":
                # Пополнение счета
                print("ПОПОЛНЕНИЕ СЧЕТА")
                display_accounts(bank, current_client_id)
                    
                try:
                    account_id = int(input("\nВведите номер счета: "))
                    amount = float(input("Введите сумму для пополнения: "))
                    bank.deposit_to_account(current_client_id, account_id, amount)
                    account = bank.accounts[account_id]
                    print(f"\nОперация успешна!")
                    print(f"Счет пополнен на {amount:.2f} {account.currency}")
                    print(f"Текущий баланс: {account.balance:.2f} {account.currency}")
                    input("\nНажмите Enter для продолжения...")
                except PermissionError as e:
                    print(f"Ошибка: {e}")
                    input("Нажмите Enter для продолжения...")
                except ValueError:
                    print("Ошибка: Номер счета и сумма должны быть числами.")
                    input("Нажмите Enter для продолжения...")
                
            elif choice == "4":
                # Снятие со счета
                print("СНЯТИЕ СО СЧЕТА")
                display_accounts(bank, current_client_id)
                
                try:
                    account_id = int(input("\nВведите номер счета: "))
                    amount = float(input("Введите сумму для снятия: "))
                    bank.withdraw_from_account(current_client_id, account_id, amount)
                    account = bank.accounts[account_id]
                    print(f"\nОперация успешна!")
                    print(f"Со счета снято {amount:.2f} {account.currency}")
                    print(f"Текущий баланс: {account.balance:.2f} {account.currency}")
                    input("\nНажмите Enter для продолжения...")
                except (PermissionError, InsufficientFundsError) as e:
                    print(f"Ошибка: {e}")
                    input("Нажмите Enter для продолжения...")
                except ValueError:
                    print("Ошибка: Номер счета и сумма должны быть числами.")
                    input("Нажмите Enter для продолжения...")
                
            elif choice == "5":
                # Перевод между счетами
                print("ПЕРЕВОД ДЕНЕГ")
                display_accounts(bank, current_client_id)
                    
                try:
                    from_account_id = int(input("\nВведите номер счета отправителя: "))
                    to_account_id = int(input("Введите номер счета получателя: "))
                    amount = float(input("Введите сумму перевода: "))
                    bank.transfer_between_accounts(current_client_id, from_account_id, to_account_id, amount)
                    from_account = bank.accounts[from_account_id]
                        
                    print(f"\nПеревод успешно выполнен!")
                    print(f"Переведено: {amount:.2f} {from_account.currency}")
                    input("\nНажмите Enter для продолжения...")
                except (PermissionError, InsufficientFundsError, TransferError) as e:
                    print(f"Ошибка: {e}")
                    input("Нажмите Enter для продолжения...")
                except ValueError:
                    print("Ошибка: Номера счетов и сумма должны быть числами.")
                    input("Нажмите Enter для продолжения...")
                
            elif choice == "6":
                # Показать счета
                print("ВАШИ СЧЕТА")
                display_accounts(bank, current_client_id)
                input("\nНажмите Enter для продолжения...")
                
            elif choice == "7":
                # Вывод выписки в консоль
                print("ВЫПИСКИ ПО СЧЕТАМ")
                try:
                    print(bank.generate_account_statement(current_client_id))
                    input("\nНажмите Enter для продолжения...")
                except (Exception, ClientNotFoundError) as e:
                    print(f"Ошибка: {e}")
                    input("Нажмите Enter для продолжения...")
                
            elif choice == "8":
                # Выход из системы
                print(f"\nДо свидания, {current_client_name}!")
                current_client_id = None
                current_client_name = None
                input("Нажмите Enter для продолжения...")
                
            else:
                print("Неверный выбор. Попробуйте снова.")
                input("Нажмите Enter для продолжения...")
            

if __name__ == "__main__":
    main()