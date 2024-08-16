weight = float(input("Enter the weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"The weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"The weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid.")

