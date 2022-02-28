import math
import numpy as np
import matplotlib.pyplot as plt


def rot_func(y_ax):
    x_ax = []
    for i in y_ax:
        if 0<i<=1/6:
            x_ax.append(math.sqrt(6*i)-1)
        elif 1/6<i<=5/6:
            x_ax.append(3*i-1/2)
        elif 5/6<i<=1:
            x_ax.append(3-math.sqrt(6-6*i))
    return x_ax

print()

rozmiar1 = 10**4
rozmiar2 = 10**7 #maksymalny rozmiar dla komputera posiadającego 16 GB ramu który nie kończy się memory error
x = np.array([-1, 0, 2, 3])
y = np.array([0, 1/3, 1/3, 0])
y1 = np.random.uniform(0, 1, rozmiar1)
x1 = rot_func(y1)

plt.title(f"Porównanie funkcji dla {rozmiar1} losowanych liczb")
plt.plot(x, y, 'bo-', label="funkcja teoretyczna", color = 'green')
plt.hist(x1, density=True, bins=60, label='funkcja "eksperymentalna"', ec = "black")
plt.ylim(0, 0.6)
plt.legend(loc = "best")
# plt.savefig("wykres_10_do_4_4.jpg", bbox_inches='tight')
# plt.savefig("wykres_10_do_4.svg", bbox_inches='tight')
plt.show()

plt.clf()

y2 = np.random.uniform(0, 1, rozmiar2)
x2 = rot_func(y2)

plt.title(f"Porównanie funkcji dla {rozmiar2} losowanych liczb")
plt.plot(x, y, 'bo-', label="funkcja teoretyczna", color = 'yellow')
plt.hist(x2, density=True, bins=60, label='funkcja "eksperymentalna"', color='#FF7F0E', ec = "black")
plt.ylim(0, 0.45)
plt.legend(loc = "best")
# plt.savefig("wykres_10_do_7.jpg", bbox_inches='tight')
# plt.savefig("wykres_10_do_7.svg", bbox_inches='tight')
plt.show()

plt.hist(x1, density=True, bins=60, label='funkcja "eksperymentalna"', ec = "black")
plt.hist(x2, density=True, bins=60, label='funkcja "eksperymentalna"', color='#FF7F0E', ec = "black")
plt.title("Porównanie wyników")
plt.show()

