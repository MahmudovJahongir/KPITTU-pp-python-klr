names= [" али ", "МАНСУР", "зухра", "RUSTAM"]
i=0
print("ввод: ", names)
while i<len(names):
    names[i]=names[i].strip().capitalize()
    if len(names[i])<4:
        names.pop(i)
    else:
        i+=1
print("вывод:", names)
