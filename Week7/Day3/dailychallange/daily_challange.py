import random


def main():
    l_case = "abcdefghijklmnopqrstuvwxyz"
    u_case = l_case.upper()
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    strings = ["7 3", "Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"]

    max_string = 0
    msg = ""
    for x in strings:
        if len(x) > max_string:
            max_string = len(x)

    for i in range(0, max_string):
        for x in strings:
            if x[i] in l_case or x[i] in u_case or x[i] == " ":
                msg += x[i]
            else:
                msg += " "

    print(msg)

    list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
    target_number = 3728
    k = 0;
    list_of_numbers.sort()
    for i in range(list_of_numbers[0], target_number + 1):
        for j in range(i, target_number + 1):
            if i + j == target_number:
                k += 1
                print("{}. {} + {} = {}".format(k, i, j, target_number))
                break;
            if i + j > target_number:
                break;


if __name__ == "__main__":
    main()
