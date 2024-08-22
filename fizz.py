# Fizz Buzz

# for number in range(1, 31):
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Fizz")
#     elif number % 3 == 0:
#         print("Buzz")
#     else:
#         print(number)

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()