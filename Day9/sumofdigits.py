def sum_of_digits(n):
    total = 0
    for digits in str(n):
        total += int(digits)
    return total
print(sum_of_digits(584654))