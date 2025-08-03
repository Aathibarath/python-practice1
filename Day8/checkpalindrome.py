# check for palindrome string

text = input("enter a string:")

char = text.lower()

char = char.replace(" ", "")

reverse = text[::-1]

if char == reverse:
    print("its a palindrome")

else:
    print("Its not a palindrome")

