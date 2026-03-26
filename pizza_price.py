price = 0
print("Welcome to Pizza Deliveries!")

size = input("What size pizza you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? (Y/N): ").upper()
extra_cheese = input("Do you want extra cheese? (Y/N): ").upper()

if size == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price += 20
    if pepperoni == "Y":
        price += 3
elif size == "L":
    price += 25
    if pepperoni == "Y":
        price += 3
else:
    print("Invalid size! Please choose S, M or L")
    exit()

if extra_cheese == "Y":
    price += 1

print(f"Your total is ${price}")