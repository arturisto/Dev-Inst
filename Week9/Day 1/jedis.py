import random

def harmonic_mean(first_param,second_param):
    return 1/((1/first_param+1/second_param)/2)

class foreceWielder:

    def __init__(self,name_input):
        self.name = name_input
        self.power = random.randint(1,15)
        self.wisdom = random.randint(1,15)

    def train(self):
        pass
    def is_jedi(self):
        pass
    def fight_method (self, other):

        first_fighter = harmonic_mean(self.power, self.wisdom)
        second_fighter = harmonic_mean(other.power, other.wisdom)

        if first_fighter > second_fighter:
            return 1
        elif first_fighter < second_fighter:
            return 2
        else:
            return 0

class Jedi(foreceWielder):

    def __init__(self,name):
        super().__init__(name)

        if self.wisdom > self.power:
            self.lightsaber = "green"
        elif self.wisdom < self.power:
            self.lightsaber = "red"
        else:
            self.lightsaber = "violet"

        self.wisdom+=10

    def train(self):
        self.wisdom += random.randint(10,20)
        self.power += random.randint(5,15)
    def is_jedi(self):
        return True


class Sith(foreceWielder):

    def __init__(self, name):
        super().__init__("darth "+name)
        self.lightsaber = "red"
        self.power += 10

    def train(self):
        self.power += random.randint(10, 20)
        self.wisdom += random.randint(5, 15)

    def is_jedi(self):
        return False



