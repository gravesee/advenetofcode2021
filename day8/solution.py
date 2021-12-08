import itertools
from collections import defaultdict

def decode(dd):

  one   = dd[2][0]
  four  = dd[4][0]
  seven = dd[3][0]
  eight = dd[7][0]

  ## the one with 5 segments and the same one as 1 is a 3
  three = list(filter(lambda x: len(set(one) - set(x)) == 0, dd[5]))[0]
  bb = set(four) - set(three)

  five = list(filter(lambda x: len(bb - set(x)) == 0, dd[5]))[0]
  two  = list(set(dd[5]) - set([three, five]))[0]

  six  = list(filter(lambda x: len(set(one) - set(x)) > 0, dd[6]))[0]

  # remove six from the list
  nosix = list(filter(lambda x: len(set(x) - set(six)) > 0, dd[6]))
  zero = list(filter(lambda x: len(set(four) - set(x)) > 0, nosix))[0]
  nine = list(set(dd[6]) - set([zero, six]))[0]
  # print(len(nine))

  patterns = [zero, one, two, three, four, five, six, seven, eight, nine]
  lookup = { ''.join(sorted(x)): str(i) for i, x in enumerate(patterns)}

  return lookup

def solve(lookup, outputs):
  nums = [lookup.get(''.join(sorted(x))) for x in outputs]
  return int(''.join(nums))

with open("data.txt", "r") as fin:
  inputs = []
  outputs = []
  for row in fin:
    a, b = row.strip().split(" | ")
    inputs.append(a.split(" "))
    outputs.append(b.split(" "))
  
  # solution1
  guesses = map(len, itertools.chain.from_iterable(outputs))
  
  soln1 = len(list(filter(lambda x: x in [2,3,4,7], guesses)))
  print(soln1)

  # create input mappings
  res = []
  for input in inputs:
    dd = defaultdict(list)
    for i in input:
      dd[len(i)].append(i)
    res.append(dict(dd))
  
  soln2 = 0
  for x, y in zip(res, outputs):
    decoder = decode(x)
    soln2 += solve(decoder, y)
  
  print(soln2)
  