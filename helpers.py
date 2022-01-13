import os
import threading

def sum_list_digits(digits):
  return sum([int(num) for num in digits])

def create_grid(n):
  return  [['0' for i in range(n)] for i in range(n)]

def clearConsole():
  return os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# https://stackoverflow.com/questions/24000455/python-how-to-get-input-from-console-while-an-infinite-loop-is-running
class InputThread(threading.Thread):
    def __init__(self):
        super(InputThread, self).__init__()
        self.daemon = True
        self.last_user_input = None

    def run(self):
        while True:
            self.last_user_input = input('')

def create_list_of_zeros(length):
  return ['0' for _ in range(length)]

def find_sums_of_10_by_row(grid):
  return [create_list_of_zeros(len(row)) if sum_list_digits(row) >= 10 else row for row in grid]