def main():

    #exe2
    x = input("enter a digit: ")
    y = input("enter a second digit: ")
    if x >y:
        print("hello world")

    #exe3
    x = eval(input("enter a number between 1 and 12: "))

    if x < 3:
        print("Winter runs from December (12) to February (2)")
    elif x< 6:
        print("Spring runs from March (3) to May (5)")
    elif x< 9:
        print("Summer runs from June (6) to August (8)")
    elif x<12:
        print("Autumn runs from September (9) to November (11)")
    else:
        print("Winter runs from December (12) to February (2)")

if __name__ == "__main__":
    main()
