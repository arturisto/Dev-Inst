import random


def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 3), 2)
    if season == "spring":
        return round(random.uniform(4, 23), 2)
    if season == "summer":
        return round(random.uniform(24, 40), 2)
    if season == "autumn":
        return round(random.uniform(4, 20), 2)


def main():
    x = int(input("what number month it is?: "))
    if 1 <= x <= 2 or x == 12:
        season = "winter"
    if 3 <= x <= 5:
        season = "spring"
    if 6 <= x <= 8:
        season = "summer"
    if 9 <= x <= 11:
        season = "fall"
    temp = get_random_temp(season)
    print("The temperature right now is {} degrees Celsius.".format(temp))

    if temp <= 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 < temp <= 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 < temp <= 23:
        print("the temperature is chilly, take sweater")
    elif 24 <= temp <= 32:
        print("it is nice outside")
    else:
        print("it is sunny outside, take your sunnies")


if __name__ == "__main__":
    main()
