def Max_Three(a,b,c):
    if a >= b and a>= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
result = Max_Three(64,87,65)
print(result)