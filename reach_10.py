import time
from itertools import combinations
from random import choice
from constants import ROWS, COLS, SCORE
from helpers import create_grid, clearConsole, InputThread, sum_list_digits, create_list_of_zeros, find_sums_of_10_by_row

COLS_ =   {key: index for index, key in enumerate(COLS)}
ROWS_ = {key: index for index, key in enumerate(ROWS)}
GRID = create_grid(5)

OPTIONS = set(list(combinations(COLS+ROWS, 2))) - set(combinations(COLS, 2)) - set(combinations(ROWS, 2))

DICT_OF_PLACESES = {i for i in OPTIONS}

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

# def checraise_score(SCORE):
#   SCORE += 1

if __name__ == '__main__':
  
  counter = 1
  length = len(GRID)
  print()
  it = InputThread()
  it.start()
  while True:
    random_number = str(choice(range(1, 4)))
    display(GRID, length, random_number)
    time.sleep(0.5)
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



