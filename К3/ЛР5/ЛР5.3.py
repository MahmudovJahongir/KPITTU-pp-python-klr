routes = [
    ("Душанбе", 350),
    ("Худжанд", 300),
    ("Куляб", 200),
    ("Бохтар", 250),
    ("Исфара", 400),
]
sorted_by_distance=sorted(routes, key=lambda x: x[1])
print("По расстоянию:", sorted_by_distance)

sorted_by_city=sorted(routes, key=lambda x: x[0])
print("По названию города:", sorted_by_city)

