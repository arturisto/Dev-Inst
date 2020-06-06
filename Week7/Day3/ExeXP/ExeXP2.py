def get_age(year, month, day):
    curr_year = 2020
    curr_month = 6
    curr_day = 6

    curr_age = curr_year - year

    if curr_month < month:
        return curr_age - 1
    elif curr_month > month:
        return curr_age
    elif curr_day < day:
        return curr_age - 1
    else:
        return curr_age


def can_retire(age, sex):
    if (sex == "M" and age >= 67) or (sex == "F" and age >= 65):
        return True
    else:
        return False


def favourite_shirt_pos(size="L", text="I Love Python"):
    print(f"you ordered a shirt sized {size} with a '{text}' as text")

def describe_city(city ="Tel Aviv", country ="Israel"):
    print(f"{city} is in {country}")

def display_message():
    print("I am learning hot to properly use functions")
def main():
    # exe1
    year, month, day = input("enter you birthday in format YYYY/MM/DD \n>>").split("/")
    age = get_age(int(year), int(month), int(day))

    sex = input("enter your sex F or M\n>> ")
    if can_retire(age, sex):
        print("you can retire")
    else:
        print("you can't retire just yet")
    # exe2

    favourite_shirt_pos("XL", "you say a villain like it's a bad thing")
    favourite_shirt_pos("M")
    favourite_shirt_pos()


    # exe3
    describe_city()
    describe_city("Tokyo","Japan")
    describe_city("Pskov","Russia")
    # exe4
    display_message()


if __name__ == "__main__":
    main()
