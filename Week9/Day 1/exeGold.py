from jedis import *
import random

def main():

    jedi_council = [Jedi(input("name of the jedi: ")),Jedi(input("name of the jedi: ")),Jedi(input("name of the jedi: "))]
    sith_lords = [Sith(input("name of the sith: ")),Sith(input("name of the sith: ")),Sith(input("name of the sith: "))]

    number_of_fights = 0
    while len(sith_lords) >0:

        jedi_fighter = random.randint(1,3)-1
        sith_fighter = random.randint(1,len(sith_lords))-1

        fight = jedi_council[jedi_fighter].fight_method(sith_lords[sith_fighter])
        if fight == 0:
            pass
        elif fight == 1: #jedi wins
            jedi_council[jedi_fighter].train()
            del sith_lords[sith_fighter]
        else:
            jedi_council[jedi_fighter].train()
            sith_lords[sith_fighter].train()

        number_of_fights+=1

        if number_of_fights == 100:
            print("the sith has one, everyone came to the dark side for cookies")

    print("the light has peresevered over darkness")



if __name__ == "__main__":
    main()