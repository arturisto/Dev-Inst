class Family:

    def __init__(self):
        self.members = [
            {"name": "Bob",
             "age": 35,
             "gender": "male",
             "is_child": False},
            {"name": "Helen",
             "age": 31,
             "gender": "female",
             "is_child": False},
        ]
        self.lastname = "Parr"

    def born(self, **kwargs):
        self.members.append({"name": kwargs["name"],
                             "age": kwargs["age"],
                             "gender": kwargs["gender"],
                             "is_child": kwargs["is_child"]})
        print(f"congrats on a new {self.lastname} in the family")

    def is_18(self, name_of):
        for member in self.members:
            if member["name"] == name_of and member["age"] >= 18:
                return True
        return False

    def __repr__(self):

        for member in self.members:
            print(member["name"], member['age'], member["gender"], member["is_child"])


class TheIncredibles(Family):

    def __init__(self):
        super().__init__()
        self.members[0]["power"] = "strength"
        self.members[1]["power"] = "elasticness"
        self.members[0]["incredible_name"] = "Mr. Incredible"
        self.members[1]["incredible_name"] = "Elastigirl"

    def born_incredible(self, **kwargs):
        self.born(**kwargs)
        for i, member in enumerate(self.members):
            if member["name"] == kwargs["name"]:
                self.members[i]["power"] = kwargs["power"]
                self.members[i]["incredible_name"] = kwargs["incredible_name"]

    def use_power(self, member):
        for m in self.members:
            if m["name"] == member:
                if m["age"] >= 18:
                    print(m["power"])
                else:
                    raise Exception("You have not power here")

    def incredible_presentation(self):
        for member in self.members:
            print(member["name"], member['age'], member["gender"], member["is_child"], member["power"],
                  member["incredible_name"])


def main():
    incredibles = TheIncredibles()

    incredibles.born_incredible(name="Violet", age=15, is_child=True, gender="female", power="invisivle",
                                incredible_name="little invisible")
    incredibles.born_incredible(name="Dashiel", age=11, is_child=True, gender="male", power="speed",
                                incredible_name="Dash")
    incredibles.born_incredible(name="Jack", age=1, is_child=True, gender="male", power="unkown",
                                incredible_name="super baby")
    incredibles.__repr__()

    incredibles.incredible_presentation()


if __name__ == "__main__":
    main()
