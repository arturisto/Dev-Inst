class Palindrom():

    def __init__(self,word_input):
        self.word = word_input

    def is_palindrome(self):

        for i, letter in enumerate(self.word):
            if letter != self.word[-i-1]:
                return False
        return True

def main():


      while True:
          user_input = input("enter a word to be checked as palindrom \n>> ")

          pal = Palindrom(user_input)

          if pal.is_palindrome():
              print(f"{user_input} is palindrom")
          else:
              print(f"{user_input} is not a palindrom")
if __name__ == "__main__":
    main()
