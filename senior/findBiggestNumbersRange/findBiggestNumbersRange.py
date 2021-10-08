def findBiggestNumbersRange(sequence):
    sequence.sort()

    answer = [[]]
    now_working = False

    for el_num in range(len(sequence)):
        try:
            if sequence[el_num+1] - 1 == sequence[el_num]:
                if now_working:
                    answer[-1].append(sequence[el_num])
                elif not now_working:
                    now_working = True
                    answer[-1].append(sequence[el_num])
            elif sequence[el_num+1] == sequence[el_num]:
                answer[-1].append(sequence[el_num])
            else:
                if answer[-1][-1] + 1 == sequence[el_num]:
                    answer[-1].append(sequence[el_num])
                now_working = False
                answer.append([])
        except IndexError:
            answer[-1].append(sequence[el_num])

    max_len = 0
    max_len_index = int()
    for list_num in range(len(answer)):
        if len(answer[list_num]) > max_len:
            max_len = len(answer[list_num])
            max_len_index = list_num
    return [answer[max_len_index][0], answer[max_len_index][-1]]


if __name__ == '__main__':
    print(findBiggestNumbersRange([1, 0, 4, 6, 24, 14, 11, 3, 10, 2, 15, 0, 5, 16, 8, 12, 9, 13, 23]))
    print(findBiggestNumbersRange([1, 2, 3, 4, 5, 6]))
    print(findBiggestNumbersRange([-8, -7, -7, -7, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12, 12, 12, 13, 14, 15, 16, 17, 18, 19]))
