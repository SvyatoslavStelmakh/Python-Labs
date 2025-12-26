import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sys

sys.setrecursionlimit(10000)

# Читаем данные, начиная со строки 3 (skiprows=2 пропускает первые 2 строки)
df = pd.read_excel('lab_4_part_5.xlsx', 
                   sheet_name='Данные',
                   usecols='B:J',  # колонки B-J
                   skiprows=1,     # пропускаем 2 строки (строки 1 и 2)
                   engine='openpyxl')

# Назначаем имена колонкам (так как пропустили заголовки)
df.columns = ['Дата', 'Год', 'Год-мес', 'точка', 'бренд', 'товар', 
              'Количество', 'Продажи', 'Себестоимость']

# Удаляем полностью пустые строки
df = df.dropna(how='all')

# Преобразование даты
df['Дата'] = pd.to_datetime(df['Дата'])
df['Месяц'] = df['Дата'].dt.month
df['Квартал'] = df['Дата'].dt.quarter

df['Продажи'] = df['Продажи']*0.036
df['Себестоимость'] = df['Себестоимость']*0.036
print("\nПервые 5 строк:")
print(df.head(5))

# Расчет дополнительных показателей
df['Прибыль'] = df['Продажи'] - df['Себестоимость']
df['Средняя цена'] = (df['Продажи'] / df['Количество']).round(2)

print("\nПервые 5 строк:")
print(df.head(5))

print("=== ОБЩАЯ ДИНАМИКА ТОВАРООБОРОТА ===")

# Месячная динамика
print("Месячная динамика:")
monthly_sales = df.groupby(df['Дата'].dt.to_period('M')).agg({
    'Продажи': 'sum',
    'Количество': 'sum',
    'Себестоимость': 'sum',
    'Прибыль': 'sum'
}).reset_index()

print(monthly_sales)

# Анализ по точкам реализации
print("\n=== АНАЛИЗ ПО ТОЧКАМ РЕАЛИЗАЦИИ ===")

# Получаем список всех уникальных точек
all_points = df['точка'].unique()
print(f"Всего точек реализации: {len(all_points)}")
print(f"Список точек: {all_points}")

# Информация об объемах продажах по точкам
point_analysis_sales = df.groupby('точка').agg({'Продажи': ['sum', 'mean', 'std']}).round(2).reset_index()
point_analysis_sales.columns = ['Точка', 'Общие продажи(млн)', 'Средние продажи', 'Стандартное отклонение продаж']
point_analysis_sales['Общие продажи(млн)'] = (point_analysis_sales['Общие продажи(млн)']/1e6).round(3)
print(point_analysis_sales)

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=point_analysis_sales.values,
                 colLabels=point_analysis_sales.columns,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)  # Масштабирование таблицы
plt.title('Статистика продаж по точкам', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

# Информация о количестве проданных товаров по точкам
point_analysis_amount = df.groupby('точка').agg({'Количество': ['sum', 'mean', 'std']}).round(0).reset_index()
point_analysis_amount.columns = ['Точка', 'Общее количество', 'Средние количество', 'Стандартное отклонение\nколичества проданных товаров']
print(point_analysis_amount)

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=point_analysis_amount.values,
                 colLabels=point_analysis_amount.columns,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)  # Масштабирование таблицы
plt.title('Статистика по количеству продаж по точкам', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

# Информация о прибыли по точкам
point_analysis_profit = df.groupby('точка').agg({'Прибыль': ['sum', 'mean']}).round(2).reset_index()
point_analysis_profit.columns = ['Точка', 'Общая прибыль(млн)', 'Средняя прибыль']
point_analysis_profit['Общая прибыль(млн)'] = (point_analysis_profit['Общая прибыль(млн)']/1e6).round(3)
print(point_analysis_profit)

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=point_analysis_profit.values,
                 colLabels=point_analysis_profit.columns,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)  # Масштабирование таблицы
