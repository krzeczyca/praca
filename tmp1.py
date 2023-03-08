# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:20:47 2022

@author: krzeczyca
"""


liczba=int(input("podaj liczbę: "))

if liczba < 12:
  print("liczba mniejsza od 12")
  if liczba > 12 and liczba < 18:
    print("liczba pomiędzy 12 i 18")
  else:
    print("liczba większa od 18")



print("liczba mniejsza niż 12" if liczba <= 12 else ("liczba większa niz 12 a mniejsza niz 18" if liczba<=18 else "liczba większa niz 18"))