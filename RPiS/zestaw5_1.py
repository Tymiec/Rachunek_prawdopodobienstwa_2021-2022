import numpy as np
import matplotlib.pyplot as plt


def rozklad_poisson(lmbd):
    L = np.exp(-lmbd)
    k = 0
    p = 1

    while True:
        k = k + 1
        u = np.random.uniform(0, 1)
        p = p * u

        if p <= L:
            break
    return k - 1


def num(parametr):
    y = [0] * parametr
    k = 0
    while k < parametr:
        y[k] = rozklad_poisson(4)
        k = k + 1
    return y

print()
p1 = np.random.poisson(4, 10000)
plt.hist(p1, 14, density = True)
plt.title('Oczekiwany rozkład Poisson')
plt.grid()
plt.savefig("wynik_oczekiwany.svg", format="svg")
plt.show()

p2 = num(10000)
plt.hist(p2, 14, density = 'True', color = '#FF7F0E')
plt.title('Otrzymany rozkład Poisson')
plt.grid()
plt.savefig("wynik_otrzymany.svg", format="svg")
plt.show()

plt.hist(p1)
plt.hist(p2)
plt.title("Porównanie wyników")
plt.legend(["Wyniki Otrzymane", "Wyniki Oczekiwane"])
plt.grid()
plt.savefig("porownanie_wynkow.svg", format="svg")
plt.show()