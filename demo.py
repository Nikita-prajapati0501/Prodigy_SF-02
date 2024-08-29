import random
while True:
    secret_num = random.randint(1, 100)
    guesses = 0

    while True:
        print(secret_num)
        guess = int(input("Guess the secret number (between 1 and 100): "))
        guesses += 1

        if guess < secret_num:
            print("Guess higher!")
        elif guess > secret_num:
            print("Guess lower!")
        else:
            print(f"Congratulations! You guessed the secret number in {guesses} attempts!")
            break

    ask_status = input('Do you want to continue playing the game? yes/no\n').lower()
    if ask_status == 'no':
        print('Thanks for playing!')
        break