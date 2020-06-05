import random
def main():

    #exe1+2+3
    birthdays={
       "arthur":"1989/06/27",
        "Yael":"1993/04/09",
        "Mom":"1963/05/08",
        "Dad":"1960/06/28",
        "brother":"1987/11/26"
    }
    user_name = input("enter a name of a person to be added to the dictionary\n>> ")
    if user_name not in birthdays:
        birthdays[user_name]=input("enter that person's birthday in YYYY/MM/DD format \n>>")
    else:
        print(f"{user_name} is in the dictionary\n his birthdays is {birthdays[user_name]}")

    user_input=input("Whose birthday you want to see:\n"
                     ">> ")
    if user_input in birthdays:
        print(f"{user_input}'s birthday is on {birthdays[user_input]}")
    else:
        print(f"{user_input} is not in the dictionary")

    #exe4+5
    inputs = [random.randint(-100,100) for _ in range(random.randint(50,100))]
    # for x in range(3):
    #     inputs.append(eval(input("enter a number between -100 and 100\n>>")))
    print("*"*23)

    print("all of the numbers in one line:")
    print(*inputs, sep=", ")
    print("the sum of all the numbers is:")
    print(sum(inputs))
    print("A list containing the first and the last number only:")
    print(f"{inputs[0]}, {inputs[-1]}")
    print("The numbers without any duplicates (Test this by typing in some duplicates):")
    print(set(inputs))
    print("A list of all the numbers greater than 50:")
    print([x for x in inputs if x>=50])
    print("A list of all the numbers smaller than 10:")
    print([x for x in inputs if x <= 10])
    print("A list of all of the numbers squared:")
    print([x*x for x in inputs])
    print("The average of all the numbers:")
    print(sum(inputs)/len(inputs))
    print("The largest number:")
    print(max(inputs))
    print("The smallest number:")
    print(min(inputs))

if __name__ == "__main__":
    main()
