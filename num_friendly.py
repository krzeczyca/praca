# -*- coding: utf-8 -*-
"""
@author: Krzysztof Rzeczyca

  Liczby naturalne a i b nazywamy zaprzyjaźnionymi, jeżeli suma dzielników
  właściwych* a wynosi b, a suma dzielników właściwych b wynosi a. Proszę
  napisać program, który znajduje wszystkie pary liczb zaprzyjaźnionych
  mniejszych od 1000. Pomocą może być jeden z programów z 1. laboratorium.
  *Dzielnik właściwy liczby, to każdy jej dzielnik mniejszy od niej samej, łącznie z 1.
  Przykładowo dzielnikami właściwymi 27 są 1, 3 i 9.

Program wykorzystuje funkcje z programów z 1-ego i 2-ego labolatorium oraz umożliwia 
sprawdzenie szybkosci uzyskania wyników dla większych zakresów poszukiwań.

Przykładowy wynik programu:
  Podaj zakres wyszukiwania liczba zaprzyjaznionych: 1000
  Program wyszukuje liczby zaprzyjaznione mniejsze od: 1000
  Wywolywana funkcja: <function sp_fast at 0x00000266F02B4160>
  Liczby zaprzyjaznione:  220 284
  
  Program wyszukuje liczby zaprzyjaznione mniejsze od: 1000
  Wywolywana funkcja: <function sp at 0x00000266F02B41F0>
  Liczby zaprzyjaznione:  220 284
"""

def input_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print ("To nie jest liczba")


def sp(n):
  """
  Funkcja sp(n) zwraca sumę podzielnikow własciwych, sprawdzajęc czy zadana liczba n
  dzieli sie bez reszty z dzielenia z podzielnikiem z zakresu od 1 do n//2 + 1.

  Parameters
  ----------
  n: int
    liczba, dla której funkcja wylicza sumę podzielników własciwych

  Returns
  -------
  out: int
    suma podzielników własciwych dla parametru n
  """
  s = 0
  for p in range(1, n//2 + 1):
    is_divisible_by_p = n%p == 0
    if is_divisible_by_p:               
      s += p                  
  return s


def sp_fast(n):
  """
  Funkcja sp_fast(n) zwraca sume podzielników własciwych, jest szybsza gdyż 
  dodaje podzielniki parami, zaczynając od sprawdzenia czy liczba n jest podzielna 
  przez 2. 

  Parameters
  ----------
  n: int
    liczba, dla której funkcja wylicza sumę podzielników własciwych

  Returns
  -------
  out: int
    suma podzielników własciwych dla parametru n
  """
  if n == 1:
    return 0
  s = 1
  p = 2
  while p*p < n:
    if n%p == 0:              
      s += p + n//p            
    p += 1                    
  if p*p == n:
    s += p
  return s


def test_sp(sp_function, scope):
  print("Program wyszukuje liczby zaprzyjaznione mniejsze od:", scope)
  print("Wywolywana funkcja: {}".format(sp_function))
  for i in range(2, scope):
    j = sp_function(i)
    if sp_function(j) == i and i<j: 
      print("Liczby zaprzyjaznione: ", i, j)
  print('\n')


if __name__ == "__main__":
  zakres = input_int("Podaj zakres wyszukiwania liczba zaprzyjaznionych: ")
  test_sp(sp_fast, zakres)
  test_sp(sp, zakres)