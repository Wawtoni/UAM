ilosc = int(input())
najwyzszy = 0
liczby = input()
wyniki = []
wyniki = liczby.split(" ")
for a in wyniki:
    if int(a) > najwyzszy:
        najwyzszy = int(a)
print(najwyzszy)
