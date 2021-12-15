
import itertools
from collections import defaultdict

rules = {}
with open("data.txt", "r") as fin:
  for row in fin:
    if ">" in row:
      (a,b),c = row.strip().split(" -> ")
      rules[(a,b)] = c
    elif row == "\n":
      continue
    else:
      start = list(row.strip())

def pairwise(l):
  a, b = itertools.tee(l)
  next(b)
  return iter(zip(a, b))

## parts 1 & 2
pairs = defaultdict(int)
for tup in pairwise(start):
  pairs[tup] += 1

chars = defaultdict(int)
for ch in start:
  chars[ch] += 1

for i in range(40):
  tmp = defaultdict(int)
  for (a, b), v in pairs.items():
    z = rules.get((a, b))
    tmp[(a, z)] += v
    tmp[(z, b)] += v
    chars[z] += v
  pairs = tmp
  print(sum(chars.values())) 


mn, mx = min(chars.values()), max(chars.values())
print(chars)
print(mx - mn)
