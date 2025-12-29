def fib(n):
    if n < 0:
        print("Ошибка")
        return
    
    a, b= 0, 1
    for _ in range(n):
        yield a
        a, b= b, a+b
        
print(list(fib(7)))

print(list(fib(0)))

print(list(fib(-3)))
