# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:41:25 2022

@author: krzeczyca
"""

"""
def czyPalindrom(x):
    x = x.lower().replace(" ", "") #zmieniamy wszystkie literki na male i pozbywamy sie spacji
    n = len(x) #zmienna pomocnicza przechowujaca dlugosc slowa
    for i in range(n-1):
        if x[i] != x[n-1-i]: #jezeli znak po przeciwnej stronie (w tej samej kolejnosci od konca) nie bedzie taki sam
            return False #zwroc false
    return True; #jezeli nie napotkano problemow, zwroc true

print("Program sprawdzajacy czy slowo jest palindromem")
print("Podaj slowo")
s1 = input() #pobieramy slowo
print("Podane slowo " + ("jest " if(czyPalindrom(s1)) else "nie jest ") + "palindromem")


# Palindrom to coś, co czyta się tak samo od przodu i od tyłu.
#  Hipoteza: weź dowolną liczbę naturalną. Jeżeli nie jest palindromem,
# to zapisz ją od tyłu i dodaj obie liczby. Jeżeli wynik nadal nie jest palindromem, kontynuuj, traktując go jako daną. Przerwij, gdy osiągniesz palindrom. Na przykład: 78+87=165, 165+561=726, 726+627=1353, 1353+3531=4884. Napisz program sprawdzający hipotezę dla pierwszych 200 liczb naturalnych jako startowych. Czy zawsze osiągniemy palindrom?

# funkcja zwracająca palindrom
"""
def szukaj_palindromu(num):
    sum = 0
    sum += int(num)

    # pętla działa tak długo, kiedy sum rzutowane na string nie jest taka sama jak string od tyłu

    while str(sum) != str(sum)[::-1]:
        # przypisanie zmiennej next_num sumy od tyłu
        next_num = int(str(sum)[::-1])
        # sumowanie obu liczb
        sum += next_num
    return sum

# pętla sprawdzająca palindromy dla liczb 0 - 200
for i in range(1, 201):
    # program wpadnie w nieskończoną pętlę przy 200 i 196. Dla tych liczb nie można osiągnąć palindromu
    if(i != 196 and i != 200):
        print('Palindrom dla {}:'.format(i), szukaj_palindromu(i))
    else:
        print('Nie istnieje palindrom dla {}'.format(i))

print('Koniec Programu')