def sum_digits_string(str1):
    sum_digit = 0
    for i in str1:
        if i.isdigit() == True:
            z = int(i)
            sum_digit = sum_digit + z
    return sum_digit
print(sum_digits_string(input()))