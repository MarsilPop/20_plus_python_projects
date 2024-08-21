# Python card number validator

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# STEP 1 - Remove any "-" or " "
card_number = input("Enter a credit card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# STEP 2 - Add all digits in the odd places from right to left
for x in card_number[::2]:
    sum_odd_digits += int(x)

# STEP 3 - Double every second digit from right to left.
#          (If result is a two digit number, add the
#           two-digit number together to get a single digit.)
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# STEP 4 - Sum the total of steps 2 & 3
total = sum_odd_digits + sum_even_digits

# STEP 5 - If the sum is divisible by 10, the credit card # is valid
if total % 10 == 0:
    print("CREDIT CARD NUMBER IS VALID.")
else:
    print("CREDIT CARD NUMBER IS INVALID.")