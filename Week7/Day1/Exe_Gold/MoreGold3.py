import random
from googletrans import Translator

from functools import reduce


def do_sum(x1, x2):
    return x1 + x2


def main():
    # exe1
    i = random.randint(5, 10)
    l = []
    for x in range(0, i):
        l.append(random.randint(10, 20))
    print(l)
    l1 = [x for x in l if x % 3 == 0]
    print(l1)
    l1 = [x for x in l if x % len(l) == 0]
    print(l1)
    l1 = [x for x in l if x > 12]
    print(l1)
    l1 = [x * x for x in l]
    print(l1)
    l1 = list(set(l))
    print(l1)

    # exe2

    users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}
    for index, x in enumerate(users):
        dict1[x] = index
        dict2[index] = x
    for index, x in enumerate(sorted(users)):
        dict3[x] = index

    translator = Translator()
    for x in french_words:
        dict4[x] = translator.translate(x, src="fr", dest='en').text
    print(dict1)
    print(dict2)
    print(dict3)
    print(dict4)

    dict1.clear()
    for index, x in enumerate(users):
        dict1[x] = index
        dict2[index] = x

    # exe3

    # 1 Capitalize all of the pet names and print the list
    my_pets = ['sisi', 'bibi', 'titi', 'carla']

    for index, x in enumerate(my_pets):
        my_pets[index] = x.title()
    print(my_pets)
    # 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
    my_strings = ['a', 'b', 'c', 'd', 'e']
    my_numbers = [5, 4, 3, 2, 1]
    my_numbers.reverse()
    zip = []
    for index, x in enumerate(my_strings):
        zip.append((x, my_numbers[index]))
    print(zip)

    # 3 Filter the scores that pass over 50%
    scores = [73, 20, 65, 19, 76, 100, 88]
    high_scores = [x for x in scores if x >= 80]

    print(high_scores)
    # 4 Bonus : Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

    x = reduce(do_sum, scores) + reduce(do_sum, my_numbers)
    print(x)


if __name__ == "__main__":
    main()
