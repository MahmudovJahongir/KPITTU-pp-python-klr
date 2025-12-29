def max_vowels(s ,k):
    vowels = "aeiouAEIOU"
    count=0 
    
    for i in range(k):
        if s[i] in vowels:
            count+=1      
    max_count=count
    for i in range(k, len(s)):
        if s[i] in vowels:
            count+=1
        if s[i-k] in vowels:
            count-=1
            
        if count > max_count:
            max_count = count
            
    return max_count

s=input("Введите строку: ")
k=int(input("Введите длину подстроки k:"))
            
result=max_vowels(s,k)
print("макс кол-во гласных: ", result)
