#24
class Counter:
    def init(self, initial_count):
        self.count = initial_count

    def increment(self):
        self.count += 1

    def get(self):
        return self.count

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

#25
class Circle:
    pi = 3.14

    def calculate_area(self, radius):
        return self.pi * (radius ** 2)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

#26
class Person:
    def init(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            self._age = 0
        else:
            self._age = value

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
#27
class Pendulum:    
    g = 10
    pi = 3.14

    @classmethod
    def calculate_period(cls, length):
        return 2 * cls.pi * (length / cls.g) ** 0.5

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
#28
class Circle:
    _pi = 3.14

    def init(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def pi(self):
        return self._pi

    def calculate_area(self):
        return self._pi * self._radius ** 2


class SemiCircle(Circle):
    def calculate_area(self):
        return super().calculate_area() / 2

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
#31
class ContextDictionary:
    def init(self):
        self.dictionary = None

    def enter(self):
        self.dictionary = {}
        return self

    def exit(self, exc_type, exc_val, exc_tb):
        self.dictionary = None

    def put(self, key, value):
        self.dictionary[key] = value

    def get(self, key):
        return self.dictionary[key]

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)