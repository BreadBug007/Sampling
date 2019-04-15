import pygame as py
import random
import math


def main():
    for i in range(10):
        if len(active_list) > 0:
            rand = random.randint(0, len(active_list) - 1)
            pos = active_list[rand]
            found = False

            for n in range(k):
                for r_new in range(r, 2 * r):
                    angle = random.random() * math.pi * 2
                    x_new = r_new * math.cos(angle)
                    y_new = r_new * math.sin(angle)
                    new_pos = py.math.Vector2(x_new + pos.x, y_new + pos.y)
                    col = int(new_pos.x / w)
                    row = int(new_pos.y / w)

                    if (0 < col < cols - 1) and (0 < row < rows - 1):
                        active = True
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                index = (col + i) + (row + j) * cols
                                new_sample = grid[index]
                                if new_sample != -1:
                                    d = new_pos.distance_to(new_sample)
                                    if d < r:
                                        active = False
                        if active:
                            found = True
                            grid[col + row * cols] = new_pos
                            active_list.append(new_pos)
                            break
            if not found:
                active_list.pop(rand)

    for i in grid:
        if i != -1:
            py.draw.circle(screen, white, (int(i[0]), int(i[1])), 2, 0)

    for i in active_list:
        py.draw.circle(screen, red, (int(i[0]), int(i[1])), 2, 0)


py.init()

clock = py.time.Clock()
width, height = 800, 600
screen = py.display.set_mode((width, height))

r = 10
w = r / math.sqrt(2)             # So that each grid cell will contain at most one sample
rows, cols = int(height/w), int(width/w)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

k = 30          # No of tries before deciding to stop searching for samples

active_list = []

grid = [-1 for num in range(cols*rows)]

x = random.randint(0, width)
y = random.randint(0, height)
i = int(x / w)
j = int(y / w)
pos = py.math.Vector2(x, y)

grid[i + j * cols] = pos
active_list.append(pos)

flag = True

while flag:
    for event in py.event.get():
        if event.type == py.QUIT:
            flag = False

    main()

    if len(active_list) == 0:
        flag = False

    py.display.update()
    clock.tick(60)
    py.image.save(screen, "Poisson Disk Sampling.jpg")

py.quit()