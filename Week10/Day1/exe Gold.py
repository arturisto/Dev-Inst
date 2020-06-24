from datetime import date
from datetime import timedelta

import holidays


def countownd(today):
    days_between = date(2021, 1, 1) - today
    for i in range(days_between.days, 0, -1):
        print(f"there are {i} days until january first")

    print("\n\n")


def next_holiday(today):
    i = 1
    holi_day = ""
    while True:
        if holidays.Israel().get(timedelta(days=i) + today):
            holi_day = holidays.Israel().get(today + timedelta(days=i))
            break
        i += 1
    for i in range(i, 0, -1):
        print(f"there are {i} day until {holi_day}")
    print(f"{holi_day} is today!")

def main():
    today = date.today()
    print(today)

    countownd(today)

    next_holiday(today)



if __name__ == "__main__":
    main()
