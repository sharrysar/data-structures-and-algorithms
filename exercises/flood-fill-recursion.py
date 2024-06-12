def recursion_flood_fill(screen, x, y, old_color, new_color):
    if 0 <= x < len(screen) and 0 <= y < len(screen[0]) and screen[x][y] == old_color:
        screen[x][y] = new_color
        recursion_flood_fill(screen, x + 1, y, old_color, new_color)
        recursion_flood_fill(screen, x - 1, y, old_color, new_color)
        recursion_flood_fill(screen, x, y + 1, old_color, new_color)
        recursion_flood_fill(screen, x, y - 1, old_color, new_color)

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

recursion_flood_fill(screen, 4, 4, 1, 3)

for row in screen:
    print(row)
    