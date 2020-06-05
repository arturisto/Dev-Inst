import re


def main():
    # exe1
    num_of_drivers = 30
    num_of_passangers = 90
    avaialble_cars = 100
    print("the number of available cars is: {}".format(avaialble_cars))
    print("the number of registered drivers is: {}".format(num_of_drivers))
    print("The number of empty cars today: ", avaialble_cars - num_of_drivers)

    if num_of_passangers / 4 > num_of_drivers:
        print("The number of passengers that can be transported today: ", num_of_drivers * 4)
        print("The average of passengers to put in each car: ", 4)
    else:
        print("The number of passengers that can be transported today: ", num_of_passangers)
        print("The average of passengers to put in each car: ", float(num_of_passangers / num_of_drivers))

    # exe2
    letter = input("enter one letter: ")
    lista = ['A', 'E', 'I', 'O', ' U', 'Y', 'a', 'e', 'i', 'o', ' u', 'y']
    if letter in lista:
        print("a vowel")
    else:
        print("a constant")

    # exe3
    password = input("enter a password: ")
    pattern = '[A-Z][a-z][0-9][$#@]'

    if (len(password) < 6 or len(password) > 12):
        print("the password is to long");
    else:
        result = re.match(pattern, password)
        if result:
            print("password good")
        else:
            print("password not good")

    # exe4
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
            "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip " \
            "ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
            "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia " \
            "deserunt mollit anim id est laborum. "

    lorem = lorem.replace(" ", "")
    # lorem = lorem.replace(",","")
    # lorem = lorem.replace(".", "")
    print(len(lorem))

    # exe5
    s = input("enter the longest sentance without an a: ")
    c = 'a'
    l = list(s)

    if c in l:
        print("there is an a there somewhere")
    else:
        print("your sentance is: ", len(s))


    #6
    name = input ("enter your full name: ")
    pattern = '[A-Z][a-z]'
    space = ' '

    if name.count(space) != 1:
        print("there should be 1 space")
    else:
        result = re.match(pattern, name)
        if result:
            if list(name.split(" ")[0])[0].isupper() and list(name.split(" ")[1])[0].isupper():
                print("name good")
            else:
                print("name not good")
        else:
            print("name not good")


if __name__ == "__main__":
    main()
