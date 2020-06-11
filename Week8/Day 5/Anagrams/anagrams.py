from anagram_checker import AnagramChecker

def check_input(user_input):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for charecter in user_input:
        if charecter.lower() not in alphabet:
            return False
    return True


def main():
    anagram = AnagramChecker()


    while True:
        try:
            user_input = int(input("Do you want to: \n1 - FInd anagrams\n2 - Exit\n>>"))
        except:
            print("wrong input")
            continue

        if user_input >2:
            print("wrong input")
            continue
        else:
            if user_input == 1:
                word_input = input("enter a single english word with at least two letters: ")

                if check_input(word_input):
                    if anagram.is_valid_word(word_input.upper()):
                        print(anagram.get_anagrams(word_input.upper()))
                    else:
                        print("sorry, the word is not in my dictionary")
                else:
                    print("wrong input")
                    continue
            else:
                print(("bye bye"))
                return


if __name__ == "__main__":
    main()
