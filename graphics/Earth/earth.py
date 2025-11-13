import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Константы (в условных единицах)
R = 5.0          # Радиус орбиты (условные единицы)
T = 100          # Период обращения — 100 кадров = 1 "год"
omega = 2 * math.pi / T  # Угловая скорость

# Создаём фигуру
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-R - 1, R + 1)
ax.set_ylim(-R - 1, R + 1)
# ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title('Движение Земли вокруг Солнца')

# Солнце в центре
sun = plt.Circle((0, 0), 0.4, color='orange', label='Солнце')
ax.add_patch(sun)

# Земля (начальное положение)
earth_point, = ax.plot([], [], 'bo', markersize=10, label='Земля')

# Орбита (круг)
orbit = plt.Circle((0, 0), R, color='gray', fill=False, linestyle='--', alpha=0.5)
ax.add_patch(orbit)

# Обновление кадра
def update(frame):
    angle = omega * frame          # Текущий угол
    x = R * math.cos(angle)        # Координата Земли
    y = R * math.sin(angle)
    earth_point.set_data([x], [y])
    return earth_point,

# Анимация
ani = FuncAnimation(
    fig, update, frames=T, blit=True,
    interval=50, repeat=True
)

ax.legend()
plt.show()
