def main():
    d_ages = {
        "yael": 27,
        "dani": 31,
        "Julie": 30,
        "Shmecht": 19
    }
    print(d_ages)
    d_exe2 = {0: 10, 1: 20}
    d_exe2[2] = 30
    print(d_exe2)
    mx = 0
    for x in d_ages:
        if d_ages[x] > mx:
            mx = d_ages[x]
    print(mx)

    products = {"SMART WATCH": 550, "PHONE": 1000, "PLAYSTATION": 500, "LAPTOP": 1550, "MUSIC PLAYER": 600,
                "TABLET": 400
                }
    for key in products:
        print(key, products[key])
    i = 0
    while i < len(products):
        print(list(products)[i], products[list(products)[i]])
        i += 1

    products = {"SMART WATCH": 550, "PHONE": 1000, "PLAYSTATION": 500, "LAPTOP": 1000, "MUSIC PLAYER": 600,
                "TABLET": 500
                }
    products_new = {}
    flag = False
    for x in products:
        for y in products_new:
            if products[x] == products_new[y]:
                flag = True
        if not flag:
            products_new[x] = products[x]
        flag = False
    print(products_new)

    products = {"SMART WATCH": 550, "PHONE": 1000, "PLAYSTATION": 500, "LAPTOP": 1000, "MUSIC PLAYER": 600,
                "TABLET": 500
                }
    given_key = "TABLET"

    if given_key in list(products):
        print("the key is in the dict")

    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    dic4 = {**dic1, **dic2, **dic3}
    print(dic4)

    list1 = ['Rick', 'Donald', 'Mickey', 'Mario']
    list2 = ['Sanchez', 'Duck', 'Mouse', 'Kart']

    dic_names = {}

    for x in list1:
        dic_names[x] = list2[list1.index(x)]
    print(dic_names)

    products = {"SMART WATCH": 550, "PHONE": 1000, "PLAYSTATION": 500, "LAPTOP": 1550, "MUSIC PLAYER": 600,
                "TABLET": 500
                }
    x = int(input("how much money have you got?: "))

    print("you can afford the following:")
    for y in products:
        if x >= products[y]:
            print(y)

    num_to_letter = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "zero"
    }

    x = input("enter a number from 100 to gazilion: ")
    s = ""
    for y in x:
        s = s + num_to_letter[int(y)] + " "
    print(s)

    contacts = {
        "Eyal":"0586878399",
        "John":"0542815674",
        "Mario":"0512345678"
    }
    contacts["Arthur"] = "0529464352"

    for x in contacts:
        print(x +": "+contacts[x])
    search = "robert"

    if search in list(contacts):
        print(search+" is in contacts")
    else:
        print(search + " not is in contacts")

    search = "0529464352"

    for x in contacts:
        if contacts[x] == search:
            print(x+" is found")
            break;

    contacts2 = {
        "Yeal":"0528801520",
        "Aba": "0529465556",
        "Ima":"0545884455"
    }
    for x in contacts2:
        contacts[x] = contacts2[x]
    i =0
    for x in contacts:
        i+=1

    l = sorted(list(contacts))
    for x in l:
        print(x+" : "+contacts[x])

    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}

    for x in d2:
        if x in d1:
            d1[x]=d1[x]+d2[x]
        else:
            d1[x] = d2[x]
    print(d1)
if __name__ == "__main__":
    main()
