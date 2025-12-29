students={
    2020: ['ali', "mansur", "mansur"],
    2021: ["ali", "ali", "abu", "Умар", "Вали"],
    2022: ["абдували", "амир", "абубакр", "Мухаммад", "Чахонгир"],
    2023: ["Мухаммад", "ali", "temur", "faridun", "Valiev"],
    2024: ["Умар", "Умар", "Рахим", "Али", "аслиддин"]   
}
c2020=set(students[2024])
top3_sets=[]
from collections import Counter
for year, names in students.items():
    c=Counter(names)
    print(f"Год: {year}")
    print("Студенты:",set(names))
    print("частоты:", c)
    print("top-3:", f.most_common(3))
    print()
