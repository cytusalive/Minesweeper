# Minesweeper
import random as r
import pygame
import sys

pygame.init()
pygame.display.set_caption("Minesweeper")
screen = pygame.display.set_mode((600, 600))
bgcolor = (200, 200, 250)
screen.fill(bgcolor)
clock = pygame.time.Clock()

fieldsize = 20
minefield = [[None for a in range(fieldsize+2)] for b in range(fieldsize+2)]
sqsize = screen.get_width() // (fieldsize+2)
revealed = [[False for a in range(fieldsize+2)] for b in range(fieldsize+2)]

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

for c in range(70):
	plantmine(r.randint(0, fieldsize), r.randint(0, fieldsize))

for a in range(len(minefield[1:-1])):
	for b in range(len(minefield[a][1:-1])):
		if minefield[a+1][b+1] != "#":
			y = check(b+1, a+1)
			minefield[a+1][b+1] = str(y)

for a in minefield:
	print(a)

textcolor = (200, 0, 0)
font = pygame.font.Font("freesansbold.ttf", 24)

def revealarea(x, y):
    leftx = x - 1 
    rightx = x + 1
    upy = y - 1
    downy = y + 1
    xs = [leftx, x, rightx]
    ys = [upy, y, downy]
    revealed[y][x] = True
    if minefield[y][x] == "0":
        for xi in xs:
            for yi in ys:
                if revealed[yi][xi]:
                    continue
                if minefield[yi][xi] == "#":
                    continue
                if minefield[yi][xi] == None:
                    continue
                revealarea(xi, yi)

while True:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            revealarea(mousex//sqsize, mousey//sqsize)
    for y in range(len(minefield)):
        for x in range(len(minefield[y])):
            if minefield[y][x] == None:
                pygame.draw.rect(screen, (bgcolor), (x*sqsize, y*sqsize, sqsize, sqsize))
            elif minefield[y][x] == "#":
                if revealed[y][x]:
                    text = font.render("#", True, textcolor, bgcolor)
                    screen.blit(text, (x*sqsize, y*sqsize))
                else:
                    pygame.draw.rect(screen, (200, 100, 0), (x*sqsize, y*sqsize, sqsize, sqsize))
            else:
                if revealed[y][x]:
                    text = font.render(minefield[y][x], True, textcolor, bgcolor)
                    screen.blit(text, (x*sqsize, y*sqsize))
                else:
                    pygame.draw.rect(screen, (200, 100, 0), (x*sqsize, y*sqsize, sqsize, sqsize))
    pygame.display.update()
    msElapsed = clock.tick(3)
