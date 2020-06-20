import random


class Words:

    def __init__(self, path):
        self.words = set()
        with open(path, "r") as file:
            for line in file:
                line = line.rstrip("\n")
                self.words.add(line.lower())

    def get_random_sentance(self, len):


        sample = random.sample(self.words, len)
        return sample

def main():
    words = Words("words.txt")
    print("I would like to create a random sentance for you")

    user_input = input("enter length of a sentance between 2 and 20 words longs: ")

    try:
        user_input = int(user_input)

        if 2 <= user_input <= 20:
            print(" ".join(words.get_random_sentance(user_input)))

        else:
            print("wrong length, bye bye")
    except:
        raise Exception("Not a number...")


if __name__ == "__main__":
    main()
