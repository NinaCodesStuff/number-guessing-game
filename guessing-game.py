import random

high_num = 100
low_num = 1
random_num = random.randint(low_num, high_num)
guesses = 0
is_running = True

print()
print("------------------------WELCOME------------------------")
print()
while is_running:
    guess = input(f"Guess a number between {low_num} and {high_num}: ")
    print()
    if guess.isdigit():
        guess = int(guess)
        if guess < low_num or guess > high_num:
            print("Your guess is not within range!")
            guesses += 1
            guess = input(f"Guess a number between {low_num} and {high_num}: ")
            print()
        elif guess < random_num:
            print("Your guess is too low.")
            guesses += 1
        elif guess > random_num:
            print("Your guess is too high.")
            guesses += 1
        elif guess == random_num:
            print("-----------------------------------------------------")
            print(f"The number was {random_num}! You guessed correctly!")
            guesses += 1
            print(f"It took you {guesses} guesses!")
            print()
            print("Thanks for playing!")
            break

    else:
        print("Your guess is invalid.")

