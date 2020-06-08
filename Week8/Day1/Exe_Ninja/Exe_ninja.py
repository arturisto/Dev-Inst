import inflect
class MenuManager:

    def __init__(self):
        self.menu = {
            "Soup": [10, "B", False],
            "Hamburger": [15, "A", True],
            "Salad": [18, "A", False],
            "French Fries": [5, "c", False],
            "Beef Bourgignon ": [25, "B", True],
        }

    def add_item(self, name, price, spice, gluten):

        self.menu[name] = [price, spice, gluten]

    def update_item(self, name, price, spice, gluten):
        if name in self.menu:
            self.menu[name] = [price, spice, gluten]
        else:
            print(f"{name}is not in the menu")

    def remove_item(self, name):
        if name in self.menu:
            del self.menu[name]
            print(self.menu)
        else:
            print(f"{name}is not in the menu")


class Farm:

    def __init__(self, name):
        self.farm_name = name
        self.animals = {}

    def add_animal(self, name, amount=1):
        if name in self.animals:
            self.animals[name] += amount
        else:
            self.animals[name] = amount

    def get_info(self):
        string_length = len(self.farm_name) + 8
        print(f"{self.farm_name}'s Farm")
        p = inflect.engine()
        for animal in self.animals:
            print(f"{p.plural(animal)}" + " " * (string_length - len(p.plural(animal))) + ": " + f"{self.animals[animal]}")
        print(" " * (string_length - 10) + "E-I-E-I-O!")

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        list_of_animals = self.get_animal_types()
        p = inflect.engine()
        for i,x in enumerate(list_of_animals):
            list_of_animals[i] = p.plural(x)
        return f"{self.farm_name}'s farm has {', '.join(list_of_animals)}"


def main():
    # exe 1
    menu = MenuManager()

    menu.add_item("pizza", 11, "B", True)
    menu.add_item("shushi", 33, "C", False)
    menu.update_item("Hamburger", 20, "A", True)
    menu.remove_item("eggs")
    menu.remove_item("Salad")

    # exe 2
    macdonald = Farm("McDonald")
    macdonald.add_animal("cow", 5)
    macdonald.add_animal("sheep")
    macdonald.add_animal("sheep")
    macdonald.add_animal("goat", 12)

    macdonald.get_info()

    print(macdonald.get_animal_types())

    print(macdonald.get_short_info())

if __name__ == "__main__":
    main()
