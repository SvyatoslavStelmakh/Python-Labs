# Склад техники. Каждый вид техники класс наследник от класса орг-техника. Атрибуты: производитель, год, идентификационный номер. Метод str перегружен только в классе Printer. Метод action перегружен для всех производных.

class YearError(Exception):
    pass

class Gadget:
    def __init__(self, producer, id):
        self.producer = producer
        self.year = None
        self.id = id

    def action(self):
        print("Не определено")
    
    def print_info(self):
        print(f"\nПроизводитель: {self.producer}\n"
              f"Год выпуска: {self.year}\n"
              f"ID устройства: {self.id}")
        
    def set_year(self, year):
        if year < 0 or year > 2025:
            raise YearError("\nНедопустимое значение для года производства")
        else:
            self.year = year

class PC(Gadget):
     
    def __init__(self, producer, id):
        super().__init__(producer, id)
        self.type_of_gadget = "PC"
    
    def action(self):
        print("Компьютер работает")

    def print_info(self):
        super().print_info()
        print(f"Тип устройства: {self.type_of_gadget}")

class Printer(Gadget):
    def __init__(self, producer, id):
        super().__init__(producer, id)
        self.type_of_gadget = "принтер"

    def action(self):
        print("Принтер печатает")

    def print_info(self):
        super().print_info()
        print(f"Тип устройства: {self.type_of_gadget}")

    def __str__(self):
        return (f"\nПроизводитель: {self.producer}\nГод выпуска: {self.year}\nID устройства: {self.id}\nТип устройства: {self.type_of_gadget}")
        

class Scaner(Gadget):
    def __init__(self, producer, id):
        super().__init__(producer, id)
        self.type_of_gadget = "сканер"

    def action(self):
        print("Сканер сканирует")

    def print_info(self):
        super().print_info()
        print(f"Тип устройства: {self.type_of_gadget}")

class Headphones(Gadget):
    def __init__(self, producer, id):
        super().__init__(producer, id)
        self.type_of_gadget = "наушники"

    def action(self):
        print("Наушниики воспроизводят музыку")

    def print_info(self):
        super().print_info()
        print(f"Тип устройства: {self.type_of_gadget}")

pc1 = PC("Asus", 1200)
printer1 = Printer("Samsung", 3422)
scaner1 = Scaner("Dell", 2344)
headphones1 = Headphones("Sony", 3453)

def main():
    pc1.action()
    printer1.action()
    scaner1.action()
    headphones1.action()
    try:
        pc1.set_year(2026)
    except YearError as e:
        print(f"Ошибка: {e}")
    printer1.set_year(2020)
    scaner1.set_year(2010)
    headphones1.set_year(2009)
   
        

    pc1.print_info()
    print(printer1)
    scaner1.print_info()
    headphones1.print_info()

if __name__ == "__main__":
    main()