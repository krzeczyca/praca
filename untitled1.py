# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:04:10 2022

@author: krzeczyca
"""
from math import sqrt

def dzielniki(x):
  lista_dz=[]
  for i in range(1,x+1):
    if x%i == 0:
      lista_dz.append(i)
  return lista_dz

def sum_dz(x):
  suma=

liczba=int(input("enter number: "))

print(dzielniki(liczba))

