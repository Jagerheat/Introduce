some_stl = input("Get string:")
if len(some_stl) < 2:
 	print(None)
else:
	print("Take string:", (some_stl[0:2] + some_stl[-2:])