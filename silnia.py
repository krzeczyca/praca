"""Zadanie 1 Napisz pętlę, która silnię liczb w zakresie od 2 do 10.

Silnia definiowana jest jako iloczyn wszystkich liczb mniejszych lub równych danej liczby:
𝑛!=1∗2∗3∗...∗𝑛
 
np.:
2!=1⋅2=2
5!=1⋅2⋅3⋅4⋅5=120
 
Program powinien wypisać następujące komunikaty:
1! = 1
2! = 2
3! = 6
...
10! = ?"""

def give_int(prompt):
    while True:
        try:
            return (int(input(prompt)))
        except ValueError:
            print("Give number")

def strong(scope):
    if not scope:
        scope=11
    silnia=1
    for i in range(1,scope+1):
        silnia*=i
    return (silnia)

if __name__ == "__main__":
    sil=give_int("Give number: ")
    print(strong(sil))

"""
    try:
        sil=int(input("give number for enumerate strong: "))
        print(strong(sil))
    except ValueError:
        print("Podaj liczbę! Good bye")
"""