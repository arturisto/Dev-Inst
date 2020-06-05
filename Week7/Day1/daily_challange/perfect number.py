def main():
    try:
        user_input = int(input("enter a positive number to be checked as perfect\n>>"))
    except:
        print("not a number, goodbye")
        return

    if user_input < 1:
        print("not a positive number, goodbye")
        return
    divisors = []
    for x in range(1,user_input):
        if user_input % x == 0:
            divisors.append(x)
    if sum(divisors) == user_input:
        print(f"{user_input} is perfect")
    else:
        print(f"{user_input} is not perfect")


if __name__ == "__main__":
    main()
