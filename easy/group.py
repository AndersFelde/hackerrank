inpt = input()
for x in range(len(inpt)):
    char = inpt[x]
    if x+1 == len(inpt):
        break
    if char.isalnum() and char == inpt[x+1]:
        print(char)
        exit()

print(-1)
