import numpy as np
from scipy.ndimage import label

def process_data(text):
  rows = text.strip().split("\n")
  array = list(map(lambda x: list(map(int, list(x))), rows))
  return np.array(array)

def is_low_point(w):
  mid = w[1,1]
  oth = w[np.array([0,2,1,1]),np.array([1,1,0,2])]
  return np.all(mid < oth)

def find_regions(data):
  return label((data != 9) + 0)


if __name__ == '__main__':
  with open('data.txt', 'r') as fin:
    data = process_data(fin.read())
  
  # create numpy convolutions
  padded = np.pad(data, 1, 'constant', constant_values=(10))

  windows = np.lib.stride_tricks.sliding_window_view(padded, (3, 3))

  # low_pionts
  soln1 = 0
  coords = []
  for x, row in enumerate(windows):
    for y, w in enumerate(row):
      if is_low_point(w):
        coords.append((x, y))
        soln1 += w[(1,1)] + 1

  print(soln1)

  regions, _ = find_regions(data)
  
  region_sizes = []
  for x, y in coords:
    count = (regions == regions[x, y]).sum()
    region_sizes.append(count)
  
  soln2 = np.prod(sorted(region_sizes)[-3:])
  print(soln2)