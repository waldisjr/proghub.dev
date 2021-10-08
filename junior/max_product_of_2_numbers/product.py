def Product(arr):
    first_max = max(arr)
    arr.remove(first_max)
    return first_max * max(arr)


if __name__ == '__main__':
    print(Product([1, -3, 2, 2, 3, 0]))
