import random


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    i = 0
    while True:
        x = throw_dice()
        y = throw_dice()
        i += 1
        if x == y:
            return i


def main():
    l = []
    for i in range(0, 100):
        l.append(throw_until_doubles())
    total = 0
    for i in l:
        total =total + i
    print("total throws: {}".format(total))
    print("avg throws: ".format(round(total/100,2)))

if __name__ == "__main__":
    main()
