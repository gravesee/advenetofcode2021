
import itertools

class Bingo():
  def __init__(self):
    self.board = {}
    self.row = -1
    pass

  def add_row(self, row):
    self.row += 1
    for x, value in enumerate(row):
      self.add_item(value, x)

  def add_item(self, value, x):
    self.board[value] = [x, self.row, 'o']
  
  def mark_board(self, value):
    if self.board.get(value, None) is not None:
      self.board[value][2] = 'x'

  def has_bingo(self):
    exes = list(filter(lambda x: x[2] == 'x', self.board.values()))
    if len(exes) < 5:
      return False
    else:
      xs = [x[0] for x in exes]
      ys = [x[1] for x in exes]
      
      # check if any rows are filled
      for _, grp in itertools.groupby(sorted(xs)):
        if len(list(grp)) >= 5:
          return True
      
      for _, grp in itertools.groupby(sorted(ys)):
        if len(list(grp)) >= 5:
          return True
    
    return False
  
  def sum(self):
    # check if all rows or cols are marked with x
      # get the unmarked values
    items = filter(lambda x: x[1][2] == 'o', self.board.items())
    return sum(map(int, [x[0] for x in items]))

   

    
  
  def __repr__(self):
    return(str(self.board))


def read_data(path: str):

  boards = []

  with open(path, "r") as fin:
    # get the first row
    draws = fin.readline().strip().split(",")

    
    # tread all of the bingo boards
    for row in fin:
      if row == "\n":
        board = Bingo()
        boards.append(board)
      else:
        values = row.strip().split()
        board.add_row(values)
        
  return draws, boards

import pprint
if __name__ == "__main__":

  draws, boards = read_data("data.txt")

  skip = [False for board in boards]
  results = []

  ## play the game
  for draw in draws:
    for i, board in enumerate(boards):
      if not skip[i]:
        board.mark_board(draw)
        if board.has_bingo():
          skip[i] = True
          results.append(int(draw) * board.sum())
  
  print(results[-1])