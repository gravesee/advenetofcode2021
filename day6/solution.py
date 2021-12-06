import itertools
from typing import Dict

def tick(state: Dict[str, int]) -> Dict[str, int]:
  # create new state from existing state
  new = {}
  for k, v in state.items():
    new[k-1] = v

  # handle -1
  if -1 in new.keys():
    new[8] = new.get(-1, 0)
    new[6] = new.get(6, 0) + new.get(-1, 0)
    del new[-1]
  return new

with open("data.txt", "r") as fin:
  lines = fin.readlines()[0].strip()

  data = map(int, lines.split(","))

  state = {}
  grps = itertools.groupby(sorted(data))
  for k, grp in grps:
    state[k] = len(list(grp))
  
  print("start", state)
  
  for i in range(256):
    print(state)
    state = tick(state)

  print(sum(state.values()))