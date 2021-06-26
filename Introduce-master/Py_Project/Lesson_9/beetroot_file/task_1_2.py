
file = open('myfile.txt')
#file = open('myfile.json')
lines = file.readlines()
for line in lines:
	print('\n', line, '\n')

