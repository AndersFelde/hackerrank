
lst = list(map(int, input().split()))
height = lst[0]
width = lst[1]
midHeight = (lst[0] // 2)
midWidth = (lst[1] // 2)

pattern = ".|."
patternAmount = 0


for currentLine in range(height):
    x = 0
    while x < width:
        if(patternAmount == midHeight):
            print("-" * (midWidth - len(pattern)) +
                  "WELCOME" + "-" * (midWidth - len(pattern)))
            break
        elif x < midWidth - (len(pattern)*patternAmount+1) or x > midWidth + (len(pattern)*patternAmount+1):
            if(x == width - 1):
                print("-")
            else:
                print("-", end="")
            x = x+1
        else:
            """ x == midWidth - (len(pattern)*patternAmount+1) """
            for _ in range(patternAmount*2 + 1):
                print(pattern, end="")
                x = x+len(pattern)
    if(currentLine < midHeight):
        patternAmount += 1
    else:
        patternAmount -= 1
    x = 0
