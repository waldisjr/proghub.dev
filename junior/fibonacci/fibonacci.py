def fibonacci(start, end):
    answ = ''
    first = -1
    second = 1
    for i in range(end):
        old_sec = second
        second = first + second
        first = old_sec
        if i >= start:
            answ += str(second) + ' '
    return answ.strip()


if __name__ == '__main__':
    print(fibonacci(10, 15))
