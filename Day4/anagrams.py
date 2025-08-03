str1 = input("enter a first string:")
str2 = input("enter a second string:")

if sorted (str1) == sorted (str2):
    print("Its an anagram")
else:
    print("Its not an anagram")