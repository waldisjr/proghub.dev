def Reverse(a):
    return ' '.join(map(str, a.split()[::-1])) if not a.isspace() else a


if __name__ == '__main__':
    print(Reverse("   "))
