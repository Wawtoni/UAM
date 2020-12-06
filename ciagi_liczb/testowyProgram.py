x,y=map(int,input().split())
p = input();

for i in range(x,y+1):
    if p == "p":
        if i%2 == 0:
            print(i)
    elif p == "n":
        if i%2 == 1:
            print(i)