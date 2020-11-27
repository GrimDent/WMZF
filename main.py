#-----------------------------------------------------------------------------------

#Projekt ze Wstępu do Modelowania Zjawisk Fizycznych

#Autorzy: Kamil Sojka, Piotr Leymańczcyk

#-----------------------------------------------------------------------------------

#masa pierwszego obiektu
m1=2
#masa drugiego obiektu
m2=2
#odległość pomiędzy środkami ciężkości obiektów
r=1
#Stała grawitacji
G=6.67430*10**(-11)
#siła
F=(G*m1*m2)/r**2
print(F)
#przyspieszenie pierwszego obiektu
a1=(G*m2)/r**2
print(a1)
#przyspieszenie drugiego obiektu
a2=(G*m1)/r**2
print(a2)