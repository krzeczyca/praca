# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 07:50:25 2023

@author: krzeczyca

"""

# Generator haseł

import random

def input_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print ("This is not a number!")

def gen_pass(lenght):
  """
  The function returns a random string with list of chars 

  Parameters
  ----------
  length : int
    length password 

  Returns
  -------
  str : string

  """
  str = []
  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-{}][\\"\':;,./?><'
  for k in range(1, lenght+1):
    str.append(random.choice(chars))
  str = "".join(str)
  return(str)

if __name__ == "__main__":
  file = input("What file name? ")
  much = input_int("How many password to generate? ")
  long = input_int("How long do you want the string to be?  ")
  with open(file, 'x', encoding="utf-8") as f:
    for i in range(much):
      f.write(str(i+1)+". "+gen_pass(long)+"\n")
  print("The results have been saved to a file",file)
      