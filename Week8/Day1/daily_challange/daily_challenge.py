class Unique:
    def __init__(self, l):
        self.list_of_numbers = l



    def subset(self):

        subsets = []
        for x in self.list_of_numbers: #outer loop for number of items in list
            subsets.append([x])
            subsets_temp = subsets.copy()
            for y in subsets_temp: #inner loop for actual numbers
                for z in self.list_of_numbers:
                    sub = y.copy()
                    if z not in sub:
                        sub.append(z)
                    if sorted(sub) not in subsets:
                        subsets.append(sorted(sub))

        subsets.append([])

        print(subsets)
        print (len(subsets))

class Threes:

    def __init__(self, l):
        self.list_of_numbers = l

    def sum_zero(self):
        list_of_zeros = []
        flag = True
        for x in self.list_of_numbers:
            for y in self.list_of_numbers:
                for z in self.list_of_numbers:
                    if x + y + z == 0:
                        for item in list_of_zeros:
                            if x in item and y in item and z in item:
                                flag = False
                        if flag:
                            list_of_zeros.append([x, y, z])
                        else:
                            flag = True

        print(list_of_zeros)


def main():
    unique = Unique([1,3,5,7,9,8])

    unique.subset()

    three = Threes([-25, -10, -7, -3, 2, 4, 8, 10])

    three.sum_zero()


if __name__ == "__main__":
    main()
