import itertools
import random
from consumables import Apple
from participants import Participant
from constants import Constants


class World:
    """
    World class, holds the world on which the simulation will be performed

    #status:

    """

    def __init__(self):
        self.world_map = [[None for _ in range(10)] for _ in range(10)]
        self.movements = {}

    def create_consumables(self):
        # create random amount of apples:
        amount_of_apples = random.randint(10, 30)
        all_possible_tuples = Constants.all_possible_tuples_for_consumables
        chosen_places_for_apples = random.choices(all_possible_tuples, k=amount_of_apples)
        print(chosen_places_for_apples)

        for place in chosen_places_for_apples:
            self.world_map[place[0]][place[1]] = Apple()

    def create_participants(self):
        # create random amount of participants
        amount_of_participants = random.randint(10, 30)
        chosen_places_for_participants = random.choices(Constants.all_possible_positions_for_participants,
                                                        k=amount_of_participants)
        for place in chosen_places_for_participants:
            participant = Participant(place)
            self.world_map[place[0]][place[1]] = participant
            self.movements[participant.id] = [0,participant.place]

    def place_participants_new_generation(self):
        pass

    def move_participants(self):
        
        pass
