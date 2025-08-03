#count the number of string vowels
text = input("Enter a string:").lower()
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels in a string is:" , count)


