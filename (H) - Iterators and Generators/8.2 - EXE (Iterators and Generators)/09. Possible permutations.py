from itertools import permutations


def possible_permutations(numbers_list):
    permutation_object = permutations(numbers_list)
    for permutation_tuple in permutation_object:
        yield list(permutation_tuple)


# [print(n) for n in possible_permutations([1, 2, 3])]
