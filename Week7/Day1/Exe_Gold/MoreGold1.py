def main():
    #exe1
    fruits = input("enter fruits separated by space: ").split(" ")

    x = input("enter a single fruit: ")

    if x in fruits:
        print("you chose your favourite fruit. Enjoy!")
    else:
        print("You chose a new fruit. I hope you enjoy it too!")

    fruits.insert(len(fruits) - 1, "and")
    print(fruits)

    # exe2
    l_case = "abcdefghijklmnopqrstuvwxyz"
    u_case = l_case.upper()
    print(u_case)
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    chars = "$#@."
    flags = {
        "lower": False,
        "upper": False,
        "nums": False,
        "chars": False
    }
    error = False
    s = input("enter a password: ")

    if len(s) < 6 or len(s) > 12:
        print("password must be between 6 and 12")
    else:
        for x in s:
            if x in l_case:
                flags["lower"] = True
            elif x in nums:
                flags["nums"] = True
            elif x in u_case:
                flags["upper"] = True
            elif x in chars:
                flags["chars"] = True
            else:
                print("{} is not a valid character".format(x))
                error = True

    if flags["lower"] == True and flags["nums"] == True and flags["upper"] == True and flags["chars"] == True and error== False:
        print("password ok")
    else:
        print("password not ok")


    # exe3
    l = [x for x in range(3,31) if x % 3 == 0]

    for x in l:
        print(x)

    #exe4

    index = 3
    i = 17
    new_list = []
    print(l)
    for j in range(0, len(l)):
        if j == index:
            new_list.append(i)
            new_list.append(l[j])
        else:
            new_list.append(l[j])
    print(new_list)

    #exe6
    for x in range(1500, 2701):
        if x %5 ==0 and x%7 ==0:
            print(x)

    #exe7
    s="sdflksdlf sdkfl sdl;fjsdklfj sdjfsd kjsd fjsdklf jsdf"
    i=0
    for x in s:
       if x==" ":
           i+=1
    print(i)

    #exe8
    s = "sdflksdlf sdkfl sdl;fjsdklfj sdjfsd kjsd fjsdklf jsdf"

    l = s.split(" ")
    print(len(l))

    s = "lsdkflsdfAAas sdfkdsf KFSJ f ahJ HFj ahfjA hfjaf ahj"
    upp = 0
    low = 0
    for x in s:
        if x.isupper():
            upp+=1
        if x.islower():
            low+=1
    print("lower {}".format(low))
    print("upper {}".format(upp))

if __name__ == "__main__":
    main()
