import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA')   # загружаем таблицу из файла
df.columns = ['дата покупки', 'дата совершения перелета', 'тип пассажиров', 'сумма', 'способ оплаты', 'город отправления', 'город назначения', 'тип перелета', 'наличие программы лояльности', 'способ покупки']

print("ПЕРИОД ВРЕМЕНИ ДАТАСЕТА:")

# Преобразование дат в правильный формат
df['дата покупки'] = pd.to_datetime(df['дата покупки'])
df['дата совершения перелета'] = pd.to_datetime(df['дата совершения перелета'])

min_issue_date = df['дата покупки'].min()
max_issue_date = df['дата покупки'].max()
min_flight_date = df['дата совершения перелета'].min()
max_flight_date = df['дата совершения перелета'].max()

print(f"Даты продаж билетов:    {min_issue_date.strftime('%d.%m.%Y')} - {max_issue_date.strftime('%d.%m.%Y')}")
print(f"Даты перелетов:         {min_flight_date.strftime('%d.%m.%Y')} - {max_flight_date.strftime('%d.%m.%Y')}")
print(f"Заблаговременность:     В среднем {(df['дата совершения перелета'] - df['дата покупки']).dt.days.mean():.0f} дней")


print("\nОБЩЕЕ КОЛИЧЕСТВО ПАССАЖИРОВ И ТРАНЗАКЦИЙ:")

total_passengers = len(df)

print(f"Общее количество пассажиров: {total_passengers:,}")

monthly_stats = df.groupby(df['дата покупки'].dt.to_period('M')).agg({
    'тип пассажиров': 'count',
    'сумма': ['sum', 'mean']
}).round(1)

monthly_stats.columns = ['Количество пассажиров', 'Суммарная выручка', 'Средняя выручка']
print(f"Статистика по месяцам\n{monthly_stats}")

# Топ-5 аэропортов отправления
top_orig = df['город отправления'].value_counts().head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_orig.index, y=top_orig.values)
plt.title('Топ-5 аэропортов отправления')
plt.xlabel('Аэропорты')
plt.ylabel('Количество перелетов')
plt.show()

# Топ-5 аэропортов назначения
top_dest = df['город назначения'].value_counts().head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_dest.index, y=top_dest.values)
plt.title('Топ-5 аэропортов назначения')
plt.xlabel('Аэропорты')
plt.ylabel('Количество перелетов')
plt.show()

# Самые популярные маршруты
route_counts = df.groupby(['город отправления', 'город назначения']).size().reset_index(name='counts').sort_values(by='counts', ascending=True).head(5)
print("Топ-5 популярных маршрутов:")
print(route_counts)

monthly_sales = df.groupby(df['дата покупки'].dt.to_period('M')).size()   # количество продаж в месяц 
monthly_revenue = df.groupby(df['дата покупки'].dt.to_period('M'))['сумма'].sum()    # сумма продаж в месяц
monthly_flights = df.groupby(df['дата совершения перелета'].dt.to_period('M')).size()   # количество перелетов в месяц 

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
monthly_sales.plot(kind='line', title='Количество продаж по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество продаж')

plt.subplot(1, 2, 2)
monthly_revenue.plot(kind='line', title='Сумма продаж по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Сумма дохода')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
monthly_flights.plot(kind='line', title='Количество перелетов по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество перелетов')
plt.tight_layout()
plt.show()

print("Наибольшее количество продаж билетов приходится на ИЮЛЬ")
print("Также можно выделить ноябрь")
print("Наибольшая прибыль наблюдается в ИЮЛЕ и АВГУСТЕ")
print("Наибольшее количество перелетов в АВГУСТЕ")

# Распределение по типам пассажиров
pax_type_counts = df['тип пассажиров'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(pax_type_counts.values, labels=pax_type_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Распределение по типам пассажиров')
plt.show()

# Средний доход по типам пассажиров
pax_revenue = df.groupby('тип пассажиров')['сумма'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
sns.barplot(x=pax_revenue.index, y=pax_revenue.values)
plt.title("Средний доход по типам пассажиров")
plt.xlabel('Типы пассажиров')
plt.ylabel('Средний доход')

# Анализ программы лояльности
ffp_data = df['наличие программы лояльности'].fillna('NO_FFP')  # замена пустых значений на 'NO_FFP'
ffp_counts = ffp_data.value_counts()
ffp_labels = ['Участники программы\nлояльности' if x == 'FFP' else 'Без программы\nлояльности' for x in ffp_counts.index]
plt.figure(figsize=(8, 5))
plt.pie(ffp_counts.values, labels=ffp_labels, autopct='%1.1f%%', startangle=90)
plt.title('Участие в программе лояльности')
plt.show()

# Распределение по способам оплаты
fop_counts = df['способ оплаты'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=fop_counts.values, y=fop_counts.index)
plt.title('Самые популярные способы оплаты')
plt.xlabel('Количество')
plt.show()

# Средняя сумма платежа по способам оплаты
fop_revenue = df.groupby('способ оплаты')['сумма'].mean().sort_values(ascending=False).head(10)
print("Средняя сумма платежа по способам оплаты:")
print(fop_revenue)

# Связь способа оплаты и типа продажи
fop_sale_cross = pd.crosstab(df['способ оплаты'], df['способ покупки'])
fop_sale_melted = fop_sale_cross.reset_index().melt(id_vars=['способ оплаты'], 
                                                    var_name='способ покупки', 
                                                    value_name='COUNT')

plt.figure(figsize=(14, 7))
ax = sns.barplot(data=fop_sale_melted, x='способ оплаты', y='COUNT', hue='способ покупки',
                 palette=['#1f77b4', '#ff7f0e'])
plt.title('Распределение способов продажи по способам оплаты', fontsize=14, fontweight='bold')
plt.xlabel('Способ оплаты')
plt.ylabel('Количество транзакций')
plt.legend(title='Способ продажи', loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Подготовка данных для прогнозирования
daily_sales = df.groupby('дата покупки').size().reset_index(name='количество')
daily_sales = daily_sales.sort_values('дата покупки')

daily_sales['день'] = daily_sales['дата покупки'].dt.dayofyear
daily_sales['месяц'] = daily_sales['дата покупки'].dt.month
daily_sales['год'] = daily_sales['дата покупки'].dt.year

X = daily_sales[['день', 'месяц', 'год']]
y = daily_sales['количество']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(12, 6))
plt.plot(daily_sales['дата покупки'], daily_sales['количество'], label='Фактические значения')
plt.title('Прогнозирование объемов продаж')
plt.xlabel('Дата')
plt.ylabel('Количество продаж')
plt.legend()
plt.show()