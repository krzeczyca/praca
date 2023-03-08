# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:41:43 2022

@author: krzeczyca
"""

stan="t"

while stan=="t":

  a=int(input("Podaj liczbę: "))
  
  if a==0:
    print("wpisałes 0 !")
  elif a > 0:
    print("wpisałe liczbę dodatnią")
  elif a < 0:
    print("wpisałes liczbę ujemna")
  stan=input("od nowa t//n: ")
