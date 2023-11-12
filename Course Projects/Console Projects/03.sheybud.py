import random

items = ["wah", "kisi", "dhaban"]
current_player = "User 1"

while True:

    print(f"It's {current_player} Turn to Hide.")

    for i in range(3):
        # pick random choice from the list
        selected_item = random.choice(items)
        print(selected_item)
        # Opponent guesses the item 
        guess = input(f"Enter your guess: ").lower().strip()

        if guess  == selected_item:
            current_player = 'User 2' if current_player == 'User 1' else 'User 1'
            break
        else:
            print("Incorrect guess. Try again!")

            if i == 2:
                print(f"Congratulations! {current_player} has won this round!")
                exit()

