def analyze_sales(sales):
    if len(sales)<2:
        return None, 0
    max_growt=0
    max_day=None
    growth_days=0
    
    for i in range(1, len(sales)):
        growth=sales[i]-sales[i-1]
        if growth>0:
            growth_days+=1
        if max_day is None or growth>max_growth:
            max_growth=growth
            max_day=i
            
    return max_day, growth_days

test_cases=[
    [100, 120, 110, 150, 140],
    [100, 100, 100],
    [200],
    [50, 60, 70, 80]
]

for sales in test_cases:
    max_day, growth_days = analyze_sales(sales)
    print(f"Sales: {sales}")
    print(f"День с максимальным ростом: {max_day}, Количество дней с ростом: {growth_days}\n")
