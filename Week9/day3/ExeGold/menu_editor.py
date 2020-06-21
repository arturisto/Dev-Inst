import menu_manager


def load_manager():
    return menu_manager.MenuManager()


def show_user_menu():
    print("""        User Menu:
    (a) Add item
    (r) Remove Item
    (s) Show Restaurant Menu
    (x) Save menu and exit the application""")


def add_item_to_menu(menu):
    name_of_dish = input("Enter name of the dish\n>>")
    try:
        price_of_dish = round(float(input("Enter price of the dish\n>>")), 2)
    except:
        print("Wrong input")
        return

    if any(dish["name"] == name_of_dish for dish in menu["items"]):
        print(f"{name_of_dish} already in the menu, please delete it first")
        return menu
    else:
        menu["items"].append({"name": name_of_dish, "price": price_of_dish})
        print(f"{name_of_dish} was added to the menu")
    return menu


def remove_item_from_menu(menu):
    name_of_dish = input("Enter name of the dish to be delted\n>>")

    if not any(dish['name'] == name_of_dish for dish in menu["items"]):
        print(f"{name_of_dish} not on the menu")
        return menu
    else:
        for i, item in enumerate(menu["items"]):
            if item["name"] == name_of_dish:
                del menu["items"][i]
                print(f"{name_of_dish} was removed")
                return menu


def show_resturant_menu(menu):
    for item in menu["items"]:
        print(f"{item['name']}: {item['price']} $")


def main():
    pass

    manager = load_manager()

    while True:

        show_user_menu()
        user_input = input(">>")
        if user_input not in ["a", "r", "s", "x"]:
            print("wrong input")
            continue

        if user_input == "a":
            manager.menu = add_item_to_menu(manager.menu)
        elif user_input == "r":
            manager.menu = remove_item_from_menu(manager.menu)
        elif user_input == "s":
            show_resturant_menu(manager.menu)
        else:
            manager.save_to_file()


if __name__ == "__main__":
    main()
