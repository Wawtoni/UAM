iz = int(input())
wyniki = []
for x in range(iz):
    il = int(input())
    liczby = input()
    wyniki1 = []
    wyniki1 = liczby.split(" ")
    zliczaj = 0
    for i1 in range(il):
        for i2 in range(il):
            if i1 < i2:
                if wyniki1[i1]>wyniki1[i2]:
                    zliczaj = zliczaj + 1
    wyniki.append(zliczaj)
for a in wyniki:
    print(a)
