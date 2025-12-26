import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Настройка стиля графиков
plt.style.use('default')
sns.set_palette("husl")

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA')   # загружаем таблицу из файла
df.columns = ['дата покупки', 'дата совершения перелета', 'тип пассажиров', 'сумма', 'способ оплаты', 'город отправления', 'город назначения', 'тип перелета', 'наличие программы лояльности', 'способ покупки']

pax_type_names = {
    'AD': 'Взрослый',
    'CHD': 'Ребёнок',
    'INF': 'Неизвестно',
    'FIM': 'Семейный'
}

fop_names = {
    'AH': 'Корп. счёт',
    'AI': 'Корп. счёт',
    'BN': 'Бонусы',
    'CA': 'Наличные',
    'CC': 'Кредитная карта',
    'DP': 'Динамическое\nценообразование',
    'EX': 'Прочее',
    'FF': 'Оплата милями',
    'FS': 'Частично милями',
    'IN': 'Корп. счёт',
    'LS': 'Скидка 10%',
    'MC': 'Прочее',
    'PS': 'Подарок',
    'VO': 'Ваучер'
}

ffp_names = {
    'FFP': 'Да',
    np.nan: 'Нет'
}

#  перевод
df['тип пассажиров'] = df['тип пассажиров'].map(pax_type_names).fillna('Неизвестно')
df['способ оплаты'] = df['способ оплаты'].map(fop_names).fillna('Прочее')
df['наличие программы лояльности'] = df['наличие программы лояльности'].map(ffp_names).fillna('Нет')

print(df.head(10))

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

revenue_stats = df['сумма'].describe().round(2)
print(f"Общая статистика по выручке\n{revenue_stats}")

monthly_stats = df.groupby(df['дата покупки'].dt.to_period('M')).agg({
    'тип пассажиров': 'count',
    'сумма': ['sum', 'mean']
}).round(1).reset_index()

monthly_stats.columns = ['Месяц', 'Количество пассажиров', 'Суммарная выручка', 'Средняя выручка']
print(f"Статистика по месяцам\n{monthly_stats}")

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=monthly_stats.values,
                 colLabels=monthly_stats.columns,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)  # Масштабирование таблицы
plt.title('Статистика по месяцам', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

# Топ-5 аэропортов отправления
top_orig = df['город отправления'].value_counts().head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_orig.index, y=top_orig.values)
plt.title('Топ-5 аэропортов отправления', fontsize=14, fontweight='bold')
plt.xlabel('Аэропорты', fontsize=12)
plt.ylabel('Количество перелетов', fontsize=12)
plt.show()

# Топ-5 аэропортов назначения
top_dest = df['город назначения'].value_counts().head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_dest.index, y=top_dest.values)
plt.title('Топ-5 аэропортов назначения', fontsize=14, fontweight='bold')
plt.xlabel('Аэропорты', fontsize=12)
plt.ylabel('Количество перелетов', fontsize=12)
plt.show()

# Самые популярные маршруты
route_counts = df.groupby(['город отправления', 'город назначения']).size().reset_index(name='Количество перелетов').sort_values(by='Количество перелетов', ascending=False).head(5)
print("Топ-5 популярных маршрутов:")
print(route_counts)

fig, ax = plt.subplots(figsize=(10, 2))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=route_counts.values,
                 colLabels=route_counts.columns,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)  # Масштабирование таблицы
