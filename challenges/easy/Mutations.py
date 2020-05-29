def mutate_string(string, position, character):
    l = list(string)

    l[position] = character

    outputString = "".join(list)
    return outputString


if __name__ == '__main__':
    string = input()
    posChar = input()

    posCharArr = posChar.split(" ")
    position = int(posCharArr[0])
    character = posCharArr[1]

    print(mutate_string(string, position, character))
