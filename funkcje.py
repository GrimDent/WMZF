#funkcja tworząca dane do wyświetlenia na wykresie, wyniki zapisane jako tablice jednowymiarowe
def funkcje(G, m1, m2, s, V1, V2):
    import numpy as np
    v10 = (G*m2)/(s)
    v11 = (G*m2)/(9*s/10)
    v12 = (G*m2)/(8*s/10)
    v13 = (G*m2)/(7*s/10)
    v14 = (G*m2)/(6*s/10)
    v15 = (G*m2)/(5*s/10)
    v16 = (G*m2)/(4*s/10)
    v17 = (G*m2)/(3*s/10)
    v18 = (G*m2)/(2*s/10)
    v19 = (G*m2)/(s/10)
    x1 =np.array([s, s*9/10, s*8/10, s*7/10, s*6/10, s*5/10, s*4/10, s*3/10, s*2/10, s/10, 0])
    y1 =np.array([v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, V1])
    if y1[9]>y1[10]:
        x1 = np.delete(x1, len(x1) - 1, 0)
        y1 = np.delete(y1, len(y1) - 1, 0)

    v20 = (G*m1)/(s)
    v21 = (G*m1)/(9*s/10)
    v22 = (G*m1)/(8*s/10)
    v23 = (G*m1)/(7*s/10)
    v24 = (G*m1)/(6*s/10)
    v25 = (G*m1)/(5*s/10)
    v26 = (G*m1)/(4*s/10)
    v27 = (G*m1)/(3*s/10)
    v28 = (G*m1)/(2*s/10)
    v29 = (G*m1)/(s/10)
    x2 =np.array([s, s*9/10, s*8/10, s*7/10, s*6/10, s*5/10, s*4/10, s*3/10, s*2/10, s/10, 0])
    y2 =np.array([v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, V2])
    if y2[9]>y2[10]:
        x2 = np.delete(x2, len(x2) - 1, 0)
        y2 = np.delete(y2, len(y2) - 1, 0)

    return x1, y1, x2, y2

#funkcja rysująca wykres na podstawie dostarczonych tablic jednowymiarowych
def wykresy(x1, y1, x2, y2):
    import matplotlib.pyplot as plt
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.title('Zależnosc predkosci od odległości')
    plt.xlabel('odleglosc')
    plt.ylabel('predkosc')
    plt.legend(['cialo1', 'cialo2'])
    plt.show()

#funkcja sprawdzająca czy podana przez użytkownika wartość jest liczbą i czy jest większa od zera.
def test(x):
    try:
        float(x)
    except ValueError:
        print('Podana wartość nie jest liczbą!')
        return False
    else:
        if float(x) > 0:
            return True
        else:
            print('Podana wartość nie może być ujemna, nie może też być zerem')
            return False
