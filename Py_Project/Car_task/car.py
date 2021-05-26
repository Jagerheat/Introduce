# Средняя скорость 70 км/час
# В городе максимальная 50 км/час
# Траса 90 км/час
# Vср = 90 + 50 / 2 = 70

class Car:

	def __init__(self, Varg: float, S: float):
		self.Varg = 70
		self.S = 500

	def time(self):
		t = self.S / self.Varg + 2
		print(t)


r = Car('', '')
r.time()

# S = 500 км/час, t = S / Vcp
# При расстоянии 500 км/час, будет 2 остановки по часу

