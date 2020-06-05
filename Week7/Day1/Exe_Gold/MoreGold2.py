def main():
    # exe1
    l = [1, "a", 2, 2, "a", "c", "b", "3", 4]
    nums = []
    s = []
    for x in l:
        if isinstance(x, str):
            s.append(x)
        else:
            nums.append(x)
    print(s)
    print(nums)

    # exe2
    s = "quick fox jumped over the lazy dog"
    sub_s = ""
    l = []

    for x in s:
        if x != " ":
            sub_s += x
        else:
            l.append(sub_s)
            sub_s = ""
    l.append(sub_s)
    print(l)

    # exe4
    l = s.split(" ")
    max = ""
    for x in l:
        if len(max) < len(x):
            max = x
    print(max)

    # exe5
    password = "123456789111"
    new_pas = ""

    for x in password:
        new_pas += "*"
    print(new_pas)

    # exe5 & 6
    sandwich_orders = ["some pastrami", "BLT", "Sabich", "pastrami and tomato", "Eggs and Ham", "pastrami and egg",
                       "Turkey on Rye", "Omlette du Fromage"]
    finished_orders = []
    print("the deli run out of pastrami")
    i = 0
    while i < len(sandwich_orders):
        if "pastrami" in sandwich_orders[i]:
            del sandwich_orders[i]
        else:
            i += 1

    for x in sandwich_orders:
        print("i made your {}".format(x))
        finished_orders.append(x)
    print(", ".join(finished_orders))

    #exe 7
    s = ""
    for i in range(3,0,-1):
        for j in range(0,i+1):
            s+=" "
        for j in range(0,7-i*2):
            s+="*"
        print(s)
        s=""


    #exe8

    s = ""
    for i in range (5,0,-1):
        for j in range(0,i):
            s+=" "
        for j in range(0,6-i):
            s+="*"
        print(s)
        s = ""


    #exe9
    s = ""
    for i in range(1,6):
        for j in range(0,i):
            s+="*"
        for j in range(0,5-i):
            s+=" "
        print(s)
        s = ""
    s = ""
    for i in range(0, 5):
        for j in range(0, i):
            s += " "
        for j in range(0, 5-i):
            s += "*"
        print(s)
        s = ""



if __name__ == "__main__":
    main()
