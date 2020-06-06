import math


def find_max(nums):
    max = 0
    for x in nums:
        if x > max:
            max = x
    print(f"maximun number is {max}")


def factorial(x):
    num = 1
    for y in range(1, x + 1):
        num = num * y
    print(f"the factorial is {num}")


def my_sum(nums):
    sum = 0
    for x in nums:
        sum += x
    print(f"the sum is {sum}")


def list_count(m_list):
    i = 0
    for x in m_list:
        i += 1
    print(f"number of items in list is {i}")


def norm(nums):
    squares = 0
    for x in nums:
        squares = x * x
    print(f"norm of ilist is {math.sqrt(squares)}")


def isMono(nums):
    mono = True
    num = min(nums)
    for x in nums:
        if x < num:
            mono = False
            break
        num = x
    if mono == False:
        first = max(nums)
        for x in nums:
            if x > num:
                mono = False
                break
            num = x
    return mono


def is_string_Palindrome(s):
    if s == s[::-1]:
        print("palindrome")
    else:
        print("not palindrome")


def sum_over_k(sentence, k):
    num = 0
    words = sentence.split(" ")
    for x in words:
        if len(x) > k:
            num += 1
    print(f"number of words above {k} letters is : {num}")


def DicAvg(dictionary):
    avg = 0

    for x in dictionary:
        avg += dictionary[x]
    print(avg / len(dictionary))


def common_divisors(param1, param2):
    list_of_divisors = []

    for x in range(2, min(param1, param2) + 1):
        if param1 % x == 0 and param2 % x == 0:
            list_of_divisors.append(x)
    print(list_of_divisors)


def LBSearch(nums, search_item, search_type):
    if search_type == "linear":
        for x in nums:
            if x == search_item:
                print("found you")
                return
        print("you are not here :(")

    if search_type == "binary":
        nums = sorted(nums)
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = math.floor((L + R) / 2)
            if nums[m] < search_item:
                L = m + 1
            elif nums[m] > search_item:
                R = m - 1
            else:
                print("found you")
                return

        print("you are not here :(")


def isPrime(param):
    for x in range(2, param):
        if param % x == 0:
            print("not prime")
            return
    print("is prime")
    pass


def weirdPrint(param):
    new_list = []
    for x, y in enumerate(param):
        if x % 2 == 0 and y % 2 == 0:
            new_list.append(y)
    print(new_list)

    pass


def TypeCount(**kwargs):
    types = {
        "int": 0,
        "bool": 0,
        "float": 0,
        "string": 0}

    for x in kwargs:
        if type(kwargs[x]) == type(int()):
            types["int"] += 1
        elif type(kwargs[x]) == type(bool()):
            types["bool"] += 1
        elif type(kwargs[x]) == type(float()):
            types["float"] += 1
        elif type(kwargs[x]) == type(str()):
            types["string"] += 1

    print(types)


def main():
    # exe1
    nums = [1, 2, 444, 12, -122, 3344, 11, 44, 15, -9855]

    find_max(nums)

    # exe2
    factorial(4)

    # exe3
    my_sum(nums)

    # exe 4
    list_count([['a', 'a', 't', 'o'], 'a'])

    # exe 5
    norm(nums)

    # exe 6
    print(isMono(nums))

    # exe 7
    is_string_Palindrome("john")

    # exe 8
    sentence = 'Do or do not there is no try'
    k = 2
    sum_over_k(sentence, k)

    # exe 9
    DicAvg({'a': 1, 'b': 2, 'c': 8, 'd': 1})

    # exe 10
    common_divisors(120, 20)

    # exe 11
    l = [1, 2, 50, 74]
    LBSearch(l, 50, 'linear')
    LBSearch(l, 74, 'binary')
    LBSearch(l, 100, 'binary')

    # exe 12
    isPrime(17)

    # exe 13
    weirdPrint([1, 2, 2, 3, 4, 5])

    # exe 14
    TypeCount(a=1, b='string', c=1.0, d=True, e=False)


if __name__ == "__main__":
    main()
