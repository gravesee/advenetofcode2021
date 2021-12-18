# this is a graph problem - Djikstra's algorithm

# Create the edge list and node values
from collections import defaultdict
import pprint


nodes = {}
edges = defaultdict(set)
# G = nx.graph()
def embiggen(data, k):
  pprint.pprint(data)
  # expand to the right
  res = data.copy()
  for i, row in enumerate(data):
    for j, v in enumerate(row):
      res[i][j] = (res[i][j] % 9) + k
  pprint.pprint(res)
  return res

# coords = [(-1,0),(0,-1),(0,1),(1,0)]
coords = [(0,1),(1,0)]

def in_bounds(xy, aa, bb):
  res = ((xy[0] >= aa[0]) and (xy[1] >= aa[1])) and ((xy[0] <= bb[0]) and (xy[1] <= bb[1]))
  return res


def iter_edges(xy, aa, bb):
  for x, y in coords:
    pt = (xy[0] + x, xy[1] + y)
    if in_bounds(pt, aa, bb):
      yield pt

import networkx as nx


with open("test.txt", "r") as fin:
  data = list(map(lambda x: list(map(int, x)), fin.read().strip().split("\n")))


aa = (0, 0)
bb = (len(data)-1, len(data[0])-1)

G = nx.DiGraph()

vals = {}
for i, row in enumerate(data):
  for j, _ in enumerate(row):
    G.add_node((i, j))
    print(_, end="")
    for u, v in iter_edges((i, j), aa, bb):
      w = data[u][v]
      vals[(u, v)] = w
      G.add_edge((i, j), (u, v), edge_weight=w)
  print("\n", end="")

# print(G.nodes, G.edges)
## start at 0,0 and go down or right based on lowest value
from networkx.algorithms import shortest_path
path = shortest_path(G, source=aa, target=bb, weight="edge_weight")

print(path)
soln1 = [vals[p] for p in path[1:]]
print(soln1)
print(sum(soln1))

## draw the path

bigger = embiggen(data, 1)

# vals = {}
# for i, row in enumerate(data):
#   for j, _ in enumerate(row):
#     if (i,j) in path:
#       print(".", end="")
#     else:
#       print(_, end="")
#   print("\n", end="")


