liczby = input()
wyniki = []
wyniki = liczby.split(" ")
p1 = int(wyniki[0])
p2 = int(wyniki[1])
ilosc = int(input())

suma = 0

rzuty = input()
wyniki = []
wyniki = rzuty.split(" ")
for x in range(ilosc):
    cel = int(wyniki[x])

    if cel >= p1 and cel <= p2:
        suma = 0
    else:
        if cel < p1:
            suma = suma + (p1-cel)
        else:
            suma = suma + (cel-p2)
print(suma)