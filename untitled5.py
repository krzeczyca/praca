# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:28:13 2022

@author: krzeczyca
"""

  

n=input(">>")
for i in range(1,int(n)):
  elem=[]
  for i in list(n):
    elem.append(int(i)**len(list(n)))
  if sum(elem) == int(n):
    print(sum(elem))

upp_search=input(">>> ")
for n in range(1,int(upp_search+1)):
  la=[str(n)]
  a=[]
  for i in la:
    a.append(int(i)**len(la))
  if sum(a)==int(n):
    print(n, "is Amstrong number")