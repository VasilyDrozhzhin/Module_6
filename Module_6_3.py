import random


class Animal:
	live = True
	sound = None
	_DEGREE_OF_DANGER = 0

	def __init__(self, speed):
		self._cords = [0, 0, 0]
		self.speed = speed

	def move(self, dx, dy, dz):
		new_z = self._cords[2] + dz * self.speed
		if new_z < 0:
			print("It's too deep, I can't dive :(")
		else:
			self._cords[0] += dx * self.speed
			self._cords[1] += dy * self.speed
			self._cords[2] = new_z

	def get_cords(self):
		print(f'x: {self._cords[0]}, y: {self._cords[1]}, z: {self._cords[2]}')

	def attack(self):
		if self._DEGREE_OF_DANGER < 5:
			print("Sorry, i'm peaceful :)")
		elif self._DEGREE_OF_DANGER > 4:
			print("Be careful, i'm attacking you 0_0")

	def speak(self):
		print(self.sound)


class Bird(Animal):
	beak = True

	def lay_eggs(self):
		x = random.randint(1, 4)
		print(f"Here are(is) {x} eggs for you")


class AquaticAnimal(Animal):
	_DEGREE_OF_DANGER = 3

	def dive_in(self, dz):
		self._cords[2] -= abs(dz) / 2 * self.speed


class PoisonousAnimal(Animal):
	_DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
	def __init__(self, speed):
		super().__init__(speed)
		self.sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
