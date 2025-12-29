dist=[10, 20, 35, 50, 75, 80]
target=85
l=0
r=len(dist)-1
print("список:", dist)
print ("заданная сумма:", target)
while l< r:
    s=dist[l]+dist[r]
    if s== target:
        print("расстояние:", dist[l], dist[r])
        break
    elif s < target:
        l+=1
    else:
        r-=1
else:
    print("Пары нет")

