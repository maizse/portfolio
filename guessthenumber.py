import random
n = random.randint(1, 99)
print("Guess the number from 1 to 99")

def printThis():

    while True:
        try:
            guessNum = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            break

    if guessNum < 1 or guessNum > 99:
        print("Number is not in range. Guess again.")
        printThis()

    elif guessNum > n:
        print("Your guess is higher.")
        printThis()

    elif guessNum < n:
        print("Your guess is lower.")
        printThis()

    elif guessNum == n:
        print("Correct!")
        

printThis()
