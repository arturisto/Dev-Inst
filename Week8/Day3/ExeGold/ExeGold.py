class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sphynx(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class BankAccount:

    def __init__(self, own, bal):
        self.owner = own
        self.balance = bal

    def deposit(self, amnt):
        if amnt >= 0:
            self.balance += amnt

    def withdraw(self, amnt):
        if amnt >= 0 and self.balance >= amnt:
            self.balance -= amnt


class Owner(BankAccount):

    def __init__(self, pswrd, cred_card_num, own, bal):
        super().__init__(own, bal)
        self.password = pswrd
        self.credit_card_num = cred_card_num
        self.trials = 0

    def check_owner_info(self, pswrd, cred_card_num):
        if pswrd == self.password and cred_card_num == self.credit_card_num:
            option = int(input("Would you like\n 1- Deposint \n 2- Withdraw \n>>"))
            if option == 1:
                while True:
                    print("i accept bills from 20 to 100, how much do you want to deposit?")
                    deposit_20 = int(input("how much 20s would you like to deposit? >>"))
                    deposit_50 = int(input("how much 50s would you like to deposit? >>"))
                    deposit_100 = int(input("how much 100s would you like to deposit? >>"))
                    print(f" you deposited{deposit_20 * 20 + deposit_50 * 50 + deposit_100 * 100}")
                    self.deposit(deposit_20 * 20 + deposit_50 * 50 + deposit_100 * 100)

                    choice = input("Do you want to make another deposit Y/N >>")

                    if choice == "Y":
                        continue
                    else:
                        return
        else:
            self.trials += 1
            if self.trials == 0:
                self.credi_card_num = 0
                print("the card was eaten by the machine")

    def withdraw(self, amnt):

        while True:
            amnt_to_withdraw = int(input("How much do you like to withdraw?\n >>"))

            if self.balance < amnt_to_withdraw:
                print("insufficient funds")
            else:
                bills_50 = int(amnt_to_withdraw / 50)
                bills_20 = int((amnt_to_withdraw - bills_50 * 50) / 20)

                if bills_50 * 50 + bills_20 * 20 == amnt_to_withdraw:
                    self.balance -= (bills_50 * 50 + bills_20 * 20)
                    print(f"you withdrew {bills_50} 50s and {bills_20} 20s")

                else:
                    print("I can give you only 50s and 20s")

            choice = input("Do you want to make another withdrawal Y/N >>")

            if choice == "Y":
                continue
            else:
                return


class Bank:
    accounts = []

    def add_account(self, pswrd, cred_card_num, own, bal):
        if len(self.accounts) < 10:
            self.accounts.append(Owner(pswrd, cred_card_num, own, bal))
        else:
            print("The bank can't take any more accounts")

    def how_much_money(self):
        bal = 0
        for acc in self.accounts:
            bal += acc.balance
        print(f"The current balance of the bank is {bal} New Shekels")


def main():
    # exe1
    my_cats = [Bengal("rum tum tuger", 20), Chartreux("grizzabella", 30), Sphynx("McAvity", 15)]
    my_pets = Pets(my_cats)
    my_pets.walk()

    # exe2
    owner = Owner(123, 321, "Arthur", 1000)

    owner.check_owner_info(123, 321)
    owner.deposit(121)
    owner.deposit(170)
    owner.withdraw(1500)


if __name__ == "__main__":
    main()
