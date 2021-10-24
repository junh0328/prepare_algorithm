class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' cannot speak.')

    def move(self):
        print(self.name + ' cannot move.')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(self.name + ' moves like a jagger')


class Retriever(Dog):
    def __inti__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is smart enough to speak')


dog = Dog('Nancy')
dog.speak()
dog.move()

super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()

# Nancy cannot speak. >> 안건들여도 됨
# Nancy cannot move.
# Michael cannot speak.
# Michael cannot move.

# Nancy cannot speak.
# Nancy moves like a jagger.
# Michael is smart enough to speak.
# Michael moves like a jagger.
