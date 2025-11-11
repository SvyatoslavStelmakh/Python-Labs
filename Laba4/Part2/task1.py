import numpy as np

def expenses_comparison(expenses):

    expenses = np.array(expenses)
    
    winter_months = {"december": 11, "january": 0, "febraury": 1}
    summer_months = {"june": 5, "july": 6, "august": 7}
    
    winter_expenses = np.sum(expenses[winter_months.values()])
    summer_expenses = np.sum(expenses[summer_months.values()])
    
    print(f"Зимние месяцы:")
    print(f"декабрь: {expenses[winter_months["december"]]}")
    print(f"январь: {expenses[winter_months["january"]]}")
    print(f"февраль: {expenses[winter_months["febraury"]]}")
    print(f"Общие расходы зимой: {winter_expenses:.2f}")
    
    print(f"Летние месяцы: ")
    print(f"июнь: {expenses[summer_months["june"]]}")
    print(f"июль: {expenses[summer_months["july"]]}")
    print(f"август: {expenses[summer_months["august"]]}")
    print(f"Общие расходы летом: {summer_expenses:.2f}")
    
    if winter_expenses > summer_expenses:
        print("Больше тратится в зимний период")
    elif summer_expenses > winter_expenses:
        print("Больше тратится в летний период")
    else:
        print("Расходы равны в оба периода")

random_expenses = np.random.normal(5000, 1000, 12)
print(random_expenses)