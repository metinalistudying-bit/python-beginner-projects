import random

try:
    user_rock_paper_scissor = int(input("What you choosing? Type 1 for Rock, 2 for Paper or 3 For Scissor\n"))
except ValueError:
    print("Invalid choice! Please type a number 1, 2 or 3")
    exit()

computer_choice = random.randint(1, 3)

if user_rock_paper_scissor == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif user_rock_paper_scissor == 2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif user_rock_paper_scissor == 3:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Invalid choice! Please type 1, 2 or 3")
    exit()

if computer_choice == 1:
    print("""
Computer choice:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_choice == 2:
    print("""
Computer choice:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif computer_choice == 3:
    print("""
Computer choice:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if user_rock_paper_scissor == computer_choice:
    print("Draw")
elif user_rock_paper_scissor == 1 and computer_choice == 3:
    print("You Win")
elif user_rock_paper_scissor == 1 and computer_choice == 2:
    print("You Lose")
elif user_rock_paper_scissor == 2 and computer_choice == 1:
    print("You Win")
elif user_rock_paper_scissor == 2 and computer_choice == 3:
    print("You Lose")
elif user_rock_paper_scissor == 3 and computer_choice == 1:
    print("You Lose")
elif user_rock_paper_scissor == 3 and computer_choice == 2:
    print("You Win")