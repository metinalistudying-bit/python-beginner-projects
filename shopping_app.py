item = input("Hi sir What do tou want to buy: ")
price = float(input(f"What is the price of 1 {item}: "))
quantity = int(input(f"How many {item}s are you going to buy: "))
final_price = price * quantity
print(f"""
Receipt
-------------------
Item: {item}
Quantity: {quantity}
Unit Price: ${price:.2f}
-------------------
Total: ${final_price:.2f}
""")
