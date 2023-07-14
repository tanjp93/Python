import random

user_wins = 0
computer_wins = 0
tie = 0
option = ["Rock", "Paper", "scissor"]
while True:
    user_input = input("your choice or q to quit: ")
    if user_input.lower() == "q":
        break
    indexRandom = random.randint(0, 2)
    computerChoice = option[indexRandom].lower()
    if user_input.lower() == "rock" and computerChoice == "scissor":
        print("You win")
        user_wins += 1
        continue
    if user_input.lower() == "paper" and computerChoice == "rock":
        print("You win")
        user_wins += 1
        continue
    if user_input.lower() == "scissor" and computerChoice == "paper":
        print("You win")
        user_wins += 1
        continue
    if user_input.lower() == computerChoice:
        print("You tie with  computer")
        tie += 1
        continue
    print("Computer win")
    computer_wins += 1
print("Computer win :", computer_wins)
print("User win :", user_wins)
print("Tie with computer :", tie)
print("GoodBye!")