plt.title('Топ-5 популярных маршрутов', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()


monthly_sales = df.groupby(df['дата покупки'].dt.to_period('M')).size()   # количество продаж в месяц 
monthly_revenue = df.groupby(df['дата покупки'].dt.to_period('M'))['сумма'].sum()    # сумма продаж в месяц
monthly_flights = df.groupby(df['дата совершения перелета'].dt.to_period('M')).size()   # количество перелетов в месяц 

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
monthly_sales.plot(kind='line', title='Количество продаж по месяцам')
plt.xlabel('Месяц', fontsize=12)
plt.ylabel('Количество продаж', fontsize=12)

plt.subplot(1, 2, 2)
monthly_revenue.plot(kind='line', title='Сумма продаж по месяцам')
plt.xlabel('Месяц', fontsize=12)
plt.ylabel('Сумма дохода', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
monthly_flights.plot(kind='line', title='Количество перелетов по месяцам')
plt.xlabel('Месяц', fontsize=12)
plt.ylabel('Количество перелетов', fontsize=12)
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
plt.title('Распределение по типам пассажиров', fontsize=14, fontweight='bold')
plt.show()

# Средний доход по типам пассажиров
pax_revenue = df.groupby('тип пассажиров')['сумма'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
sns.barplot(x=pax_revenue.index, y=pax_revenue.values)
plt.title("Выручка по типам пассажиров", fontsize=14, fontweight='bold')
plt.xlabel('Типы пассажиров', fontsize=12)
plt.ylabel('Выручка', fontsize=12)
plt.show()

# Анализ программы лояльности
ffp_counts = df['наличие программы лояльности'].value_counts()
ffp_labels = ['Участники программы\nлояльности' if x == 'Да' else 'Без программы\nлояльности' for x in ffp_counts.index]
plt.figure(figsize=(8, 5))
plt.pie(ffp_counts.values, labels=ffp_labels, autopct='%1.1f%%', startangle=90)
plt.title('Участие в программе лояльности', fontsize=14, fontweight='bold')
plt.show()

# Распределение по способам оплаты
fop_counts = df['способ оплаты'].value_counts().head(10)
plt.figure(figsize=(10, 4))
sns.barplot(x=fop_counts.values, y=fop_counts.index)
plt.title('Самые популярные способы оплаты', fontsize=14, fontweight='bold')
plt.xlabel('Количество покупок', fontsize=12)
plt.show()

# Средняя сумма платежа по способам оплаты
fop_revenue = df.groupby('способ оплаты')['сумма'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 4))
sns.barplot(y=fop_revenue.index, x=fop_revenue.values)
plt.title('Средняя цена билета по способу оплаты', fontsize=14, fontweight='bold')
plt.xlabel('Цена', fontsize=12)
plt.ylabel('Способ оплаты', fontsize=12)
plt.tight_layout()
plt.show()
print("Средняя сумма платежа по способам оплаты:")
print(fop_revenue)

# Связь способа оплаты и типа продажи
fop_sale_cross = pd.crosstab(df['способ оплаты'], df['способ покупки'])
fop_sale_melted = fop_sale_cross.reset_index().melt(id_vars=['способ оплаты'], 
                                                    var_name='способ покупки', 
                                                    value_name='COUNT')
print("Связь способа оплаты и типа продажи:")
print(fop_sale_cross)

plt.figure(figsize=(10, 4))
sns.barplot(data=fop_sale_melted, x='способ оплаты', y='COUNT', hue='способ покупки',
                 palette=['#1f77b4', '#ff7f0e'])
plt.title('Распределение способов продажи по способам оплаты', fontsize=14, fontweight='bold')
plt.xlabel('Способ оплаты', fontsize=12)
plt.ylabel('Количество транзакций', fontsize=12)
plt.legend(title='Способ продажи', loc='upper left')
plt.tight_layout()
plt.show()

# Подготовка данных для прогнозирования
daily_sales = df.groupby(df['дата покупки'].dt.date).size().reset_index(name='количество')
daily_sales['дата покупки'] = pd.to_datetime(daily_sales['дата покупки'])
daily_sales = daily_sales.sort_values('дата покупки')

# Создание признаков для модели
daily_sales['день_года'] = daily_sales['дата покупки'].dt.dayofyear
daily_sales['месяц'] = daily_sales['дата покупки'].dt.month
daily_sales['год'] = daily_sales['дата покупки'].dt.year

# Разделение на обучающую и тестовую выборки
X = daily_sales[['день_года', 'месяц', 'год']]
y = daily_sales['количество']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание на всей выборке
y_pred_all = model.predict(X)

plt.figure(figsize=(10, 6))
plt.plot(daily_sales['дата покупки'], daily_sales['количество'], 'b-', alpha=0.7, linewidth=1.5, label='Фактические значения')
plt.plot(daily_sales['дата покупки'], y_pred_all, 'r--', alpha=0.8, linewidth=1.5, label='Прогноз модели')

# Добавляем вертикальную линию разделения
train_size = len(X_train)
plt.axvline(x=daily_sales['дата покупки'].iloc[train_size], color='green', linestyle=':', linewidth=2, label='Разделение на train/test')

# Подсветка тестовой области
test_start = daily_sales['дата покупки'].iloc[train_size]
test_end = daily_sales['дата покупки'].iloc[-1]
plt.axvspan(test_start, test_end, alpha=0.1, color='yellow', label='Тестовая область')

plt.title('Прогнозирование объемов продаж авиабилетов', fontsize=14, fontweight='bold')
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Количество продаж', fontsize=12)
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()