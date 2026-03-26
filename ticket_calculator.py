height = int(input("Your height is: "))
bill = 0

if height >= 120:
    age = int(input("Your age? "))
    if age <= 12:
        print("Child ticket - pay 5$")
        bill = 5
    elif age <= 18:
        print("Youth ticket - pay 7$")
        bill = 7
    else:
        print("Adult ticket - pay 12$")
        bill = 12

    wants_photo = input("You want a photo? (y/n) ")
    if wants_photo.lower() == "y":
        bill += 3

    print(f"Your total is {bill}$")

else:
    print("Sorry you must be 120cm or taller to ride")