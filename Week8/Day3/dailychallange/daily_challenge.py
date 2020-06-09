import random


class Gene:

    def __init__(self):
        if random.random() >= 0.5:
            self.param = 1
        else:
            self.param = 0

    def mutate_gene(self):
        if self.param == 0:
            self.param = 1
        else:
            self.param = 0



class Chromosome:

    def __init__(self):
        self.list_of_genes = [Gene() for i in range(10)]

    def mutate_chromosome(self):
        x = random.randint(1, 10)
        mutated_genes = random.sample(range(10), x)

        for x in mutated_genes:
            self.list_of_genes[x].mutate_gene()


class DNA:
    def __init__(self):
        self.list_of_chromosomes = [Chromosome() for i in range(10)]

    def mutate(self):
        x = random.randint(1, 10)
        mutated_genes = random.sample(range(10), x)

        for x in mutated_genes:
            self.list_of_chromosomes[x].mutate_chromosome()


class Organism(DNA):

    def __init__(self):
        self.prob_to_mutate = random.random()
        super().__init__()

    def check_if_human(self):
        can_mutate = random.random()
        if can_mutate <= self.prob_to_mutate:
            for chrom in self.list_of_chromosomes:
                for gene in chrom.list_of_genes:
                    if gene.param != 1:
                        return False
            return True


def main():
    orgs = [Organism(), Organism(), Organism()]
    generations = 0
    while generations <= 10000000:
        for org in orgs:
            org.mutate()
            if org.check_if_human():
                print(f"is human!!\n it took only {generations} generations")
                return
        generations += 1

    print("humans haven't evolved yet :(")


if __name__ == "__main__":
    main()
