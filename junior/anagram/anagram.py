from collections import Counter


def Anagram(string1, string2):
    return "yes" if Counter(string1.strip('\n')) == Counter(string2.strip('\n')) else "no"


if __name__ == '__main__':
    print(Anagram("school master\n", "the classroom"))
