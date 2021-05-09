import random

while True:
	num1 = random.randint(0, 100)
	num2 = random.randint(0, 100)
	answer = input(f'Insert answer {num1} + {num2} :')
	if answer == str(num1 + num2):
		print('Great, catch your cookie')
		break
	else:
		print('Try again') 