import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# === Параметры первого процесса ===
A1 = 2.0            # начальная амплитуда (насколько отклонили систему от равновесия)
k1 = 0.05           # коэффициент затухания (сила сопротивления среды)
omega1 = 3 * math.pi  # угловая частота колебаний: omega = 2*pi*f (f = 1.5 Гц)

# === Параметры второго процесса ===
A2 = 2.0            # начальная амплитуда (та же, что и у первого)
k2 = 0.1            # коэффициент затухания (сильнее, чем у первого — быстрее затухает)
omega2 = 3 * math.pi  # угловая частота (та же, что и у первого)

# === Временные параметры ===
dt = 0.05           # шаг по времени (чем меньше — плавнее анимация, но больше вычислений)
t_max = 10          # время, до которого строится график (в секундах)
steps = int(t_max / dt)  # количество шагов анимации

# === Предвычисление данных ===
t_vals = [i * dt for i in range(steps)]  # список времён [0, dt, 2*dt, ...]

# Значения функций для двух процессов
x1_vals = [A1 * math.exp(-k1 * t) * math.cos(omega1 * t) for t in t_vals]
x2_vals = [A2 * math.exp(-k2 * t) * math.cos(omega2 * t) for t in t_vals]

# Огибающие (экспоненты, ограничивающие амплитуду)
env1_up   = [ A1 * math.exp(-k1 * t) for t in t_vals]  # верхняя огибающая первого процесса
env1_down = [-A1 * math.exp(-k1 * t) for t in t_vals]  # нижняя огибающая первого процесса
env2_up   = [ A2 * math.exp(-k2 * t) for t in t_vals]  # верхняя огибающая второго процесса
env2_down = [-A2 * math.exp(-k2 * t) for t in t_vals]  # нижняя огибающая второго процесса

# === Настройка графика ===
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, t_max)                           # ось X: от 0 до t_max
ax.set_ylim(-1.1 * A1, 1.1 * A1)               # ось Y: от -1.1*A до +1.1*A
ax.set_xlabel("Время (с)")
ax.set_ylabel("Смещение")
ax.set_title("Затухающие колебания (два процесса)")
ax.grid(True)

# Огибающие — пунктирные линии
ax.plot(t_vals, env1_up,   'r--', alpha=0.5, label='Огибающая 1')
ax.plot(t_vals, env1_down, 'r--', alpha=0.5)
ax.plot(t_vals, env2_up,   'b--', alpha=0.5, label='Огибающая 2')
ax.plot(t_vals, env2_down, 'b--', alpha=0.5)

# Линии и точки для анимации
line1, = ax.plot([], [], 'r-', lw=2)   # график первого процесса
line2, = ax.plot([], [], 'b-', lw=2)   # график второго процесса
point1, = ax.plot([], [], 'ro', markersize=6)  # точка на первом графике
point2, = ax.plot([], [], 'bo', markersize=6)  # точка на втором графике

ax.legend()

# === Функция анимации ===
def animate(frame):
    if frame == 0:
        # На первом кадре линии и точки пустые
        line1.set_data([], [])
        line2.set_data([], [])
        point1.set_data([], [])
        point2.set_data([], [])
    else:
        # Обновляем данные: отрезок от 0 до frame
        line1.set_data(t_vals[:frame], x1_vals[:frame])
        line2.set_data(t_vals[:frame], x2_vals[:frame])
        # Точка — на последнем отрезке
        point1.set_data([t_vals[frame - 1]], [x1_vals[frame - 1]])
        point2.set_data([t_vals[frame - 1]], [x2_vals[frame - 1]])
    return line1, line2, point1, point2

# === Запуск анимации ===
ani = animation.FuncAnimation(
    fig, animate,
    frames=steps,       # количество кадров = число шагов
    interval=40,        # задержка между кадрами в мс (~25 FPS)
    blit=True,          # ускоряет анимацию, обновляя только изменившиеся части
    repeat=False        # не зацикливать анимацию
)

plt.tight_layout()
plt.show()
