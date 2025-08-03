#sum of digits in a number

num = int(input("enter a positive number:"))
sum_of_digits = 0

while num > 0:
    digits = num % 10
    sum_of_digits += digits
    num //= 10

print("Sum of digits :", sum_of_digits)