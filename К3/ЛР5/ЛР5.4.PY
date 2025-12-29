routes = [
    ("Душанбе", 350),
    ("Худжанд", 300),
    ("Куляб", 200),
    ("Бохтар", 250),
    ("Исфара", 400),
]

city_to_find=input("Введите названия города: ")

for city, distance in routes:
    if city.lower()==city_to_find.lower():
        print(f"Расстояние до города {city_to_find}:{distance} км")
        break
else:
    print(f"Маршрут до города {city_to_find} не найден")
