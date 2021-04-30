x = float(input("Введите значение x ="))

y = float(input("Введите значение y ="))

oper = input("Введите оператор (+, -, /, *,) =")

if oper == +:

	q = x + y

elif oper == -:

	q = x - y

elif oper == *:

	q = x * y

elif oper == /:

	q = x / y

print("Результат вычислений =",q)