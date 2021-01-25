# Minesweeper
import random as r

fieldsize = 20
minefield = [[[] for a in range(fieldsize+2)] for b in range(fieldsize+2)]

def check(x, y):
    minecount = 0
    leftx = x - 1 
    rightx = x + 1

    upy = y - 1
    downy = y + 1
 
    if minefield[upy][leftx] == "#":
        minecount += 1
    if minefield[y][leftx] == "#":
        minecount += 1
    if minefield[downy][leftx] == "#":
        minecount += 1
    if minefield[upy][x] == "#":
        minecount += 1
    if minefield[downy][x] == "#":
        minecount += 1   
    if minefield[upy][rightx] == "#":
        minecount += 1
    if minefield[y][rightx] == "#":
        minecount += 1
    if minefield[downy][rightx] == "#":
        minecount += 1     
    return minecount

def plantmine(x, y):
    for a in range(len(minefield[1:-1])):
        if a == y:
            for b in range(len(minefield[a][1:-1])):
                if b == x:
                     minefield[a+1][b+1] = "#"                 
    return

for c in range(80):
	plantmine(r.randint(0, fieldsize), r.randint(0, fieldsize))

for a in range(len(minefield[1:-1])):
	for b in range(len(minefield[a][1:-1])):
		if minefield[a+1][b+1] != "#":
			y = check(b+1, a+1)
			minefield[a+1][b+1] = str(y)

for a in minefield:
	print(a)