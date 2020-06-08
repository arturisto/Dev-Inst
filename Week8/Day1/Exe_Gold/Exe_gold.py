import math
import random


class Circle:

    def __init__(self, r=1):
        self.radious = r

    def permieter(self):
        return self.radious * math.pi * 2

    def area(self):
        return math.sqrt(self.radious) * math.pi

    def definition(self):
        print("A circle is all of the points in a given range from a single point in space")


class myList:
    def __init__(self, l):
        self.lst = l

    def reverse(self):
        rvrs = self.lst.copy()
        rvrs.reverse()
        return rvrs

    def sorted_self(self):
        return sorted(self.lst)

    def gen_new_list(self):
        new_list = []
        for x in range(len(self.lst)):
            new_list.append(random.randint(1, len(self.lst)))
        return new_list


class QuantumParticle:

    def __init__(self):
        self.position = random.randint(1, 10000)
        self.momentum = random.random()
        if random.random() >= 0.5:
            self.spin = 0.5
        else:
            self.spin = -0.5
        self.entangle = None

    def __repr__(self):
        print(f"Quantum particle in position: {self.position}, momentum of {self.momentum}, spin of {self.spin} and "
              f"is not entangled")

    @staticmethod
    def quantum_interferences(self):
        self.position = random.randint(1, 10000)
        self.momentum = random.random()
        print("Quantum Interferences!!")

    def entanglement(self, qp):
        if self.entangle is None:
            self.entangle = qp
            qp.entangle = self
            qp.position = -0.5
            print("Spooky Action at a Distance !!")


def main():
    # exe 1

    circle = Circle(10)
    print(circle.permieter())
    print(circle.area())
    circle.definition()

    # exe2

    l = [1, 4, 2, 7, 2, 55, 2, -4, 3, 77, -6, 11, -664, 34]
    if len(l) > 0:
        my_list = myList(l)
        print(my_list.reverse())
        print(my_list.sorted_self())
        print(my_list.gen_new_list())

    # exe 3
    qp = QuantumParticle()

    qp.__repr__()

    qp2 = QuantumParticle()
    qp2.entanglement(qp)


if __name__ == "__main__":
    main()
