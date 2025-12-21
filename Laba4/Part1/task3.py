import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse

fig, ax = plt.subplots()    # создаем фигуру и оси(область рисования)

# Лапы
leg1 = Ellipse((2.9, 2.1), 0.8, 2.2, angle=-30, facecolor='#8B4513', edgecolor='#654321', linewidth=1)
leg2 = Ellipse((3.2, 2.1), 0.8, 2.2, facecolor="#743A11", edgecolor='#654321', linewidth=1)
leg3 = Ellipse((6.7, 2.1), 0.8, 2.2, angle=5, facecolor="#7A3E13", edgecolor='#654321', linewidth=1)
leg4 = Ellipse((6.9, 2.1), 0.8, 2.2, angle=24, facecolor='#8B4513', edgecolor='#654321', linewidth=1)
ax.add_patch(leg2)
ax.add_patch(leg1)
ax.add_patch(leg3)
ax.add_patch(leg4)

# Хвост
tail = Ellipse((7.8, 4), 0.7, 2.4, angle=-30, facecolor='#8B4513', edgecolor='#654321', linewidth=2)
ax.add_patch(tail)

# Тело собаки
body = Ellipse((5, 3), 5.6, 2, facecolor='#8B4513', edgecolor='#654321', linewidth=2)
ax.add_patch(body)

# Уши
left_ear = Ellipse((1.1, 4.9), 0.8, 2, angle=-43, facecolor="#783C11", edgecolor='#654321', linewidth=2)

ax.add_patch(left_ear)


# Голова
head = Circle((2.2, 4.4), 1.2, facecolor='#8B4513', edgecolor='#654321', linewidth=2)
ax.add_patch(head)

# Язык
tongue = Ellipse((1.4, 3.6), 0.6, 1.2, angle=-38, facecolor='pink', edgecolor='lightcoral', linewidth=1)
ax.add_patch(tongue)

# Морда
snout = Ellipse((1.6, 4), 1.4, 1, facecolor='#DEB887', edgecolor='#654321', linewidth=1)
ax.add_patch(snout)

# Нос
nose = Circle((1.4, 4.2), 0.3, facecolor='black', edgecolor='black')
ax.add_patch(nose)

# Глаза
left_eye = Circle((1.6, 4.9), 0.22, facecolor='white')
right_eye = Circle((2.5, 4.8), 0.22, facecolor='white')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Блики в глазах
left_glint = Circle((1.6, 4.9), 0.18, facecolor='black')
right_glint = Circle((2.5, 4.8), 0.18, facecolor='black')
ax.add_patch(left_glint)
ax.add_patch(right_glint)

right_ear = Ellipse((3.1, 4.8), 1, 1.8, angle=30, facecolor='#8B4513', edgecolor='#654321', linewidth=2)
ax.add_patch(right_ear)

# Пятна на теле для реалистичности
spots = [
    Circle((3.7, 3.2), 0.4, facecolor='#654321'),
    Circle((6.6, 3.3), 0.3, facecolor='#654321'),
    Circle((5.4, 2.8), 0.2, facecolor='#654321')
]
for spot in spots:
    ax.add_patch(spot)

ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')  # скрываем оси

# Добавляем текст
ax.text(5, 9.5, 'Собака с высунутым языком!', fontsize=16, ha='center', color='#8B4513')

plt.tight_layout()
plt.show()