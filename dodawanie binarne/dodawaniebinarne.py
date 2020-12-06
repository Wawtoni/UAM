iz = int(input())
wyniki = []
for x in range(iz):
    il1 = int(input())
    liczby = input()
    wyniki1 = []
    wyniki1 = liczby.split(" ")
    il2 = int(input())
    liczby = input()
    wyniki2 = []
    wyniki2 = liczby.split(" ")
    tekst1 = "".join(wyniki1)
    tekst2 = "".join(wyniki2)
    suma = int(tekst1, 2) + int(tekst2, 2)
    wyniki.append(bin(suma))
for a in wyniki:
    print(a[2:])