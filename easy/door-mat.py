
lst = list(map(int, input().split()))
height = lst[0]
width = lst[1]
midHeight = (lst[0] // 2)
midWidth = (lst[1] // 2)

z = 0
y = 0
heightCount = 0
for _ in range(height):
    x = 0
    while x < width:
        if(y == midHeight):
            print("-" * (midWidth - 3) + "WELCOME" + "-" * (midWidth - 3))
            break
        elif x < midWidth - (3*y+1) or x > midWidth + (3*y+1):
            if(x == width - 1):
                print("-")
            else:
                print("-", end="")
            x = x+1
        elif x == midWidth - (3*y+1):
            for _ in range(z + 1):
                print(".|.", end="")
                x = x+3
    if(heightCount < midHeight):
        z = z+2
        y = y+1
    else:
        z = z-2
        y = y - 1
    x = 0
    heightCount = heightCount + 1
