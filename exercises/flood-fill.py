def change_color(screen, x, y, row_ct, col_ct, old_color):
    if 0 <= x < col_ct and 0 <= y < row_ct and screen[x][y] == old_color:
        return True
    return False

def flood_fill(screen, x, y, new_color):
    screen = screen
    old_color = screen[x][y]
    row_ct = len(screen)
    col_ct = len(screen[0])
    
    q = []
    q.append([x,y]) # append the starting coords
    screen[x][y] = new_color # changing starting coords with new color

    while q:
        current = q.pop()
        pos_x = current[0]
        pos_y = current[1]

        if change_color(screen, pos_x + 1, pos_y, row_ct, col_ct, old_color):
            screen[pos_x + 1][pos_y] = new_color
            q.append([pos_x + 1, pos_y])

        if change_color(screen, pos_x - 1, pos_y, row_ct, col_ct, old_color):
            screen[pos_x - 1][pos_y] = new_color
            q.append([pos_x - 1, pos_y])

        if change_color(screen, pos_x, pos_y + 1, row_ct, col_ct, old_color):
            screen[pos_x][pos_y + 1] = new_color
            q.append([pos_x, pos_y + 1])

        if change_color(screen, pos_x, pos_y - 1, row_ct, col_ct, old_color):
            screen[pos_x][pos_y - 1] = new_color
            q.append([pos_x, pos_y - 1])

screen = [
  [2, 2, 2, 1, 1, 1, 0, 0],
  [2, 1, 1, 1, 1, 1, 1, 0],
  [2, 1, 0, 0, 0, 1, 1, 0],  
  [2, 1, 0, 0, 1, 1, 1, 0],
  [2, 1, 0, 0, 1, 1, 1, 0],
  [2, 1, 0, 0, 0, 1, 1, 0],
  [2, 2, 2, 1, 1, 1, 0, 0],
  [2, 2, 2, 1, 1, 1, 1, 1],
]

flood_fill(screen, 4, 4, 3)

for row in screen:
    print(row)