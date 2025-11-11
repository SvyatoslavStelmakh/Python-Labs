import numpy as np

def expenses_comparison(expenses):

    expenses = np.array(expenses)
    
    winter_months = [11, 0, 1]
    summer_months = [5, 6, 7]
    
    winter_expenses = np.sum(expenses[winter_months])
    summer_expenses = np.sum(expenses[summer_months])
    
    print(f"Зимние месяцы:")
    print(f"декабрь: {expenses[11]:.2f}")
    print(f"январь: {expenses[0]:.2f}")
    print(f"февраль: {expenses[1]:.2f}")
    print(f"Общие расходы зимой: {winter_expenses:.2f}")
    
    print(f"Летние месяцы: ")
    print(f"июнь: {expenses[5]:.2f}")
    print(f"июль: {expenses[6]:.2f}")
    print(f"август: {expenses[7]:.2f}")
    print(f"Общие расходы летом: {summer_expenses:.2f}")
    
    if winter_expenses > summer_expenses:
        print("Больше тратится в зимний период")
    elif summer_expenses > winter_expenses:
        print("Больше тратится в летний период")
    else:
        print("Расходы равны в оба периода")

    print(f"Номер месяца с наибольшими тратами: {np.argmax(expenses) + 1}")

random_expenses = np.random.normal(80, 50, 12)
print(random_expenses)

expenses_comparison(random_expenses)