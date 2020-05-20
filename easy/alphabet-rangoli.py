import string


def print_rangoli(size):
    alphabet = string.ascii_lowercase

    height = size * 2 - 1
    width = height * 2
    midHeight = (height // 2)
    line = 0

    for y in range(height):
        letters = list()
        for i in range(line+1):
            letters.append(alphabet[size-i-1])
        for i in range(len(letters)-2, -1, -1):
            letters.append(letters[i])
        antLines = width - len(letters)*2-2
        print("-" * int(antLines/2+1), end="")
        print('-'.join(letters), end="")
        print("-" * int(antLines/2+1))

        if y < midHeight:
            line += 1
        else:
            line -= 1


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
