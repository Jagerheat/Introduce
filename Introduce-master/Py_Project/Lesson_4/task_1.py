#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
#The result should be sent back to the user via a print statement.

import random
taken = 0
number = random.randint(1, 10)
print('And, number between 1 and 10.')
while taken < 6:
    print('Take a guess.') 
    digit = input()
    digit = int(digit)
    taken = taken + 1
    if digit < number:
        print('Your guess is too low.') 
    elif digit > number:
        print('Your guess is too high.')
    elif digit == number:
        break
  