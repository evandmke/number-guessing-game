import random

print("Welcome to Number Guessing Game")

while True:
    diff = input("Which difficulty would you like to play? Easy(1-10)/ Medium(1-100)/ Hard(1-500): ").lower()
    if diff == "easy":
        low, high = 1, 10
    elif diff == "medium":
        low, high = 1, 100
    elif diff == "hard":
        low, high = 1, 500
    else:
        print("Invalid difficulty")
        continue

    n = random.randint(low, high)

    while True:
        try:
            num = int(input("Enter number: "))
        except ValueError:
            print("Invalid input")
            continue

        if num < low or num > high:
            print(f"Number must choose a number between {low} and {high}")
            continue
        elif low <= num <= high:
            if num == n:
                print("You guessed the number correctly")

            elif n < num:
                print("You guessed the number incorrectly")
                print("Try lower")
                continue
            elif n > num:
                print("You guessed the number incorrectly")
                print("Try higher")
                continue

            again = input("Do you want to play again? (y/n): ")
            if again == "y":
                 continue
            elif again == "n":
                 print("Thank you for playing")
                 exit()
            else:
                 print("Invalid input")
                 exit()
