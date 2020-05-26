import datetime


def main():

    c1= "  |:H:a:p:p:y:|"
    c2= "__|___________|__"
    c3= "|^^^^^^^^^^^^^^^^^|"
    c4= "|:B:i:r:t:h:d:a:y:|"
    c5= "|                 |"
    c6= "~~~~~~~~~~~~~~~~~~~"

    date = input("enter your birtday in DD/MM/YYYY: ")

    days, month, year= date.split("/")

    date = input("enter today in DD/MM/YYYY: ")

    days_now, month_now, year_now = date.split("/")

    age = int(year_now)-int(year)

    print(age)
    header="   "
    for i in range(int((11-age%10)/2)):
        header+="_"
    for i in range(age%10):
        header+="i"
    for i in range(int((11 - age % 10) / 2)):
        header += "_"

    print(header)
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    print(c5)
    print(c6)

    if int(year)%4 == 0:
        print(header)
        print(c1)
        print(c2)
        print(c3)
        print(c4)
        print(c5)
        print(c6)

if __name__ == "__main__":
    main()
