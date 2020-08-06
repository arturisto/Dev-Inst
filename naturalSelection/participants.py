class Participant:
    """
    Classes for simulation inhabitants

    """

    # id - the original place of the participant
    def __init__(self, id, son_of=None):
        self.id = id
        self.generations_lived = 0
        self.isActive = True
        self.parent = son_of


    def print_me(self):
        if self.parent:
            print(f"I am {self.id}, i've lived for {self.generations_lived} generations!"
                  f"I am first of my kind")
        else:
            print(f"I am {self.id}, i've lived for {self.generations_lived} generations!"
                  f"my parent is {self.parent}")
