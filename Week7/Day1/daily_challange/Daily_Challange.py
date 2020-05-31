def encrypt(shift, message, l):
    message.lower()
    answer = ""

    for x in message:
        if x in l:
            i = (l.index(x) + shift) % 26
            answer += l[i]
        else:
            answer += x

    print(answer)


def decrypt(shift, message, l):
    message.lower()
    answer = ""

    for x in message:
        if x in l:
            i = (l.index(x) - shift) % 26
            answer += l[i]
        else:
            answer += x

    print(answer)


def main():
    y = int(input("For encryption press 1, for decryption press 2: "))
    msg = input("enter your message: ")
    shift = int(input("enter the shift: "))

    l = list("abcdefghijklmnopqrstuvwxyz")
    print(l)
    if y == 1:
        encrypt(shift, msg, l)
    else:
        decrypt(shift, msg, l)


if __name__ == "__main__":
    main()
