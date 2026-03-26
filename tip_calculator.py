print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))
final = (total * (tip_percentage / 100 + 1)) / split
print(f"Each person should pay: ${final:.2f}")