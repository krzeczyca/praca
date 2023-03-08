# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:19:24 2022

@author: krzeczyca

"""

n=input("Specify the upper search range for Armstrong numbers : ")
for i in range(int(n)):

  elem=list()
  for i in list(n):
    elem.append(int(i)**len(list(n)))
  if sum(elem)==int(n): 
    print(sum(elem))
 
""" 
  
upp_search=input("Specify the upper search range for Armstrong numbers : ")
for n in range(10,int(upp_search)):

  la=list(str(n))
  p=len(la)

  a=list()
  for i in la:
    a.append(int(i)**p)
  if sum(a)==int(n):
    print(n, "is Amstrong number")
  """  
    