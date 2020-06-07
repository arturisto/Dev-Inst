def favourite_book(title):

    print(f"One of my favorite books is {title}")

def favourite_shirt_pos(size,text):
    print(f"you ordered a shirt sized {size} with a '{text}' as text")
def favourite_shirt_kwargs(**kwargs):

    print(f"you ordered a shirt sized {kwargs['size']} with a '{kwargs['text']}' as text")
def print_magicians(magicians):
    for x in magicians:
        print(x)
def make_great(magicians):
    new_list = []
    for x in magicians:
        new_list.append(x+" The Great")
    return new_list
def check_drivers_age(age):

    if int(age) < 18:
        return "Sorry, you are too young to drive this car. Powering off"
    elif int(age) > 18:
        return "Powering On. Enjoy the ride!"
    elif int(age) == 18:
        return "Congratulations on your first year of driving. Enjoy the ride!"

def main():

    #exe1
    favourite_book("The Name of The Rose")
    #exe2
    favourite_shirt_pos("XL","you say a villain like it's a bad thing")
    favourite_shirt_kwargs(size= "XL", text = "you say a villain like it's a bad thing")

    #exe3+4
    magicians = ['Berkovich','Houdini', 'Hummus','Sushard']
    print_magicians(make_great(magicians))

    #exe5
    age = input("What is your age?: ")
    print (check_drivers_age(age))
if __name__ == "__main__":
    main()
