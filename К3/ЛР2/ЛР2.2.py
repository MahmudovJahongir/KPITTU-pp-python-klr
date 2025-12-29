text=input("Введите число через пробел: ")
nums=[int(x) for x in text.split()]
max_so_far=nums[0]
index=0
for i in range(1, len(nums)):
    if nums[i]> max_so_far:
        max_so_far=nums[i]
        index=i
        
print("Число: ", max_so_far)
print("Индекс: ", index)
