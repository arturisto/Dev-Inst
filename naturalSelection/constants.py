#constants
import itertools

class Constants:

    all_possible_tuples_for_consumables = list(itertools.product(range(1, 10), range(1, 10)))

    all_possible_positions = list((itertools.product([0], range(1, 10))))
    all_possible_positions.extend(list(itertools.product([9], range(1, 10))))
    all_possible_positions.extend(list(itertools.product(range(1, 10), [0])))
    all_possible_positions.extend(list(itertools.product(range(1, 10), [9])))
    all_possible_positions_for_participants = all_possible_positions.copy()