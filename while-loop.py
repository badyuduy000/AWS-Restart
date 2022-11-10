print("Welcome to guess the number")
print("The rules are simple I will think of a number and you will try to guess it.")
import random
number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    print(number)
    guess = input("Guess a number between 1 and 10 ")
    if int(guess) == number:
        print("You guess {}. That is correct, you win!".format(guess))
        isGuessRight = True 
    else:
        print("You guess {}. Sorry the number is incorrect.".format(guess))
print("while loop exit")