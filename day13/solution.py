

grid = set()
folds = []
with open("data.txt", "r") as fin:
  for row in fin:
    if "," in row:
      x, y = map(int, row.strip().split(","))
      grid.add((x, y))
    elif row == "\n":
      continue
    else:
      _, _, fold = row.strip().split(" ")
      axis, value = fold.split("=")
      folds.append((axis, value))



from itertools import filterfalse
def filter_folds(grid, value, axis='x'):
  i = ['x','y'].index(axis)
  # return two lists
  above = filterfalse(lambda xy: xy[i] > value, grid)
  below = filter(lambda xy: xy[i] > value, grid)

  return set(above), set(below)


def fold(grid, value, axis):
  i = ['x','y'].index(axis)
  
  grid, tmp = filter_folds(grid, value, axis)
  
  ## for the b-folds, subtract the value from the ith axis
  for _ in tmp:
    pt = list(_)
    diff = pt[i] - value
    pt[i] -= diff * 2
    grid.add(tuple(pt))
  return grid


  
# solution 1
for axis, value in  [folds[0]]:
  res = fold(grid, int(value), axis)
  print(len(res))


# solution 1
for axis, value in  folds:
  grid = fold(grid, int(value), axis)

# print out the grid

for x in range(50):
  for y in range(50):
    if (y, x) in grid:
      print("*", end="")
    else:
      print(" ", end="")
  print("\n", end="")



# solution 1



    
# print(grid, folds)