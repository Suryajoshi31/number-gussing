import random

target = random.randint(1, 100)

while True:
    user_input = int(input("Guess a number between 1 and 100 or quit (Q): "))
    
    if user_input.lower() == "q":
        break

    try:
        user_choice = int(user_input)
        
        if user_choice == target:
            print("Congratulations! You guessed the number correctly.")
            break
        elif user_choice < target:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100 or 'Q' to quit.")

print("---GAME OVER---")
