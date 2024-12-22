import random
import os

class ticTacToe:
  def __init__(self):
    self.reset()

  def print_board(self):
    print('')
    print(' '+self.board[0][0]+' | '+self.board[0][1]+' | '+self.board[0][2])
    print('-----------')
    print(' '+self.board[1][0]+' | '+self.board[1][1]+' | '+self.board[1][2])
    print('-----------')
    print(' '+self.board[2][0]+' | '+self.board[2][1]+' | '+self.board[2][2])

  def reset(self):
    self.board = [[' ' for _ in range(3)] for _ in range(3)]
    self.done = ''

  def check_win_or_draw(self):
    dict_wint = {}

    for i in ['X','O']:
      # Horizontais
      dict_wint[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
      dict_wint[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_wint[i]
      dict_wint[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_wint[i]
      
      # Verticais
      dict_wint[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_wint[i]
      dict_wint[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_wint[i]
      dict_wint[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_wint[i]

      # Diagonais
      dict_wint[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_wint[i]
      dict_wint[i] = (self.board[0][2] == self.board[1][1] == self.board[2][0] == i) or dict_wint[i]
    
    if dict_wint['X']:
      self.done = 'X'
      print('X wins')
      return
    elif dict_wint['O']: 
      self.done = 'O'
      print('O wins')
      return
    
    d = 0
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == ' ':
          d += 1
          break
    if d == 0:
      self.done = 'D'
      print('Draw')
      return

  def get_palyer_move(self):
    invalid_move = True

    while invalid_move:
      try:
        x = int(input('Digite a linha do seu proximo lance: '))
        y = int(input('Digite a coluna do seu proximo lance: '))
        if x > 2 or x < 0 or y > 2 or y < 0:
          print('Posição inválida')
          continue
        if self.board[x][y] != ' ':
          print('Posição já preenchida')
          continue
      except Exception as e:
        print(e)
        continue
      invalid_move = False

    self.board[x][y] = 'X'

  def make_move(self):
    list_moves = []

    for i in range(3):
      for j in range(3):
        if self.board[i][j] == ' ':
          list_moves.append((i,j))

    if len(list_moves) > 0:
      x, y = random.choice(list_moves)
      self.board[x][y] = 'O'

tic_tac_toe = ticTacToe()
tic_tac_toe.print_board()

next_t = 0

while next_t == 0:
  os.system('cls')
  tic_tac_toe.print_board()
  while tic_tac_toe.done == '':
    tic_tac_toe.get_palyer_move()
    tic_tac_toe.make_move()
    os.system('cls')
    tic_tac_toe.print_board()
    tic_tac_toe.check_win_or_draw()
  op = int(input('Digite qualquer tecla para jogar novamente ou 1 para sair: '))
  if op == 1:
    break
  else:
    tic_tac_toe.reset()
    next_t = 0

