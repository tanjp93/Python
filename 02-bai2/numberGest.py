import random

while True:
    top = input("Input top of range : ")
    if top.isdigit():
        top = int(top)
        print("Top of range: ", top)
        numberRandom = random.randint(0, top)
        countPlay = 1
        break
    else:
        print("Invalid input!")
while True:
    choice = input("Input your number : ")
    if choice.isdigit():
        choice=int(choice)
        if (choice > numberRandom):
            print("your number was above ")
            countPlay += 1
            continue
        if (choice < numberRandom):
            print("your number was below ")
            countPlay += 1
            continue
        if (choice == numberRandom):
            print("Choice number correctly :" + str(numberRandom))
            print("You got it in :" + str(countPlay))
            break
