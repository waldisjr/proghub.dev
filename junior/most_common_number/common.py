from collections import Counter


def Common(arr):
    return Counter(arr).most_common()[0][0]


if __name__ == '__main__':
    print(Common([1, 3, 2, 2, 2, 3, 0]))
