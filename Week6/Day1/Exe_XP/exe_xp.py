def main():
    # exe1

    print("hello world\nhello world\nhello world\nhello world\n")

    # exe2
    print((99 ** 3) * 8)

    # exe3
    name = "arthur"
    age = 30
    shoe_size = 43
    info = "My name is " + name + " and my shoe size is " + str(shoe_size) + " but my age is  only " + str(age)

    # exe4

    computer_brand = "omen"
    string = "my computer is " + computer_brand + " and it is a beast"
    print(string)

    # exe5

    # exe6
    int = eval(input("enter you height in inches: "))
    if int >= 35:
        print("old enough to ride a ride")
    else:
        print("to small to ride a ride")


    int = eval(input("enter a number: "))
    if int%2 == 0:
        print("even")
    else:
        print("odd")
if __name__ == "__main__":
    main()
