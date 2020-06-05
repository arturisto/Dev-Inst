def main():

    user_input = (input("enter a sentence without special characters\n>>"))

    words = user_input.split(" ")

    words.reverse()

    print(words)


if __name__ == "__main__":
    main()
