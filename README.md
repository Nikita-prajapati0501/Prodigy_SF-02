# Number_guessing_game
This program uses the random module to create a number guessing game based in python.

This program uses the random module to create a number guessing game in python.

The import random statement at the beginning of the code imports the built-in random module, which contains functions for generating random numbers.

The program uses two nested while loops. The outer while loop is set to True, meaning it will run indefinitely until it is explicitly broken out of using the break statement.

Inside the outer while loop, a new random number between 1 and 100 is generated using random.randint(1, 100). This number is assigned to the variable secret_num.

The variable guesses is initialized to 0 to keep track of the number of guesses made by the user.

The inner while loop is also set to True, meaning it will run indefinitely until it is explicitly broken out of using the break statement.

Inside the inner while loop, the player is prompted to guess the secret number using the input() function. The input is then converted to an integer using int(), and the result is stored in the variable guess.

The number of guesses made by the player is incremented by 1 using guesses += 1.

If the player's guess is less than secret_num, the program outputs the message "Guess higher!" using the print() function. If the player's guess is greater than secret_num, the program outputs the message "Guess lower!".

If the player's guess is equal to secret_num, the program outputs a congratulatory message that includes the number of guesses made by the player. The break statement is used to exit the inner while loop and return to the outer while loop.

After the inner while loop ends, the program prompts the user to decide whether to continue playing the game using the input() function. If the user enters "no", the program outputs a final message "Thanks for playing!" and breaks out of the outer while loop to end the program. If the user enters "yes", a new game starts with a new secret_num.
