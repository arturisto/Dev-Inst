class Animal:
    def __init__(self, name):
        self.name_of_animal = name

    def eat(self):
        print("i am eating")

    def sleep(self):
        print("i am sleeping")

    def breat(self):
        print("i am breathing")


class Dog(Animal):
    def run(self):
        print("i am runnning")


class Bird(Animal):
    def fly(self):
        print("i am flying")


class Fish(Animal):
    def swim(self):
        print("i am swimming")


def main():

    doggy = Dog("rexxy")
    doggy.eat()
    doggy.run()

    birdy = Bird("twitty")
    birdy.fly()
    fishi= Fish("Cthulhu")
    fishi.swim()

if __name__ == "__main__":
    main()
