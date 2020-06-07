import math


def main():
    #EXE1
    l =  [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

    print("the list is: {}".format(l))
    print("Sorted descending list: {}".format(sorted(l,reverse=True)))
    print("the sum of the list is: {}".format(sum(l)))
    new_list = []
    new_list.append(l[0])
    new_list.append(l[-1])
    print("The first and the la"
          "st items of list are: {}".format(new_list))
    new_list.clear()
    for i in l:
        if i >50:
            new_list.append(i)
    print("list with items above 50: {}".format(new_list))
    new_list.clear()
    for i in l:
        if i < 10:
            new_list.append(i)
    print("list with items bellow 10: {}".format(new_list))

    new_list.clear()
    for i in l:
        new_list.append(i*i)
    print("list with items bellow 10: {}".format(new_list))

    s = set(l);
    print ("list of {} items without dupliacates: {}".format(len(s),s))

    print("the average of list is: {}".format(sum(l)/len(l)))
    print("max of list is: {}".format(max(l)))
    print("min of list is: {}".format(min(l)))

    for i in range(10):
        l.append(eval(input("input a number betweeb -100 and 100")))
    print("\n the new line is: {}".format(l))


    # exe2
    par = "'Where do they get a random paragraph?' he wondered as he clicked the generate button. Do they just write " \
          "a random paragraph or do they get it somewhere? At that moment he read the random paragraph and realized " \
          "it was about random paragraphs and his world would never be the same."
    print("the paragraph has with spaces: {} and {} without spaces".format(len(par), len(par.replace(" ", ""))))

    print("the paragraph has {} sentences".format(par.count("?") + par.count(".") + par.count("!")))

    print("the paragraph has {} words".format(par.count(" ") + 1))

    print("the paragraph has {} unique words".format(len(set(par.split(" ")))))

    str2 = par

    str2.replace("?", ".")
    str2.replace("!", ".")

    l = str2.split(".")
    print(l)
    y = 0
    for x in l:
        y += len(x.split(" "))

    print("the paragraph has {} words per sentence".format(y / 4))

    s = set(par.split(" "))
    y=0
    l.clear()
    for x in s:
        if par.count(x) >1:
            y+=1
            l.append(x)
    print("The amount of non unique words is: {}".format(y))
    print(l)

    # exe4
    string = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
    l = string.split(" ")
    s = set(l);
    l.clear()
    for x in s:
        t = ()
        t = (x, string.count(x))
        l.append(t)
    print(sorted(l))

    #exe5
    print(abs.__doc__)
    print(int.__doc__)
    print(input.__doc__)

    #exe6
    l = input("enter comma seperated numbers: ").split(",")
    print("this is a list: {}".format(l))
    print("this is a tuple: {}".format(tuple(l)))

    #exe7
    c = 50
    h=30
    l = input("enter comma seperated numbers: ").split(",")
    l2 =[]
    for x in l:
        l2.append(int(math.sqrt(2*c*int(x)/h)))
    print(l2)

if __name__ == "__main__":
    main()
