import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

x = []
y = []
for i in range(4):
    y.append(-0.25 * i + 1)
    x.append(i)

for i in range(4,10):
    x.append(i)
    y.append((i-4)/3)

for i in range(10,14):
    x.append(i)
    y.append(2 + 0.6 * math.sin(3.14/2 * (i - 10)))

for i in range(14,21):
    x.append(i)
    y.append(0.5/6 * (i - 14) + 2)

fig, ax = plt.subplots()

line = ax.plot([],[])[0]

def animation(frame):
    x_animation = x[:frame +1]
    y_animation = y[:frame +1]
    line.set_data(x_animation,y_animation)
    return line,

ani = FuncAnimation(fig,animation,frames=30,interval=100, repeat=True)
ax.set_xlim(0,20)
ax.set_ylim(0,5)
plt.show()
