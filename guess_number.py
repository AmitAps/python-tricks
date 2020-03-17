
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and x (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!





x = int(input("Please think a number: "))
print('Please think of a number between 0 and {}!'.format(x))
low = 0
high = x

while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + ' ?')
    check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if check == 'c':
        print('Game over. Your secret number was:', str(guess))
        break
    elif check == 'l':
        low = guess
    elif check == 'h':
        high = guess
    else:
        print('Sorry, I did not understand your input.')
