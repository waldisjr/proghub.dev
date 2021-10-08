def Unique(arr):
    answ = []
    for el in arr:
        if el not in answ:
            answ.append(el)
    return answ


if __name__ == '__main__':
    print(Unique([1, 3, 2, 2, 3, 0]))
