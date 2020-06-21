import json
class MenuManager:

    def __init__(self):
        self.menu = {}
        with open("menu.json", "r") as file:
            self.menu = json.load(file)

    def add_item(self,name,price):

        self.menu[name] = price

    def remove_item(self, name):
        del self.menu[name]

    def save_to_file(self):
        with open("menu.json", "w") as file:
            json.dump(self.menu, file)


