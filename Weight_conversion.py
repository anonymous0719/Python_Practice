#Python Program to convert weights in Pounds or Kilos
Weight = int(input("Enter the Weight : "))
unit = input("Pounds(L) or KGs(K): ")
if unit.upper() == "L":
    converted = Weight * 0.45
    print(f"You are {converted} Kilos")
else:
    converted = Weight / 0.45
    print(f"You are {converted} Pounds")


