#count even and odd numbers in a list

nums = [10,20,30,31,25,64,98]

even_count = 0
odd_count = 0 

for num in nums:
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even number:", even_count)
print("Odd numbers:", odd_count)

