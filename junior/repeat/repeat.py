def Repeat(arr):
    answ = []
    new = []
    for el in arr:
        if el in new and el not in answ:
            answ.append(el)
        new.append(el)
    return answ


if __name__ == '__main__':
    print(Repeat([1, 3, 2, 2, 3, 0]))
