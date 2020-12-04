#-----------------------------------------------------------------------------------

#Projekt ze Wstępu do Modelowania Zjawisk Fizycznych

#Autorzy: Kamil Sojka, Piotr Leymańczcyk

#-----------------------------------------------------------------------------------
plik=open('wyniki.txt', 'a')
print("masa pierwszego obiektu w kg: ")
#m1=2000000000
m1=float(input())
print("promień pierwszego obiektu w m: ")
#r1=1000000
r1=float(input())
print("masa drugiego obiektu w kg: ")
#m2=3000000000
m2=float(input())
print("promień drugiego obiektu w m: ")
#r2=2000000
r2=float(input())
print("odległość pomiędzy powirzchniami obiektów w m: ")
#s=10000000
s=float(input())
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