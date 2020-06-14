class Currency:

    def __init__(self, name, val):
        self.currency_type = name
        self.value = val

    def __str__(self):
        return f"{self.currency_type} with value of {self.value}"

    def __repr__(self):
        return {"currency_type": self.currency_type, "value": self.value}

    def math_currency(self, another_currency, operator):

        if self.currency_type == another_currency.currency_type:

            if operator == "+":
                return self.value + another_currency.value
            elif operator == "+=":
                self.value += another_currency.value
                return self.value
            elif operator == "-":
                return self.value - another_currency.value
            elif operator == "-=":
                self.value -= another_currency.value
                return self.value
            elif operator == "*":
                return self.value * another_currency.value
            elif operator == "*=":
                self.value *= another_currency.value
                return self.value
            elif operator == "/":
                return self.value / another_currency.value
            else:
                self.value /= another_currency.value
                return self.value
        else:
            raise Exception("can't do math on different values")


class Circle:

    def __init__(self, val, param_type):
        if param_type == "radius":
            self.radius = val
            self.diameter = val * 2
        else:
            self.radius = val / 2
            self.diameter = val

    def print(self):
        print(f"circle size of {self.radius} ")

    def area(self):
        return self.radius * self.radius * 3.14

    def __add__(self, other):
        return self.radius + other.radius

    def compare(self, other):
        if self.radius > other.radius:
            print("self is larger")
        elif self.radius < other.radius:
            print("other is larger")
        else:
            print("they are equal")

    def sort(self, other):
        list_of_circles = [self, other]

        return sorted(list_of_circles, key=lambda x: x.radius)


def main():
    cur = Currency("usd", 31.3)
    cur2 = Currency("usd", 1)
    cur.__repr__()
    cur.__str__()
    print(cur.math_currency(cur2, "+"))
    print(cur.math_currency(cur2, "+="))
    print(cur.math_currency(cur2, "-"))
    print(cur.math_currency(cur2, "-="))
    print(cur.math_currency(cur2, "*"))
    print(cur.math_currency(cur2, "*="))
    print(cur.math_currency(cur2, "/"))
    print(cur.math_currency(cur2, "/="))

    cur3 = Currency("ILS", 33)
    print(cur.math_currency(cur3, "+"))

    # exe 2

    circle1 = Circle(3, "radius")
    circle2 = Circle(7, "diameter")

    circle1.area()
    circle1.print()
    circle1.__add__(circle2)

    circle1.compare(circle2)
    print(circle1.sort(circle2))


if __name__ == "__main__":
    main()
