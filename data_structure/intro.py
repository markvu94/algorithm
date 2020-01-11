class Animal:
    def __init__(self, name):
        self.name = name
        self.weight = 5
        self.skills = []

    def feed(self):
        self.weight += 1

    def teach(self, skill):
        self.skills.append(skill)


# Inheritance class
class Dog(Animal):
    def bark(self):
        print('go go')


dog = Dog('Shiba')
print(dog.weight)
dog.feed()
print(dog.weight)
dog.bark()


class Timer:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1

    def reset(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0


def get_number_of_second(hours, minutes, seconds):
    number_of_second = 3600 * hours + 60 * minutes + seconds
    return number_of_second


number_of_second = get_number_of_second(3, 5, 62)

timer = Timer()

for i in range(number_of_second):
    timer.tick()

print(timer.hours, timer.minutes, timer.seconds)

