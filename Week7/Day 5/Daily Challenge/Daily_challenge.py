import random


def main():
    user_input = input("enter a number: ")

    #check input

    for x in user_input:
        if x.isdigit() != True:
            print("not good input")
            return;
    user_input=int(user_input)
    converted = []
    output=0
    # convert to bit
    print(user_input)
    while user_input > 0:
        if user_input % 2 == 0:
            converted.append(0)
            user_input = user_input / 2
        else:
            converted.append(1)
            user_input = (user_input - 1) / 2

    converted

    #make the 32 bit list
    convereted_32bit= [0]*32
    for index,x in enumerate(converted):
        convereted_32bit[index]=x
    #Convert back to number
    for x in convereted_32bit:
        output = output*2 +x
    print(f"output: {output}")



if __name__ == "__main__":
    main()
