def main():
    # exe1
    t = []
    for i in range(3):
        arr = input("enter name age and score").split(",")
        name, age, score = arr
        t.append((name, age, score))
    print(t)

    print(sorted(t, key=lambda x: x[0]))
    print(sorted(t, key=lambda x: x[1]))
    print(sorted(t, key=lambda x: x[2]))

    #exe2

    name = input("what is your name: ")
    name_w = input("waiter's name: ")
    item_name = input("what did you order: ")
    price = eval(input("price of {}: ".format(item_name)))
    amount = int(input("how many {}s did you order:  ".format(item_name)))
    discount = eval(input("is there discount(%): "))
    vat = 17
    total = price*amount*(1+vat/100)
    discount_amount = total*discount/100
    bill_total = total-discount_amount

    bill = """
    *********************************
    *customer:{}
    *waiter:{}
    *order:{} {}s - {}
    *Total: {}
    *Discount: {}
    *Total to Pay: {}
    ********************************
    """.format(name,name_w,amount,item_name,price,total,discount_amount,bill_total)

    print(bill)

    #exe3
    l = []
    l.append(eval(input("enter the first number: ")))
    l.append(eval(input("enter the second number: ")))
    l.append(eval(input("enter the third number: ")))

    print(max(l))

    #exe4
    vowls = ['a','e',"i","o","u","y"]
    alphabet = 'abcdefghjiklmnopqrstuvwxyz'

    for x in alphabet:
        if x in vowls:
            print("{} is vowls".format(x))
        else:
            print("{} is constant".format(x))

    # exe5
    x = 4
    y = eval(input("enter a number between 1 and 9: "))
    if x != y:
        print("not equal")
    else:
        print("equal")

    #exe6
    for i in range(1,21):
        print(i)

    #exe7
    l = range(1,1000001)
    for i in l:
        print(i)

    #exe8
    l = range(1, 1000001)
    print(min(l))
    print(max(l))
    print(sum(l))


    #exe9
    item = "x"
    string = "sdxfmsklm sjxsdxdf"
    i = 0;
    for x in string:
        if x == item:
            print(i)

            break;
        i += 1


    #exe10
    l1 = [1,2,3,4,5,6]
    l2 = [7,8,9]

    for x in l2:
        l1.append(x)
    print(l1)

if __name__ == "__main__":
    main()
