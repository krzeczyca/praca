# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:41:39 2022

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

a=input("Enter any natural number: ")

#testuje wykonywanie funkcji
czy_jest_palindrom(a)

suma=int(a)+int(revers(a))
czy_jest_palindrom(suma)

#main

while czy_jest_palindrom(suma):
  suma=suma+int(revers(suma))
  if czy_jest_palindrom(suma):
    print(suma, "This is palindrom")
    break
    #return False
  else:
    suma=suma+int(revers(suma))
    
