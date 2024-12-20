# https://github.com/VasilyDrozhzhin/Module_6/blob/main/Module_6_hard.py
import math
class Figure:
	sides_count = 0

	def __init__(self, color, *sides, filled=False):
		if len(sides) != self.sides_count and __is_valid_sides(*sides):
			sides = [1] * self.sides_count
		self.__sides = list(sides)
		self.__color = list(color)
		self.filled = filled

	def get_color(self):
		return self.__color

	def __is_valid_color(self, r, g, b):
		return all(0 <= i <= 255 and isinstance(i, int) for i in [r, g, b])

	def set_color(self, r, g, b):
		if self.__is_valid_color(r, g, b):
			self.__color = [r, g, b]

	def __is_valid_sides(self, *args):
		return all(0 < i and isinstance(i, int) for i in args) and len(args) == self.sides_count

	def get_sides(self):
		return self.__sides

	def __len__(self):
		return sum(self.__sides)

	def set_sides(self, *new_sides):
		if self.__is_valid_sides(*new_sides):
			self.__sides = list(new_sides)


class Circle(Figure):
	sides_count = 1

	def __init__(self, color, round, filled=False):
		super().__init__(color, round, filled=filled)
		self.__radius = round / (2 * math.pi)

	def get_square(self):
		return math.pi * self.__radius ** 2


class Triangle(Figure):
	sides_count = 3

	def __init__(self, color, *sides, filled=False):
		super().__init__(color, *sides, filled=filled)

	def get_square(self):
		a, b, c = self.get_sides()
		p = (a + b + c) / 2
		return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
	sides_count = 12

	def __init__(self, color, line, filled=False):
		sides = [line] * self.sides_count
		super().__init__(color, *sides, filled=filled)

	def get_volume(self):
		line = self.get_sides()[0]
		return line ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216
