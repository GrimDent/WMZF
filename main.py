#-----------------------------------------------------------------------------------

#Projekt ze Wstępu do Modelowania Zjawisk Fizycznych

#Autorzy: Kamil Sojka, Piotr Leymańczcyk

#-----------------------------------------------------------------------------------
import funkcje
print("wpisanie dom przy podawaniu wartości, spowoduje użycie wartości domyślnej. \nWartości te to odpowiednio: masa Ziemi, promień Ziemi, masa księżyca, promień księżyca i odległość księżyca od Ziemi")
while True:
    m1=input("masa pierwszego obiektu w kg: ")
    if m1=='dom':
        m1 = 5.972 * 10 ** 24
    wynikT=funkcje.test(m1)
    if wynikT==True:
        m1=float(m1)
        break

while True:
    r1=input("promień pierwszego obiektu w m: ")
    if r1=='dom':
        r1 = 6378.137
    wynikT = funkcje.test(r1)
    if wynikT == True:
        r1=float(r1)
        break

while True:
    m2=input("masa drugiego obiektu w kg: ")
    if m2=='dom':
        m2 = 7.3477 * 10 ** 22
    wynikT = funkcje.test(m2)
    if wynikT == True:
        m2=float(m2)
        break

while True:
    r2=input("promień drugiego obiektu w m: ")
    if r2=='dom':
        r2 = 1737.1
    wynikT = funkcje.test(r2)
    if wynikT == True:
        r2=float(r2)
        break

while True:
    s=input("odległość pomiędzy powirzchniami obiektów w m: ")
    if s=='dom':
        s = 384400
    wynikT = funkcje.test(s)
    if wynikT == True:
        s=float(s)
        break


#Stała grawitacji
G=6.67430*10**(-11)

#siła oddziaływania grawitacyjnego między obiektami w
F=(G*m1*m2)/s**2
print('siła oddziaływania grawitacyjnego między obiektami na dla t=0: ', F, 'Newtonów\n')

#przyspieszenie pierwszego obiektu
a1=(G*m2)/s**2
print('przyspieszenie pierwszego obiektu wynosi', a1, 'metrów na sekundę do kwadratu\n' )

#przyspieszenie drugiego obiektu
a2=(G*m1)/s**2
print('przyspieszenie drugiego obiektu wynosi', a2, 'metrów na sekundę do kwadratu\n')

#prędkość ciała 1 w chwili zderzenia
V1=(G*m2)/(r1+r2)
print('prędkość ciała 1 w chwili zderzenia wynosi', V1, 'metrów na sekundę\n')

#prędkość ciała 2 w chwili zderzenia
V2=(G*m1)/(r1+r2)
print('prędkość ciała 2 w chwili zderzenia wynosi', V2, 'metrów na sekundę\n')


t=['dane wejściowe',
'\nmasa1=',str(m1),
'\npromień1=',str(r1),
'\nmasa2=',str(m2),
'\npromień2=',str(r2),
'\nodległość=',str(s),

'\n\ndane wyjściowe',
'\nsiła grawitacyjna t=0 =',str(F),
'\nprzyspiesznie1=',str(a1),
'\nprzyspiesznie2=',str(a2),
'\nprędkość w chwili zderzenia 1 =' ,str(V1),
'\nprędkość w chwili zderzenia 2 =' ,str(V2),'\n\n']

plik=open('wyniki.txt', 'a')
plik.writelines(t)
plik.close()

wynik=funkcje.funkcje(G, m1, m2, s, V1, V2)
funkcje.wykresy(wynik[0],wynik[1],wynik[2], wynik[3])