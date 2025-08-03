a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
if a >= b and a >= c:
    print(a, "is largest number")
elif b >= c and b >= a:
    print(b, "is largest number")

else:
    print(c, "is largest number")