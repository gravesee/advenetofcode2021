# Python program to print all paths from a source to destination.

visitedList = []

def is_lower(x):
  return (x.lower() == x)



def depthFirst(graph, currentVertex, visited):
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if (vertex not in visited) or (not is_lower(vertex)):
            depthFirst(graph, vertex, visited.copy())
    if currentVertex == "end":
      visitedList.append(visited)


from collections import Counter
def any_small_twice(vertex, visit_counts):
  if vertex in ["start", "end"]:
    return False
  return all([v < 2 for v in visit_counts.values()]) and len(visit_counts) > 0


def depthFirst_single_small(graph, currentVertex, visited, visit_counts):
    visited.append(currentVertex)
    if is_lower(currentVertex):
      visit_counts[currentVertex] += 1
      # print(visit_counts)
    for vertex in graph[currentVertex]:
        # print(vertex, visited, visit_counts, any_small_twice(vertex, visit_counts))
        if (vertex != "start") and ((vertex not in visited) or (not is_lower(vertex)) or (any_small_twice(vertex, visit_counts))):
            depthFirst_single_small(graph, vertex, visited.copy(), visit_counts.copy())
    if currentVertex == "end":
      visitedList.append(visited)


from collections import defaultdict

with open("data.txt", "r") as fin:
  data = [x.strip().split("-") for x in fin]

  g = defaultdict(list)
  for l, r in data:
    g[l].append(r)
    g[r].append(l)
  
  # print(g)

  
  # depthFirst(g, 'start', [])


  visit_counts = defaultdict(int)

  depthFirst_single_small(g, 'start', [], visit_counts)

  import pprint
  # pprint.pprint(visitedList)
  print(len(visitedList))