from datetime import date
from faker import Faker
import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation


def calc_minutes(birthday):
    delta = (date.today() - date(birthday[0], birthday[1], birthday[2])).days

    print(f"you have lived {delta * 24 * 60} minutes")


class PasswordGen:

    def __init__(self):
        self.password = ""
        self.len_of_password = random.randint(6, 30)

    def generate(self):

        # 1 digit
        self.password += random.choice(lower)
        # 1 lower case
        self.password += random.choice(upper)
        # 1 upper case
        self.password += random.choice(digits)
        # 1 special char
        self.password += random.choice(special)
        all_chars = lower + upper + digits + special
        self.password += "".join(random.choices(all_chars, k=(self.len_of_password - 4)))
        shuffled = list(self.password)
        random.shuffle(shuffled)
        self.password = "".join(shuffled)

    def check_password(self):
        flags = [False, False, False, False]

        if not 6 <= len(self.password) <= 30:
            return False
        for char in self.password:
            if char in lower:
                flags[0] = True
            elif char in upper:
                flags[1] = True
            elif char in digits:
                flags[2] = True
            elif char in special:
                flags[3] = True
            else:
                continue

            if False not in flags:
                return True
        if False not in flags:
            return True
        return False

    def self_test(self):
        success_test = 0
        fail_test = 0

        for i in range(100):
            self.generate()
            if self.check_password():
                success_test+=1
            else:
                fail_test+=1

            self.password=""
        print(f"success: {success_test} ; fail: {fail_test}")

def main():
    calc_minutes([1989, 6, 27])
    fake = Faker()
    user = {}

    number_of_users = random.randint(1, 10)
    for i in range(number_of_users):
        user[fake.name()] = [fake.address(), fake.text(), fake.language_name()]
    print(user)

    # exe 3 random password generator:

    my_password = PasswordGen()
    my_password.self_test()


if __name__ == "__main__":
    main()
