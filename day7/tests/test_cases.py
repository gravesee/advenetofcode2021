import pytest
from ..solution import distance

def test_cases():
  assert distance(5, 10) == 5
  assert distance(10, 5) == 5

  assert distance(10, 5) == 5
  assert distance(16,  5, lambda x: x + 1) == 66
  assert distance(1,  5, lambda x: x + 1) == 10
  assert distance(2,  5, lambda x: x + 1) == 6
  assert distance(0,  5, lambda x: x + 1) == 15
  assert distance(4,  5, lambda x: x + 1) == 1
  assert distance(2,  5, lambda x: x + 1) == 6
  assert distance(7,  5, lambda x: x + 1) == 3
  assert distance(1,  5, lambda x: x + 1) == 10
  assert distance(2,  5, lambda x: x + 1) == 6
  assert distance(14,  5, lambda x: x + 1) == 45
  