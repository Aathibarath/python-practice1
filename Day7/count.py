#count character in a string

s = "placement preparation"

s = s.replace(" ","")

char_count = {}

for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

for key in char_count:
    print(key , ":" , char_count[key])