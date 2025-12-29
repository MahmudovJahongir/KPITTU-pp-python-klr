code=input("введите код маршрута: " )
left=0 
right=len(code)-1
is_palindrome= True
while left < right :
    if code[left] != code[right]:
        is_palindrome = False
        break
    left+=1
    right-=1
if is_palindrome:
    print("Код маршрута является палиндромом")
else:
    print("код маршрута не является палиндромом")

