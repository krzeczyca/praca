# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:52:27 2022

@author: Krzysztof Rzeczyca

Liczby Armstronga to N-cyfrowa liczba naturalna która jest sumą swoich cyfr
podniesionych do potęgi N. Na przykład: 153 = 1**3+5**+3**3. Proszę napisać
program znajdujący jak najwięcej takich liczb.
Proszę pamiętać o możliwości konwersji liczby na napis (str(153) → „153”),
napisu na liczbę (int(„5”) → 5) oraz iteracji po napisie pętlą for.
"""


def num_Amstrong(scope):
  """
  Funkcja zwraca listę zawierającą liczby Amstronga z zakresu parametru scope 

  Parameters
  ----------
  scope : int
    Liczba do wartoci której funkcja poszukuje liczb Amstronga.

  Returns
  -------
  results : list
    Lista zawierająca wyszukane liczby Amstronga.

  """
  results = []
  for n in range(10,scope):
    la = list(str(n))
    p = len(la)
    a = list()
    for i in la:
      a.append(int(i)**p)
    if sum(a) == int(n):
      results.append(n)
  return results

      
z=20000
print(num_Amstrong(z))