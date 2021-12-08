from functools import partial
import math


def distance(x, target, cost=lambda x: 1):
  diff = abs(x - target)
  dist = 0
  for i in range(diff):
    dist += cost(i)
  return dist


if __name__ == "__main__":

  with open("data.txt", "r") as fin:
    data = list(map(int, fin.read().strip().split(",")))

    ### Solution 1
    # The cost function described in challenge 1 is just the l1 norm
    # We can just use the median value but need to account for an even
    # number of elements in the array.
    
    s = sorted(data)
    i = len(data)/2
    if int(i) != i:
      medians = [s[math.floor(i)], s[math.ceil(i)]]
      a = sum(map(partial(distance, target=medians[0]), data))
      b = sum(map(partial(distance, target=medians[1]), data))
      soln1 = min(a, b)
    else:
      soln1 = sum(map(partial(distance, target=s[int(i)]), data))

    print(soln1)

    ### Solution 2
    # The cost function described in the challenge is an affine transformation of
    # any increasing cost function. Therefore, the value that leads to the minimum value
    # will be the same as for an easy-to-calculate measure of centrality like the mean

    mean = sum(data) / len(data)

    s = sorted(data)
    targets = [math.floor(mean), math.ceil(mean)]
    a = sum(map(partial(distance, target=targets[0], cost=lambda x: x + 1), data))
    b = sum(map(partial(distance, target=targets[1], cost=lambda x: x + 1), data))
    soln2 = min(a, b)
    print(soln2)

    