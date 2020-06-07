class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog:
    species = "mammal"

    def __init__(self, nameDog, heigtDog):
        self.name = nameDog
        self.height = heigtDog

    def talk(self):
        print("Wouaf")

    def jump(self):
        print(self.height * 2)


class Zoo:

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.pen = {}

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            print(f"bye bye {animal_sold}")
            self.animals.remove(animal_sold)
        else:
            print("you cannot sell what is isn't yours")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        set_of_letters = list(set([x[0] for x in self.animals]))

        for x in range(0,len(set_of_letters)):
            list_of_animals = []
            for y in sorted_animals:
                if y[0] == set_of_letters[x]:
                    list_of_animals.append(y)
            self.pen[x+1] = list_of_animals

    def get_pen(self):
        print(self.pen)

def oldest_cat(list_of_cats):
    max = 0
    cat = ""
    for x in list_of_cats:
        if x.age > max:
            cat = x
            max = x.age
    print(cat.name)


def main():
    # exe1
    list_of_cats = []
    list_of_cats.append(Cat("Grizzabella", 60))
    list_of_cats.append(Cat("Rum Tum Tager", 15))
    list_of_cats.append(Cat("Macavity", 25))
    oldest_cat(list_of_cats)

    # exe2
    davids_dog = Dog("Rex", 50)
    davids_dog.jump()
    davids_dog.talk()
    sarahs_dog = Dog("Teacup", 20)
    sarahs_dog.talk()
    sarahs_dog.jump()
    Dog.winner = False

    if davids_dog.height > sarahs_dog.height:
        davids_dog.winner = True

    else:
        sarahs_dog.winner = False

    print("*"*32)
    ramatGanSafari = Zoo("safari")
    ramatGanSafari.add_animal("pikachu")
    ramatGanSafari.add_animal("pichu")
    ramatGanSafari.add_animal("dragonight")
    ramatGanSafari.add_animal("drattini")
    ramatGanSafari.add_animal("mew")
    ramatGanSafari.add_animal("mewtwo")
    ramatGanSafari.add_animal("charizard")
    ramatGanSafari.get_animals()
    ramatGanSafari.sell_animals("mew")
    ramatGanSafari.sell_animals("ratata")
    ramatGanSafari.sort_animals()
    ramatGanSafari.get_pen()
if __name__ == "__main__":
    main()
