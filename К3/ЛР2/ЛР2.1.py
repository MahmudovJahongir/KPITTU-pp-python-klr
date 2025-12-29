n=int(input("Введите число N:"))
m=int(input("Введите число M:"))
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, "*", j , "=", i*j)
    print()
