def main():
    print("# exe")

    basket = ["Banana", "Apples", "Oranges", "Blueberries"];

    basket.remove("Banana");
    basket = basket[:-1];
    basket.append("Kiwi");
    basket.insert(0, "Apples");
    print(basket.count("Apples"));
    basket = [];

    print(basket);

    print("# exe1")
    my_fav_numbers = {7, 777, 77, 7777, 3};
    my_fav_numbers.add(4);
    my_fav_numbers.add(77777);
    my_fav_numbers.pop();
    friend_fav_numbers = {3, 333, 33, 77, 7, 565556566};
    my_fav_numbers.update(friend_fav_numbers);
    print(my_fav_numbers);
    print("# exe2")
    my_fav_numbers = (7, 777, 77, 7777, 3);
    new_num = (4, 4);
    my_fav_numbers = my_fav_numbers + new_num;
    l = list(my_fav_numbers);
    l.pop();
    my_fav_numbers = tuple(l)
    new_t = (1, 2, 3)
    my_fav_numbers = my_fav_numbers + new_t;
    print(my_fav_numbers);

    print("# exe3")
    l = []
    for x in range(3, 11):
        l.append(x / 2)
    print(l)

    print("# exe4")
    topings = [];
    quit = True;

    # while(quit):
    #     toping = input("enter a topping: ")
    #     if toping != "quit":
    #         print("you are adding {} on the pizza".format(toping))
    #         topings.append(toping);
    #     else:
    #         break;
    # print(topings);

    # print("# exe5")
    #
    # for i in range(3):
    #     x = int(input("enter a number"))
    #     if x <=3:
    #         print("ticket is free");
    #     elif x <=12:
    #         print("the ticket is  10 bucks");
    #     else:
    #         print("the ticket is 12 bucks");
    #
    print("exe6");
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    while (len(list2) > 0):
        print(list2[-1])
        list2.pop()

    print("exe7");
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];

    for i in list2:

        if i <=3:
            print("ticket is free");
        elif i <=12:
            print("the ticket is  10 bucks");
        else:
            print("the ticket is 12 bucks");

    print("exe8");
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    i = 0
    while( i<len(list2)):
        if i%2 ==0:
            print(list2[i])
        i+=1

    print("exe9");

    while(True):
        x = input("enter age or quit");
        if (x == "quit"):
            break;
        else:
            x = int(x)
            if  16<=x<=21:
                print("you can see the movies");
            else:
                print("you can't see the movie");

    print("exe10");



    list3 = ["joye", "chanlder", "monica"]
    new_list=[]
    for x in list3:
        age = int(input("{}, tell me your age".format(x)))
        if age >=16:
            new_list.append(x)
    print(new_list)
if __name__ == "__main__":
    main()
