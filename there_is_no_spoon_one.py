import sys
import math

# There is no Spoon - Episode 1
# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
locations = [];
for i in range(height):
    line = input()  # width characters, each either 0 or .
    i = 0
    row = []
    for l in line:
        row.append(l)
        i = i + 1
    locations.append(row)
r = 0;
while r < len(locations):
    c = 0
    while c < len(locations[r]):
        neighbours = ""
        if locations[r][c] == "0":
            neighbours = neighbours + str(c) + " " + str(r) + " "
            nc = c + 1
            nr = r + 1
            while nc <= len(locations[r]):
                if nc == len(locations[r]):
                    neighbours = neighbours + str(-1) + " " + str(-1) + " "
                    break;
                elif locations[r][nc] == "0":
                    neighbours = neighbours + str(nc) + " " + str(r) + " "
                    break;
                nc = nc + 1
            while nr <= len(locations):
                if nr == len(locations):
                    neighbours = neighbours + str(-1) + " " + str(-1) + " "
                    break;
                elif locations[nr][c] == "0":
                    neighbours = neighbours + str(c) + " " + str(nr) + " "
                    break;
                nr = nr + 1
        c = c + 1
        if neighbours is not "":
            print(neighbours)
    r = r + 1