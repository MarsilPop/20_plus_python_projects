# FOR LOOPS

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

# NESTED LOOPS

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter the symbol to use: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end=" ")
#     print()

# 2D COLLECTIONS

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "beef"]

# print(groceries[0][1]) # orange

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "beef"]]

for stuff in groceries:
    for food in stuff:
        print(food, end=" ")
    print()

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for button in row:
        print(button, end=" ")
    print()
