def Reverse(a):
    if a == len(a) * a[0]:
        return a
    return ' '.join(a.split()[::-1])


if __name__ == '__main__':
    print(Reverse("hello world"))
