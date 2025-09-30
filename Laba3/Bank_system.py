class bank():
    def __init__(self):
        last_name = input("Введите вашу фамалию: ")
        first_name = input("Введите ваше имя: ")
        first_name = input("Введите ваше отчество: ")
    

class bank_account():
    def __init__(self, client_ID, currency = "BYN"):
        self.currency = currency
        
class client():
    def __init__(self, client_ID):
        self.client_ID = client_ID