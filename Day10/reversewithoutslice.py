#reverse a string without using slicing

text = input("enter a string:")
reversed_str = ""

for i in range(len(text) -1, -1, -1):
    reversed_str += text[i]

print("Reversed string is:", reversed_str)