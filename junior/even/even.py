def Even(arr):
    answ = []
    for el in arr:
        if el % 2 == 0:
            answ.append(el)
    return answ


if __name__ == '__main__':
    print(Even([1, 2, 3, 4, 5]))
