def Zeros(arr):
    answ = []
    zeros = []
    for el in arr:
        if el != 0:
            answ.append(el)
        else:
            zeros.append(el)
    return answ+zeros


if __name__ == '__main__':
    print(Zeros([3, 0, 0, 1, 2, 0, 5, 4, 3, 3]))
