sales=[]
n=int(input("Сколько дней продаж?: "))
for i in range(n):
    value = int(input("Продажи за день : "))
    sales.append(value)
                
growth_days=0
max_growth=0


for i in range(1, len(sales)):
    if sales[i] > sales[i-1]:
        growth_days+=1
        growth = sales[i]- sales[i - 1]
        if growth > max_growth:
            max_growth = growth
            
print("продажи: ", sales)
print("Дней роста:", growth_days)
print("максимальный рост:", max_growth)
