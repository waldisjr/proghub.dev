import itertools


def Turing(a):
    a_list = tuple(a.lower())
    return sorted(list(itertools.permutations(a_list))).index(a_list)+1


if __name__ == '__main__':
    print(Turing("Turing"))
