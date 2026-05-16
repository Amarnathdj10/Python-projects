import random
import time

def game(choice):
    options = ["rock", "paper", "scissors"]
    ai_choice = random.choice(options)
    if ai_choice == choice:
        print('Computer: Same, redo')
        return None

    user_score = 0
    ai_score = 0

    if choice == 'rock' and ai_choice == 'scissors':
        user_score += 1
        print("Computer: scissors")
        time.sleep(1)
        print("User takes the round")
        time.sleep(1)
    elif choice == 'rock' and ai_choice == 'paper':
        ai_score += 1
        print("Computer: paper")
        time.sleep(1)
        print("Computer takes the round")
        time.sleep(1)
    elif choice == 'paper' and ai_choice == 'rock':
        user_score += 1
        print("Computer: rock")
        time.sleep(1)
        print("User takes the round")
        time.sleep(1)
    elif choice == 'paper' and ai_choice == 'scissors':
        ai_score += 1
        print("Computer: scissors")
        time.sleep(1)
        print("Computer takes the round")
        time.sleep(1)
    elif choice == 'scissors' and ai_choice == 'paper':
        user_score += 1
        print("Computer: paper")
        time.sleep(1)
        print("User takes the round")
        time.sleep(1)
    elif choice == 'scissors' and ai_choice == 'rock':
        ai_score += 1
        print("Computer: rock")
        time.sleep(1)
        print("Computer takes the round")
        time.sleep(1)
    else:
        print('Invalid input')
        return None

    return user_score, ai_score


total_user = 0
total_comp = 0
print("*-----WELCOME TO THE GAME-----*")
while True:
    user_choice = input("User: ").lower()
    output = game(user_choice)
    if output is None:
        continue

    total_user += output[0]
    total_comp += output[1]

    print("Current user score: ", total_user)
    print("Current computer score: ", total_comp)

    if total_comp == 3 or total_user == 3:
        break

if total_user > total_comp:
    print("User wins")
elif total_user < total_comp:
    print('Computer wins')
else:
    print('Draw game')