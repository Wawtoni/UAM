liczby = input()
wyniki = []
wyniki = liczby.split(" ")
p1 = int(wyniki[0])
p2 = int(wyniki[1])
cel = int(input())

if cel >= p1 and cel <= p2:
    print("BINGO")
else:
    if cel < p1:
        print(p1-cel)
    else:
        print(cel-p2)