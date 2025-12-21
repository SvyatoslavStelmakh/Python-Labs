import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import sys
from openpyxl import load_workbook

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

# Информация об объемах продажах по точкам
point_analysis_sales = df.groupby('точка').agg({'Продажи': ['sum', 'mean', 'std']}).round(2)
point_analysis_sales.columns = ['Общие продажи', 'Средние продажи', 'Стандартное отклонение продаж']
print(point_analysis_sales)

# Информация о количестве проданных товаров по точкам
point_analysis_amount = df.groupby('точка').agg({'Количество': ['sum', 'mean', 'std']}).round(0)
point_analysis_amount.columns = ['Общее количество проданных товаров', 'Средние количество проданных товаров', 'Стандартное отклонение количества проданных товаров']
print(point_analysis_amount)

# Информация о прибыли по точкам
point_analysis_profit = df.groupby('точка').agg({'Прибыль': ['sum', 'mean']}).round(2)
point_analysis_profit.columns = ['Общая прибыль', 'Средняя прибыль']
print(point_analysis_profit)

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

product_analysis.columns = ['Общие продажи', 'Средние продажи', 'Общее количество', 'Среднее количество', 'Общая прибыль', 'Средняя прибыль', 'Средняя цена']
print(product_analysis.sort_values('Общие продажи', ascending=False))

# ОБЩАЯ ДИНАМИКА ПРОДАЖ

monthly_sales = df.groupby(df['Дата'].dt.to_period('M'))['Продажи'].sum()
monthly_profit = df.groupby(df['Дата'].dt.to_period('M'))['Прибыль'].sum()
monthly_cost = df.groupby(df['Дата'].dt.to_period('M'))['Себестоимость'].sum()
monthly_qty = df.groupby(df['Дата'].dt.to_period('M'))['Количество'].sum()

print(monthly_sales)

plt.figure(figsize=(14, 6))
monthly_sales.plot(kind='line')
plt.title('Динамика продаж по месяцам')
plt.ylabel('Рублей')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(monthly_cost.index, monthly_cost.values, label='Себестоимость')
plt.title('Динамика себестоимости по месяцам')
plt.ylabel('Рублей')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(monthly_profit.index, monthly_profit.values, label='Прибыль')
plt.title('Динамика прибыли по месяцам')
plt.ylabel('Рублей')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(monthly_qty.index, monthly_qty.values, color='green', label='Количество')
plt.title('Динамика объемов продаж')
plt.ylabel('Количество')
plt.tick_params(axis='x', rotation=45)
plt.show()

# АНАЛИЗ ПО БРЕНДАМ
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Продажи по брендам
brand_sales = df.groupby('бренд')['Продажи'].sum().sort_values(ascending=False)
brand_sales.plot(kind='bar', ax=axes[0], title='Объем продаж по брендам')
axes[0,0].tick_params(axis='x', rotation=45)

# Прибыль по брендам
brand_profit = df.groupby('бренд')['Прибыль'].sum().sort_values(ascending=False)
brand_profit.plot(kind='bar', ax=axes[1], title='Прибыль по брендам', color='orange')
axes[0,1].tick_params(axis='x', rotation=45)

# Количество продаж по брендам
brand_qty = df.groupby('бренд')['Количество'].sum().sort_values(ascending=False)
brand_qty.plot(kind='bar', ax=axes[2], title='Количество продаж по брендам', color='red')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# 3. АНАЛИЗ ПО ТОВАРАМ (ТОП-10)
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Топ-10 товаров по продажам
top_products_sales = df.groupby('товар')['Продажи'].sum().nlargest(10)
top_products_sales.plot(kind='bar', ax=axes[0,0], title='Топ-10 товаров по объему продаж')
axes[0,0].tick_params(axis='x', rotation=45)

# Топ-10 товаров по прибыли
top_products_profit = df.groupby('товар')['Прибыль'].sum().nlargest(10)
top_products_profit.plot(kind='bar', ax=axes[0,1], title='Топ-10 товаров по прибыли', color='orange')
axes[0,1].tick_params(axis='x', rotation=45)

# Топ-10 товаров по количеству продаж
top_products_qty = df.groupby('товар')['Количество'].sum().nlargest(10)
top_products_qty.plot(kind='bar', ax=axes[1,1], title='Топ-10 товаров по количеству продаж', color='red')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# Сезонность по месяцам
plt.figure(figsize=(10, 6))
monthly_pattern = df.groupby('Месяц')[['Продажи', 'Количество']].mean()
monthly_pattern['Продажи'].plot(marker='o')
plt.title('Средние продажи по месяцам')
plt.ylabel('Средние продажи, руб')
plt.show()

# ПРОГНОЗИРОВАНИЕ ДЛЯ КАЖДОГО ТОВАРА
def forecast_product_sales(product_data, product_name, periods=6):
    if len(product_data) < 6:
        return None, None, None
    
    # Подготовка данных для модели
    X = np.array(range(len(product_data))).reshape(-1, 1)
    y = product_data['Продажи'].values
    
    # Обучение линейной регрессии
    model = LinearRegression()
    model.fit(X, y)
    
    # Прогноз на future_periods месяцев
    future_X = np.array(range(len(product_data), len(product_data) + periods)).reshape(-1, 1)
    forecast = model.predict(future_X)
    
    # Расчет метрик качества
    y_pred = model.predict(X)
    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    
    return forecast, mae, rmse

# Прогноз для топ-5 товаров
top_products = df.groupby('товар')['Продажи'].sum().nlargest(5).index

fig, axes = plt.subplots(3, 2, figsize=(15, 12))
axes = axes.flatten()

for i, product in enumerate(top_products[:6]):
    product_data = df[df['товар'] == product].sort_values('Дата')
    
    # Прогноз
    forecast, mae, rmse = forecast_product_sales(product_data, product)
    
    if forecast is not None:
        # Визуализация исторических данных и прогноза
        dates = product_data['Дата'].dt.strftime('%Y-%m')
        future_dates = pd.date_range(start=product_data['Дата'].iloc[-1] + pd.DateOffset(months=1), 
                                   periods=6, freq='M').strftime('%Y-%m')
        
        axes[i].plot(dates, product_data['Продажи'].values, marker='o', label='Исторические данные')
        axes[i].plot(future_dates, forecast, marker='s', linestyle='--', label='Прогноз', color='red')
        axes[i].set_title(f'{product}\nMAE: {mae:.0f}, RMSE: {rmse:.0f}')
        axes[i].tick_params(axis='x', rotation=45)
        axes[i].legend()
        axes[i].grid(True, alpha=0.3)

# Удаляем лишние subplots
for i in range(len(top_products[:6]), 6):
    fig.delaxes(axes[i])

plt.tight_layout()
plt.show()

