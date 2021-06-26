#Words combination

#Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

import random

some_str = ''.join((random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(5)))
print(some_str)