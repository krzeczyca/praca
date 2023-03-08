# -*- coding: utf-8 -*-
"""
@author: Krzysztof Rzeczyca

  Liczby Armstronga to N-cyfrowa liczba naturalna która jest sumą swoich cyfr
  podniesionych do potęgi N. Na przykład: 153 = 1**3+5**+3**3. Proszę napisać
  program znajdujący jak najwięcej takich liczb.
  Proszę pamiętać o możliwości konwersji liczby na napis (str(153) → „153”),
  napisu na liczbę (int(„5”) → 5) oraz iteracji po napisie pętlą for.

Program wykorzystuje funkcję input_int z 2-ego labolatorium.

Przykładowy wynik programu:
  Podaj zakres poszukiwania Liczb Amstronga: 10000
  Wyszukuję liczby Amstronga do wartosci:  10000 
  Proszę o chwilę cierpliwosci :)
  
  Wyszukane liczby Amstronga to: 
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]  
"""

def input_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print ("To nie jest liczba")
      

def num_Amstrong(scope):
  """
  Funkcja zwraca listę zawierającą liczby Amstronga z zakresu parametru scope 

  Parameters
  ----------
  scope : int
    Liczba do wartosci której funkcja poszukuje liczb Amstronga.

  Returns
  -------
  results : list
    Lista zawierająca wyszukane liczby Amstronga.

  """
  results = []
  for n in range(1,scope):
    la = list(str(n))
    p = len(la)
    a = []
    for i in la:
      a.append(int(i)**p)
    if sum(a) == n:
      #print("Liczba Amstronga jest: ", n)
      results.append(n)
  return results


if __name__ == "__main__":
  zakres = input_int("Podaj zakres poszukiwania Liczb Amstronga: ")      
  print("Wyszukuję liczby Amstronga do wartosci: ", zakres, "\nProszę o chwilę cierpliwosci :)\n")
  print("Wyszukane liczby Amstronga to: \n", num_Amstrong(zakres))