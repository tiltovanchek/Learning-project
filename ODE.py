from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
"""решение ОДУ первого порядка
f0 = float(input())
dt = 0.001
t = np.arange(0, 2, dt)
func = lambda f, t: f + t
res = odeint(func, f0, t)
print(str(np.round(res[1000], 2))[1:-1:]) """


""" Движение частицы в электрическом поле
x0, vx0 = input().split()
x0, vx0 = float(x0), float(vx0)
dt = 1e-3
t = np.arange(0, 2, dt)

def E(t):
    return np.exp(-0.1*t**2)

def func(r, t):
    x, vx = r
    return [vx, E(t)]

res = odeint(func, y0 = [x0, vx0], t = t)

print(round(res[1000][0], 2))

plt.figure(figsize=(9, 5))
plt.plot(t, res.T[0])
plt.show()  """

""" Задача о взаимодействии двух точечных зарядов
q1, q2 = input().split()
q1, q2 = float(q1), float(q2)
dt = 1e-2
t = np.arange(0, 2, dt)

Q = [q2, q1]
init = [0, 1, 0, 0, 0, 0, 0, 1]
N = 2

def MF(r, t, Q, N = 2):
    x, vx, y, vy = [r[N * i: N * (i + 1)] for i in range(4)]
    dvxdt = np.zeros(N)
    dvydt = np.zeros(N)
    for i in range(N):
        for j in range(N):
            if j != i:
                R = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**0.5
                dvxdt[i] += Q[0] * Q[1] * (x[i] - x[j]) / R**3
                dvydt[i] += Q[0] * Q[1] * (y[i] - y[j]) / R**3
    return [*vx, *dvxdt, *vy, *dvydt]

res = odeint(MF, y0 = init, t = t, args = (Q, N))
x, vx, y, vy = [res.T[N * i: N * (i + 1), :] for i in range(4)]

'''for i in range(N):
    plt.plot(x[i], y[i])
plt.show()'''

fig, ax = plt.subplots(1, 1, figsize=(8, 6))


def animate(tlim):
    ax.clear()
    for i in range(N):
        ax.plot(x[i, : tlim + 1], y[i, :tlim + 1], color='tab:blue', zorder=0)
        ax.scatter(x[i, tlim], y[i, tlim], color='tab:red', s=80)
    ax.set_xlim(1.25 * np.min(x), 1.25 * np.max(x))
    ax.set_ylim(1.25 * np.min(y), 1.25 * np.max(y))


myAnimation = animation.FuncAnimation(fig, animate, frames=t.size - 1)
plt.show()
#plt.close()
myAnimation.save('3body.gif', fps=2000, writer='pillow') """