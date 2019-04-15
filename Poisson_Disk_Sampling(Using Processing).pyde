r = 10
k = 30
grid = []
active_list = []
w = r / sqrt(2)

def setup():
    global rows, cols, w, k, r, active_list, grid, pos
    size(600, 600)
    cols = int(width / w)
    rows = int(height / w)
    grid = [-1 for i in range(rows*cols)]
    
    x = random(width)
    y = random(height)
    i = int(x / w)
    j = int(y / w)
    pos = PVector(x, y)

    grid[i + j * cols] = pos
    active_list.append(pos)

    
    
def draw():
    background(0)
    for i in range(100):
        if len(active_list) > 0:
            rand = int(random(len(active_list)))
            pos = active_list[rand]
            found = False
        
            for n in range(k):
                new_pos = PVector.random2D()
                m = random(r, 2*r)
                new_pos.setMag(m)
                new_pos.add(pos)
                col = int(new_pos.x / w)
                row = int(new_pos.y / w)
                
                if col > 0 and row > 0 and col < cols - 1 and row < rows - 1:
                    
                    active = True
                    
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            index = (col + i) + (row + j)*cols
                            new_sample = grid[index]
                            if new_sample != -1:
                                d = PVector.dist(new_pos, new_sample)
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
            stroke(255)
            strokeWeight(2)
            point(i.x, i.y)
    
    for i in active_list:
        stroke(255, 0, 200)
        strokeWeight(2)
        point(i.x, i.y)
    save("Poisson Disc.jpg")
