# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:27:47 2022

@author: krzeczyca
"""

 
def ams(n):
  elem=list()
  for i in list(n):
    elem.append(int(i)**len(list(n)))
  if sum(elem) == int(n):
    return(sum(elem))


def amstron(n):
  elem=list()
  for i in list(n):
    elem.append(i**len(list(n)))
  if sum(elem)==int(n): 
    return sum(elem)



yes="y"
while yes=="y":
  n=input("Specify the upper search range for Armstrong numbers : ")
  for i in range(10,int(n)):
    elem=list()
    for i in list(n):
      elem.append(int(i)**len(list(n)))
    if sum(elem)==int(n): 
      print(sum(elem))

  yes=input("Are we checking a different range y\\n: ")



yes="y"
while yes=="y":
  upp_search=input("Specify the upper search range for Armstrong numbers : ")
  for n in range(10,int(upp_search)):
    la=list(str(n))
    p=len(la)
    a=list()
    for i in la:
      a.append(int(i)**p)
    if sum(a)==int(n):
      print(n, "is Amstrong number")
  yes=input("Are we checking a different range y\\n: ")
