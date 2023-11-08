import random  # Import the 'random' module to generate random numbers


# Generate a random number within the specified range
random_number = random.randint(0, 100)  # Generate a random number between 0 and 100
guesses = 0  # Initialize the number of guesses to 0

# Start the guessing loop
while True: 
    user_guess = input("Make a guess: ")  # Prompt the user to make a guess

    # Check if the user's input is a valid integer
    if user_guess.isdigit():  # Check if the input consists of digits only

        guesses += 1  # Increment the number of guesses by 1
        user_guess = int(user_guess)  # Convert the input to an integer

        if user_guess == random_number:  # Check if the user's guess is correct
            print("You got it!")  # Congratulate the user for guessing correctly
            break  # Exit the loop

        elif user_guess > random_number:  # Check if the user's guess is too high
            print("You guessed too high!")  # Inform the user that their guess is too high
        
        else:
            print("You guessed too low!")  # Inform the user that their guess is too low
    else:
        print('Please type a valid number.')  # Ask the user for a valid input

# Display the results
if guesses == 1:  # Check if the user guessed correctly on the first attempt
    print("You got it in the first attempt.")  # Display a message for a correct first guess
elif guesses == 2:  # Check if the user guessed correctly on the second attempt
    print("You got it in the second attempt.")  # Display a message for a correct second guess
else:
    print("You got it in", guesses, "guesses.")  # Display the number of guesses needed for the correct answer
