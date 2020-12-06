ilosc = int(input()) #pobranie ilosci liczb
liczby = input() #pobranie ciagu liczb do sortowania
wyniki = [] #utworzenie pustej tablicy
wyniki = liczby.split(" ") #rozdzielenie ciągu liczb na poszczególne elementy tablicy
for x in range(ilosc-1):
    test = 0
    for a in range(ilosc - 1):
        if int(wyniki[a]) > int(wyniki[a+1]):
            wyniki[a], wyniki[a+1] = wyniki[a+1], wyniki[a] #zamiana miejscami elementów tablicy
            test = 1
    if test == 0:
        break #zakonczenie petli jezeli juz nie wykonano zadnej zamiany
print(wyniki) #wypisanie tablicy