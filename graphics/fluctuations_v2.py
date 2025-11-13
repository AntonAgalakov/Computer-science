import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# === Параметры первого процесса ===
A1 = 2.0            # начальная амплитуда
k1 = 0.05           # коэффициент затухания
omega1 = 3 * math.pi  # угловая частота колебаний: f = 1.5 Гц

# === Параметры второго процесса ===
A2 = 2.0            # начальная амплитуда
k2 = 0.1            # коэффициент затухания (сильнее)
omega2 = 3 * math.pi  # угловая частота (та же)

# === Временные параметры ===
dt = 0.05           # шаг по времени
t_max = 10          # конечное время
steps = int(t_max / dt)  # количество шагов

# === Предвычисление данных ===
t_vals = [i * dt for i in range(steps)]

# Значения функций
x1_vals = [A1 * math.exp(-k1 * t) * math.cos(omega1 * t) for t in t_vals]
x2_vals = [A2 * math.exp(-k2 * t) * math.cos(omega2 * t) for t in t_vals]

# Огибающие
env1_up   = [ A1 * math.exp(-k1 * t) for t in t_vals]
env1_down = [-A1 * math.exp(-k1 * t) for t in t_vals]
env2_up   = [ A2 * math.exp(-k2 * t) for t in t_vals]
env2_down = [-A2 * math.exp(-k2 * t) for t in t_vals]

# === Настройка графиков ===
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Настройка осей
ax1.set_ylim(-1.1 * A1, 1.1 * A1)
ax1.set_title("Затухающие колебания (процесс 1)")
ax1.set_ylabel("Смещение x1(t)")
ax1.grid(True)

ax2.set_xlim(0, t_max)
ax2.set_ylim(-1.1 * A2, 1.1 * A2)
ax2.set_title("Затухающие колебания (процесс 2)")
ax2.set_xlabel("Время (с)")
ax2.set_ylabel("Смещение x2(t)")
ax2.grid(True)

# Огибающие (пунктирные линии)
ax1.plot(t_vals, env1_up, 'r--', alpha=0.5, label='Огибающая')
ax1.plot(t_vals, env1_down, 'r--', alpha=0.5)
ax1.legend()

ax2.plot(t_vals, env2_up, 'b--', alpha=0.5, label='Огибающая')
ax2.plot(t_vals, env2_down, 'b--', alpha=0.5)
ax2.legend()

# Линии и точки для анимации
line1, = ax1.plot([], [], 'r-', lw=2)
point1, = ax1.plot([], [], 'ro', markersize=6)

line2, = ax2.plot([], [], 'b-', lw=2)
point2, = ax2.plot([], [], 'bo', markersize=6)

# === Функция анимации ===
def animate(frame):
    if frame == 0:
        line1.set_data([], [])
        line2.set_data([], [])
        point1.set_data([], [])
        point2.set_data([], [])
    else:
        line1.set_data(t_vals[:frame], x1_vals[:frame])
        point1.set_data([t_vals[frame - 1]], [x1_vals[frame - 1]])

        line2.set_data(t_vals[:frame], x2_vals[:frame])
        point2.set_data([t_vals[frame - 1]], [x2_vals[frame - 1]])
    return line1, line2, point1, point2

# === Запуск анимации ===
ani = animation.FuncAnimation(
    fig, animate,
    frames=steps,
    interval=40,
    blit=True,
    repeat=False
)

plt.tight_layout()
plt.show()
