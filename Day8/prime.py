#print prime number in a range

num1 = int(input("enter first number:"))
num2 = int(input("enter 2nd number:"))

i = 0 

for i in range (num1 , num2):
    if i %2 == 0:
        print("Its not prime")
    elif i == int(i**0.5 + 1):
        print("Its a prime")
