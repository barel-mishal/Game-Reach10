import os
import time
import threading
from itertools import combinations
from random import choice

ROWS = 'ZXCVB'
COLS = 'ASDFG'
SCORE = 0
COLS_ =   {key: index for index, key in enumerate(COLS)}
ROWS_ = {key: index for index, key in enumerate(ROWS)}
def create_grid(n):
  return  [['0' for i in range(n)] for i in range(n)]
GRID = create_grid(5)

OPTIONS = set(list(combinations(COLS+ROWS, 2))) - set(combinations(COLS, 2)) - set(combinations(ROWS, 2))

DICT_OF_PLACESES = {i for i in OPTIONS}

def clearConsole():
  return os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def display(grid, grid_length, random_number):
  print(f'Reach Ten')
  print(f'Move by click one of ____ and click enter')
  print()
  print(f'number to fill: {random_number}')
  print()
  print(f'TBD (how to play)')
  for _ in range(grid_length):
    print(f'{ROWS[_]} ' + '  '.join(grid[_]))
  print(" ", f'  '.join(COLS[:length]))
  
# https://stackoverflow.com/questions/24000455/python-how-to-get-input-from-console-while-an-infinite-loop-is-running
class InputThread(threading.Thread):
    def __init__(self):
        super(InputThread, self).__init__()
        self.daemon = True
        self.last_user_input = None

    def run(self):
        while True:
            self.last_user_input = input('')

def sum_list_digits(digits):
  return sum([int(num) for num in digits])

def create_list_of_zeros(length):
  raise_score()
  return ['0' for _ in range(length)]

def raise_score(SCORE):
  SCORE += 1

def find_sums_of_10_by_row(grid):
  return [create_list_of_zeros(len(row)) if sum_list_digits(row) >= 10 else row for row in grid]


if __name__ == '__main__':
  
  counter = 1
  length = len(GRID)
  print()
  it = InputThread()
  it.start()
  while True:
    random_number = str(choice(range(1, 4)))
    display(GRID, length, random_number)
    time.sleep(9)
    user_input = it.last_user_input
    if user_input in [''.join(tupl) for tupl in OPTIONS]:
      col, row = tuple(user_input)
      GRID[ROWS_[row]][COLS_[col]] = random_number
    else:
      possibilities = 0
      col, row = choice(COLS), choice(ROWS)
      GRID[ROWS_[row]][COLS_[col]] = random_number
    GRID = find_sums_of_10_by_row(GRID)
    user_input = ''
    clearConsole()



