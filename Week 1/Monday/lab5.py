number_to_guess = int(input("Enter the secret number: "))
tries = 0

print("Guess the number broo")

guess = int(input("Take your first guess!\n"))
print("")

while guess != number_to_guess and tries < 2:
    tries += 1
    if guess < number_to_guess:
        print("Too low! Try again bro.")
    else:
        print("It's still high! Try again bro.")
    print(f"Try: {tries}\n")

    guess = int(input(f"Take your {tries+1}nd guess!\n"))


if guess == number_to_guess:
    print(f"Congrats! You guessed the correct number!")

else:
    print(f"You lost! The number was {number_to_guess}")
