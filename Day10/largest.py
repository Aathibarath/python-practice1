#Find the largest element in a list

numbers = (input("enter numbers seperated by spaces:")).split()
numbers = [int(num) for num in numbers]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)