plt.title('Статистика прибыли по точкам', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

# Создаем пустые словари данных для хранения результатов
point_sales_dynamic = {}
point_qnt_dynamic = {}
pont_profit_dynamic = {}

# Собираем данные по каждой точке
for point in all_points:
    # Фильтруем данные для текущей точки
    point_data = df[df['точка'] == point]
    
    # Группируем по месяцам и считаем сумму для каждой точки
    point_sales_dynamic[point] = point_data.groupby(df['Дата'].dt.to_period('M'))['Продажи'].sum()
    point_qnt_dynamic[point] = point_data.groupby(df['Дата'].dt.to_period('M'))['Количество'].sum()
    pont_profit_dynamic[point] = point_data.groupby(df['Дата'].dt.to_period('M'))['Прибыль'].sum()

# Динамика продаж по месяцам
plt.figure(figsize=(14, 7))

for point in all_points:
    if point in point_sales_dynamic:
        plt.plot(point_sales_dynamic[point].index.astype(str), point_sales_dynamic[point]/1e6, label=point, marker='o', alpha=0.9)

plt.title('Динамика продаж по месяцам для точек реализации', fontsize=16, fontweight='bold', pad=25)
plt.xlabel('Месяц', fontsize=14)
plt.ylabel('Продажи (млн)', fontsize=14)
plt.xticks(rotation=30)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Динамика количества продаж по месяцам
plt.figure(figsize=(14, 7))

for point in all_points:
    if point in point_qnt_dynamic:
        plt.plot(point_qnt_dynamic[point].index.astype(str), point_qnt_dynamic[point], label=point, linewidth=2, marker='o', alpha=0.9)

plt.title('Динамика количества продаж по месяцам для точек реализации', fontsize=16, fontweight='bold', pad=25)
plt.xlabel('Месяц', fontsize=14)
plt.ylabel('Количество продаж', fontsize=14)
plt.xticks(rotation=30)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Динамика прибыли по месяцам
plt.figure(figsize=(14, 7))

for point in all_points:
    if point in pont_profit_dynamic:
        plt.plot(pont_profit_dynamic[point].index.astype(str), pont_profit_dynamic[point], label=point, linewidth=2, marker='o', alpha=0.9)

plt.title('Динамика прибыли по месяцам для точек реализации', fontsize=16, fontweight='bold', pad=25)
plt.xlabel('Месяц', fontsize=14)
plt.ylabel('Прибыль', fontsize=14)
plt.xticks(rotation=30)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Анализ по брендам
print("\n=== АНАЛИЗ ПО БРЕНДАМ ===")

brand_analysis = df.groupby('бренд').agg({
    'Продажи': ['sum', 'mean'],
    'Количество': ['sum', 'mean'],
    'Прибыль': ['sum', 'mean']
}).round(2)

brand_analysis.columns = ['Общие продажи', 'Средние продажи', 'Общее количество', 'Среднее количество', 'Общая прибыль', 'Средняя прибыль']
print(brand_analysis)

# Анализ по товарам
print("\n=== АНАЛИЗ ПО ТОВАРАМ ===")

product_analysis = df.groupby('товар').agg({
    'Продажи': ['sum', 'mean'],
    'Количество': ['sum', 'mean'],
    'Прибыль': ['sum', 'mean'],
    'Средняя цена': 'mean'
}).round(2)

product_analysis.columns = ['Общие продажи', 'Средние продажи',
                            'Общее количество', 'Среднее количество',
                            'Общая прибыль', 'Средняя прибыль',
                            'Средняя цена']
print(product_analysis.sort_values('Общие продажи', ascending=False))

# ОБЩАЯ ДИНАМИКА ПРОДАЖ

# Годовая динамика
yearly_sales = df.groupby('Год').agg({
    'Продажи': 'sum',
    'Количество': 'sum',
    'Себестоимость': 'sum',
    'Прибыль': 'sum'
}).reset_index()

# Годовая динамика ключевых показателей
years = yearly_sales['Год']
x = np.arange(len(years))
width = 0.2

plt.figure(figsize=(10, 6))
plt.bar(x - width, yearly_sales['Продажи']/1e6, width, label='Продажи (млн)')
plt.bar(x, yearly_sales['Прибыль']/1e6, width, label='Прибыль (млн)')
plt.bar(x + width, yearly_sales['Количество']/1000, width, label='Количество (тыс)')
plt.title('Годовая динамика ключевых показателей')
plt.xlabel('Год')
plt.xticks(x, years)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

monthly_sales = df.groupby(df['Дата'].dt.to_period('M'))['Продажи'].sum()/1e6
monthly_profit = df.groupby(df['Дата'].dt.to_period('M'))['Прибыль'].sum()/1e6
monthly_cost = df.groupby(df['Дата'].dt.to_period('M'))['Себестоимость'].sum()/1e6
monthly_qty = df.groupby(df['Дата'].dt.to_period('M'))['Количество'].sum()
monthly_price = df.groupby(df['Дата'].dt.to_period('M'))['Средняя цена'].mean()

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', label='Продажи')
plt.title('Динамика продаж по месяцам')
plt.ylabel('Рублей (млн)')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
monthly_profit.plot(kind='line',  color='green', label='Прибыль')
plt.title('Динамика прибыли по месяцам')
plt.legend()
plt.ylabel('Рублей (млн)')
plt.show()

plt.figure(figsize=(10, 6))
monthly_cost.plot(kind='line', color='orange', label='Себестоимость')
plt.title('Динамика себестоимости по месяцам')
plt.legend()
plt.ylabel('Рублей (млн)')
plt.show()

plt.figure(figsize=(10, 6))
monthly_qty.plot(kind='line', color='red', label='Количество')
plt.title('Динамика объемов продаж')
plt.legend()
plt.ylabel('Количество')
plt.show()

plt.figure(figsize=(10, 6))
monthly_qty.plot(kind='line', color='purple', label='Средняя цена')
plt.title('Динамика средней цены')
plt.legend()
plt.ylabel('Рублей')
plt.show()

# АНАЛИЗ ПО БРЕНДАМ

# Распределение продаж по брендам
brand_sales = df.groupby('бренд')['Продажи'].sum().sort_values(ascending=False)/1e6
plt.figure(figsize=(6, 6))
plt.pie(brand_sales.values, labels=brand_sales.index, autopct='%1.1f%%')
plt.title('Распределение продаж по брендам')
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Продажи по брендам
brand_sales.plot(kind='bar', ax=axes[0], title='Объем продаж по брендам')
axes[0].set_ylabel('Рублей (млн)')
axes[0].tick_params(axis='x', rotation=45)

# Прибыль по брендам
brand_profit = df.groupby('бренд')['Прибыль'].sum().sort_values(ascending=True)/1e6
brand_profit.plot(kind='bar', ax=axes[1], title='Прибыль по брендам', color='orange')
axes[1].set_ylabel('Рублей (млн)')
axes[1].tick_params(axis='x', rotation=45)

# Количество продаж по брендам
brand_qty = df.groupby('бренд')['Количество'].sum().sort_values(ascending=True)
brand_qty.plot(kind='bar', ax=axes[2], title='Количество продаж по брендам', color='red')
axes[2].set_ylabel('Штук')
axes[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# 3. АНАЛИЗ ПО ТОВАРАМ (ТОП-10)
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
indexes = range(1, 11)

# Топ-10 товаров по продажам
top_products_sales = df.groupby('товар')['Продажи'].sum().nlargest(10)
top_products_sales.plot(kind='bar', ax=axes[0,0], title='Топ-10 товаров по объему продаж')
axes[0,0].tick_params(axis='x', rotation=30)

# Топ-10 товаров по прибыли
top_products_profit = df.groupby('товар')['Прибыль'].sum().nlargest(10)
top_products_profit.plot(kind='bar', ax=axes[0,1], title='Топ-10 товаров по прибыли', color='orange')
axes[0,1].tick_params(axis='x', rotation=30)

# Топ-10 товаров по количеству продаж
top_products_qty = df.groupby('товар')['Количество'].sum().nlargest(10)
top_products_qty.plot(kind='bar', ax=axes[1,0], title='Топ-10 товаров по количеству продаж', color='green')
axes[1,0].tick_params(axis='x', rotation=30)

# Топ-10 товаров по средней цене
top_products_price = df.groupby('товар')['Средняя цена'].mean().nlargest(10)
top_products_price.plot(kind='bar', ax=axes[1,1], title='Топ-10 товаров по средней цене', color='red')
axes[1,1].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.show()

# Создадим временные ряды для прогнозирования
def create_time_series(data, product_name=None):
    if product_name:
        data = data[data['товар'] == product_name]
    
    time_series = data.groupby(['Год', 'Месяц']).agg({'Продажи': 'sum'}).reset_index()
    time_series['period'] = time_series['Год'] * 100 + time_series['Месяц']
    time_series = time_series.sort_values('period')
    time_series['time_index'] = range(len(time_series))
    
    return time_series

# Прогноз для топ-5 товаров
top_5_products = df.groupby('товар')['Продажи'].sum().nlargest(5).index

# Прогноз на будущие периоды
total_sales_ts = create_time_series(df)
future_periods = 12
last_time_index = total_sales_ts['time_index'].max()
future_indices = np.array(range(last_time_index + 1, last_time_index + future_periods + 1)).reshape(-1, 1)

for i, product in enumerate(top_5_products):
    plt.figure(figsize=(8, 4))
    product_ts = create_time_series(df, product)
    
    if len(product_ts) > 4:  # минимальное количество точек для прогноза
        X_product = product_ts[['time_index']]
        y_product = product_ts['Продажи']
        
        # Линейная регрессия для прогноза тренда
        product_model = LinearRegression()
        product_model.fit(X_product, y_product)
        
        # Прогноз
        future_product = product_model.predict(future_indices)
        
        plt.plot(product_ts['time_index'], y_product/1e3, 'b-', marker='o', label='История')
        plt.plot(future_indices, future_product/1e3, 'r--', marker='s', label='Прогноз')
        plt.title(f'Прогноз для: {product}')
        plt.xlabel('Временной индекс')
        plt.ylabel('Продажи (тыс)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
