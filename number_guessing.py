import random

def int_check(n: any) -> int:
    '''
    This function checks if the input is an integer.
    If not, it prompts the user to enter a valid integer.
    '''
    try:
        return int(n)
    except ValueError:
        return int_check(input("Please enter a valid integer:"))

def main():
    top_range = int_check(input("Enter the top range: "))
    r= random.randrange(top_range)
    guess = 0

    while True:
        guess += 1
        guess = int_check(input("Enter your guess: "))
        if guess == r:
            print("You guessed it!")
            break
        elif guess < r:
            print("Too low!")
        else:
            print("Too high!")
    
    print("You guessed it in", guess, "guesses!")

if __name__ == "__main__":
    main()