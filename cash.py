import numpy as np
import matplotlib.pyplot as plt

"""
'графики'
x = np.linspace(-10, 1, 1000)
y = np.sin(2*x)**2 * np.exp((x+2) / 10)**2
plt.figure(figsize=(9, 5))
plt.grid(lw=1, ls='--')
plt.plot(x, y, lw=2, color='red')
plt.show()

"диграммы разброса"
n = 250
x = np.linspace(-3 * np.pi, 3 * np.pi, n)
y = np.sin(x) + 0.05 * np.random.normal(loc=1.0, scale=4.0, size=x.size)
plt.figure(figsize=(10, 5))
plt.title(
    label='название',
    fontsize=20
)
plt.xlabel("x", fontsize=15)
plt.ylabel("y", fontsize=15)
plt.tick_params(labelsize=10)

'''
свои значения для осей
plt.xticks(
    ticks=np.arange(-10,11,2)
);
plt.yticks(
    ticks=np.arange(-1.5, 2, 0.5)
    
    labels = ['a', 'b', 'c', 'd'][::-1]
)
'''
plt.scatter(x, y)
plt.show()


'гистграммы'
y = np.random.standard_cauchy(size=10**7)
plt.figure(figsize=(10, 5))
plt.hist(y,
    range=(0, 5),  #дипазон
    bins=50,       #количество разбиений
    density=True   #нормировка
);
plt.show()



#np.concatenate() - объединение нескольких графиков (суммирование)

'круговые диаграммы'

N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)

plt.figure(figsize=(6, 6))
plt.axes(projection='polar')
plt.scatter(theta, r, s=200*r**2, c=theta, cmap='cool', alpha=0.8)

counts = [17, 3]
plt.figure(figsize=(5, 5))
plt.pie(counts,
        colors=['royalblue', 'gold'],
        labels=['Dogs', 'Cats'],
        startangle=20,
        autopct='%.3f%%')

plt.show()


'графики с погрешностями'

x = np.linspace(-5, 5, 40)
y = np.sin(x) + np.tanh(2*(x-2))
yerr = abs(2 * np.random.sample(size=y.size) - 1)

plt.figure(figsize=(10, 5))
plt.errorbar(x, y,
             yerr=yerr,
             color='yellow',
             ecolor='forestgreen',
             capsize=10,
             elinewidth=1.5)
plt.show()



'подгафики'

fig, ax = plt.subplots(nrows=2, ncows=2, figsize=(0, 6))
#ax[0, 0].plot(x, y, label='abc')
for i in ax.flatten():
    i.legend()

"""

'двумерные графики'

def func(x, y):
    return (x - 1)**2 - (y + 2)**2

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)

X, Y = np.meshgrid(x, y)
z = func(X, Y)

fig, ax = plt.subplots(1, 1, figsize=(6, 5))
obj = ax.imshow(z, cmap=plt.cm.seismic, vmin=-400, vmax=400)
fig.colorbar(obj)
plt.show()

