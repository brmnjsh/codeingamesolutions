import sys
import math

# Shadows of the Knight - Episode 1
# https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
yMin = 0
yMax = h - 1
xMin = 0
xMax = w - 1
yM = 0
xM = 0
first = True
print(w, h, file=sys.stderr)
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if "D" in bomb_dir:
        if first is not True:
            yMin = int(yM + 1)
    if "U" in bomb_dir:
        if first is not True:
            yMax = int(yM - 1)
    if "R" in bomb_dir:
        if first is not True:
            xMin = int(xM + 1)
    if "L" in bomb_dir:
        if first is not True:
            xMax = int(xM - 1)
    
    first = False
    yM = int((yMin + yMax) / 2)    
    xM = int((xMin + xMax) / 2)    
    print(yM, xM, bomb_dir, file=sys.stderr)
    print(xM, yM)   
    # the location of the next window Batman should jump to.
    #print(0, m)