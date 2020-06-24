import random
import string
def randomize(number):

    if number == random.randint(1,100):
        print("wow, success")


def main():

    user_input = int(input("enter a number 1 to 100: "))

    randomize(user_input)

    print("".join((random.choices(string.ascii_letters, k=5))))

if __name__ == "__main__":
    main()