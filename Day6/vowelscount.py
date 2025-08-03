def count_vowels(text):
    text = text.lower()
    count = 0

    for char in text:
         if char in 'aeiou':
          count += 1
    return count

result = count_vowels("Welcome to Zoho")
print(result)


    