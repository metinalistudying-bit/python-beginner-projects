import random
random_number = random.randint(1,100)
guess = int(input("There is a random number from 1 to 100 \n Try to guess it: "))

while not(guess == random_number):  
    if guess > random_number:
        guess = int(input("Decrease your number: "))
        
    elif guess < random_number:
        guess = int(input("Increase your number: "))
        
print("Congrats you found the number!")
