# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:18:09 2022

@author: krzeczyca
"""

"""
Palindrom to coś, co czyta się tak samo od przodu i od tyłu. Hipoteza: 
weź dowolną liczbę naturalną. Jeżeli nie jest palindromem, 
to zapisz ją od tyłu i dodaj obie liczby. 
Jeżeli wynik nadal nie jest palindromem, kontynuuj, traktując go jako daną. 
Przerwij, gdy osiągniesz palindrom, albo po 10. próbie. 
Na przykład: 78+87=165, 165+561=726, 726+627=1353, 1353+3531=4884. 
Napisz program sprawdzający hipotezę dla pierwszych 200 liczb naturalnych 
jako startowych. Czy zawsze osiągniemy palindrom?
"""


def czyPalindrom(x):
#    x = x.lower().replace(" ", "") #zmieniamy wszystkie literki na male i pozbywamy sie spacji
    n = len(x) #zmienna pomocnicza przechowujaca dlugosc slowa
    for i in range(n-1):
        if x[i] != x[n-1-i]: #jezeli znak po przeciwnej stronie (w tej samej kolejnosci od konca) nie bedzie taki sam
            return False #zwroc false
    return True; #jezeli nie napotkano problemow, zwroc true


#sprawdzamy liczbę czy jest palindromem

def revers(x):
  lx=list(str(x))         #przekształcamy liczbę (string) w listę
  lxr=lx[::-1]       #odwracamy listę
  xr="".join(lxr)    #łączy odwróconą listę w jedne string
  return(xr)
#end

def czy_jest_palindrom(x):
  xr=revers(str(x))       #odwracamy stringa
  if x == xr:             #sprawdzamy warunek
    #print(x, "jest palindromem")
    return True
  else: 
    #print(x, "nie jest palindromem")
    return False
#end

#wprowadzamy liczbę, konwertujemy na listę i tworzymy rewers listy
a=input("Enter any natural number: ")

czy_jest_palindrom(a)

suma=int(a)+int(revers(a))
czy_jest_palindrom(suma)


while not(czy_jest_palindrom(suma)):
  if czy_jest_palindrom(suma):
    print(suma, "This is palindrom")
    break
    #return False
  else:
    suma=suma+int(revers(suma))

print("done")