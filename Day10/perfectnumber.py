#check if a number is a perfect number

num = int(input("enter a number:"))
sum_of_divisors = 0

for i in range(1 , num // 2 + 1):
    if num % i == 0:
        sum_of_divisors += 1

if sum_of_divisors == num:
    print(num , "Its a perfect number")
else:
    print(num , "its not a perfect number")

