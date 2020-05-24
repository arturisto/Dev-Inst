def main():
    string = input("please enter a string: ")
    print(string[0])
    print(string[len(string) - 1])

    for x in string:
        print(x)

    arr = list(string)

    arr[1], arr[3] = arr[3], arr[1]

    string = ''.join(arr)
    print(string)


if __name__ == "__main__":
    main()
