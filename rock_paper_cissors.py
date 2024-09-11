import random
user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors"))

form = ["rock", "paper", "scissors"]
computer_chose = random.choice(form)

print(f"computer chooses {computer_chose}")

if user_choice == "0":
    print(form[0])