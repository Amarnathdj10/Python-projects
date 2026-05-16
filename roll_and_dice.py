import random
import time

def roll():
    rolled = random.randint(1,6)
    return rolled

user_total = 0
ai_total = 0

print('Welcome to the game!\n')

first = random.randint(0,1)
if first == 0:
    time.sleep(1)
    print('Your turn')
else:
    time.sleep(1)
    print("Computer's turn")
    
if first == 0:
    for i in range(10):
        if i%2==0:
            time.sleep(1)
            input("\nPress enter to roll...")
            time.sleep(1)
            print('\nUser Rolling...')
            time.sleep(1)
            rolled = roll()
            print(f"User gets {rolled}")
            user_total += rolled
            print("\nUser score:",user_total)
            print("Computer score:", ai_total)
            time.sleep(1)

        else:
            time.sleep(1)
            print("\nComputer rolling...")
            time.sleep(1)
            rolled = roll()
            print(f"Computer gets {rolled}")
            ai_total += rolled
            print("\nUser score:",user_total)
            print("Computer score:", ai_total)
            time.sleep(1)
else:
    for i in range(10):
        if i%2==0:
            time.sleep(1)
            print('Computer rolling...')
            time.sleep(1)
            rolled = roll()
            print(f"Computer gets {rolled}")
            ai_total += rolled
            print("\nUser score:",user_total)
            print("Computer score:", ai_total)
            time.sleep(1)
        else:
            time.sleep(1)
            input("\nPress enter to roll...")
            print("\nUser Rolling...")
            time.sleep(1)
            rolled = roll()
            print(f"User gets {rolled}")
            user_total += rolled
            print("\nUser score:",user_total)
            print("Computer score:", ai_total)
            time.sleep(1)

print(f"User gets {user_total}")
print(f"Computer gets {ai_total}")

if user_total > ai_total:
    print("User wins")
elif user_total < ai_total:
    print('Computer wins')
else:
    print('Draw game')
