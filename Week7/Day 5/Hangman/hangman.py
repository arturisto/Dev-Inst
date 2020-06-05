import random
def main():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
                 'credit card', 'rush', 'south']
    word = random.choice(wordslist)
    letters = list("abcdefghijklmnopqrstuvwxyz")
    ### YOUR CODE STARTS FROM HERE ###
    l_word = list(word)
    encrypted_word = []
    lives = 10;
    print(word)
    for letter in l_word:
        if letter != " ":
            encrypted_word.append("*")
        else:
            encrypted_word.append(" ")

    while lives > 0:
        print("".join(encrypted_word))
        print(f"number of lives is: {lives}")
        print("pick next letter for your list:")
        print(" ".join(letters))
        user_input = input(">> ")
        if  user_input not in letters:
            print("wrong input, try again")
            continue
        if user_input in l_word:
            for x,y in enumerate(l_word):
                if y == user_input:
                    encrypted_word[x] = user_input
        else:
            lives -= 1
            print("wrong choice, you lost a life")
        letters.remove( user_input)
        if lives < 1:
            print(f"tough luck, the word was: {word}")
            return;
        if "*" not in encrypted_word:
            print("you won!!! congratzzzzzzzz")


if __name__ == "__main__":
    main()
