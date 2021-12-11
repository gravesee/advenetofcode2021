
from typing import Set

# import data and store each point as an object with neighbors

with open("data.txt", "r") as fin:
  data = [[int(x) for x in x.strip()] for x in fin]

class Octopus:
  def __init__(self, level):
    self._original_level = level
    self.level = level
    self.neighbors: Set["Octopus"] = set()
    self._flashed = False
  
  def reset(self):
    self._flashed = False
  
  def hard_reset(self):
    self.level = self._original_level
  
  def increase_energy(self):
    if not self.flashed:
      self.level += 1

    if (self.level > 9):
      self.flash()
      self.level = 0
      
  def add_neighbor(self, o):
    self.neighbors.add(o)

  def flash(self):
    if not self.flashed:
      self._flashed = True
      for n in self.neighbors:
        n.increase_energy()
  
  @property
  def flashed(self):
    return self._flashed


# create base list
octopuses = []
for i, row in enumerate(data):
  octopuses.append([])
  for j, level in enumerate(row):
    octopuses[i].append(Octopus(level))

coords = [(-1,-1),(-1,0),(-1,1),
          (0,-1),(0,1),
          (1,-1),(1,0),(1,1)]

def in_bounds(xy, aa, bb):
  res = ((xy[0] >= aa[0]) and (xy[1] >= aa[1])) and ((xy[0] <= bb[0]) and (xy[1] <= bb[1]))
  return res
  
# add the neighbors
aa, bb = (0,0), (len(data[0]) - 1, len(data) - 1)
for i, row in enumerate(octopuses):
  for j, level in enumerate(row):
    for ci, cj in coords:
      x,y = ((ci + i), (cj + j))
      if in_bounds((x,y), aa, bb):
        octopuses[i][j].add_neighbor(octopuses[x][y])


from itertools import chain, repeat
flatlist = list(chain.from_iterable(octopuses))

import pprint

def print_state():
  pprint.pprint(([[o.level for o in v] for v in octopuses]))

def print_neighbors():
  pprint.pprint(([[len(o.neighbors) for o in v] for v in octopuses]))

# now process the steps
flashes = 0
for step in range(100):
  for o in flatlist:
    o.increase_energy()
  for o in flatlist:
    if o.flashed:
      flashes += 1
    o.reset()

# solution 1
print(flashes)

from itertools import count

for o in flatlist:
  o.hard_reset()

for step in count(1):
  for o in flatlist:
    o.increase_energy()
  
  flashes = 0
  for o in flatlist:
    if o.flashed:
      flashes += 1
    o.reset()
  
  if (flashes == len(flatlist)):

    break

# solution 2
print(step)
print_state()