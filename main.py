#-----------------------------------------------------------------------------------

#Projekt ze Wstępu do Modelowania Zjawisk Fizycznych

#Autorzy: Kamil Sojka, Piotr Leymańczcyk

#-----------------------------------------------------------------------------------
plik=open('wyniki.txt', 'a')
print("masa pierwszego obiektu w kg: ")
m1=5.972*10**24
#m1=float(input())
print("promień pierwszego obiektu w m: ")
r1=6378.137
#r1=float(input())
print("masa drugiego obiektu w kg: ")
m2=7.3477*10**22
#m2=float(input())
print("promień drugiego obiektu w m: ")
r2=1737.1
#r2=float(input())
print("odległość pomiędzy powirzchniami obiektów w m: ")
s=384400
#s=float(input())
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

plik.writelines(t)
plik.close()

import matplotlib.pyplot as plt

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
x1 = [s, s*9/10, s*8/10, s*7/10, s*6/10, s*5/10, s*4/10, s*3/10, s*2/10, s/10, 0]
y1 = [v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, V1]

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
x2 = [s, s*9/10, s*8/10, s*7/10, s*6/10, s*5/10, s*4/10, s*3/10, s*2/10, s/10, 0]
y2 = [v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, V2]


plt.plot(x1,y1)
plt.plot(x2,y2)
plt.title('Zależnosc predkosci od czasu')
plt.xlabel('odleglosc')
plt.ylabel('predkosc')
plt.legend(['cialo1', 'cialo2'])
plt.show()