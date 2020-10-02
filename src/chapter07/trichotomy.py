import random
rng = random.Random()
number = rng.randrange(1, 10)

guesses = 0
msg = ""

while True:
    guess = int(input(msg + "take a guess: "))
    guesses += 1
    if guess > number:
        msg += str(guess) + " is too high \n"
    elif guess < number:
        msg += str(guess) + " is too low \n"
    else:
        break

# print("Guessed in " + str(guesses) + " attempts")
input("\n\nGreat, you got it in {0} guesses and the value is {1}".format(guesses, guess))
