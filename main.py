#-----------------------------------------------------------------------------------

#Projekt ze Wstępu do Modelowania Zjawisk Fizycznych

#Autorzy: Kamil Sojka, Piotr Leymańczcyk

#-----------------------------------------------------------------------------------

#masa pierwszego obiektu w kg
m1=2000000000
#promień pierwszego obiektu w m
r1=1000000
#masa drugiego obiektu w kg
m2=3000000000
#promień drugiego obiektu w m
r2=2000000
#odległość pomiędzy powirzchniami obiektów w m
s=10000000
#Stała grawitacji
G=6.67430*10**(-11)
#siła oddziaływania grawitacyjnego między obiektami w
F=(G*m1*m2)/s**2
print('siła oddziaływania grawitacyjnego między obiektami na w t=0', F, 'Newtonów\n')
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