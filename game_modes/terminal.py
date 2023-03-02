"""terminal
module responsible for running pyxo in the terminal
"""
from .models.models import Symbol
from pyinputplus import inputChoice
from random import choice

class Grid:
	"""Grid Class
	Abstracts the creation and display of the X and O on a terminal 3 x 3 grid
	"""
	_empty: list[list[str]] = [["", "", ""], ["", "", ""], ["", "", ""]] # empty matrix indicating an empty board

	def __init__(self, matrix: list[list[str]] = _empty) -> None:
		"""Constructor

		Args:
			matrix (list[list[str]], optional): matrix to include in the grid. Defaults to _empty.
		"""
		if Grid.check_matrix(matrix):
			self._matrix = matrix
		else:
			self._matrix = self._empty

	def display_grid(self):
		""" Prints the grid using the existing matrix """
		print( """\
             A   B   C
           ------------
        1 ┆  {0:1} │ {1:1} │ {2:1}
          ┆ ───┼───┼───
        2 ┆  {3:1} │ {4:1} │ {5:1}
          ┆ ───┼───┼───
        3 ┆  {6:1} │ {7:1} │ {8:1}
    """.format(*self.matrix[0], *self.matrix[1], *self.matrix[2]))

	@property
	def matrix(self):
		""" Getter function for the matrix private attr/prop """
		return self._matrix

	@matrix.setter
	def matrix(self, value: list[list[str]]):
		""" Setter function for the matrix private attr/prop """
		if Grid.check_matrix():
			self._matrix = value

	@staticmethod
	def check_matrix(matrix: list[list[str]]) -> bool:
		""" Static function for checking the validity of the matrix passed """
		if type(matrix) is not list or len(matrix) != 3:
			return False
		for elem in matrix:
			if type(elem) is not list or len(elem) > 3:
				return False
			for i in elem:
				if type(i) is not Symbol and i != "":
					return False
		return True

def main() -> int:
	"""main
	function responsible for running the terminal components
	"""
	TABLE = {"1": (0, 0), "2": (1, 0), "3": (2, 0), "4": (0, 1), "5": (1, 1), "6": (2, 1), "7": (0, 2), "8": (1, 2), "9": (2, 2), "a1": (0, 0), "a2": (1, 0), "a3": (2, 0), "b1": (0, 1), "b2": (1, 1), "b3": (2, 1), "c1": (0, 2), "c2": (1, 2), "c3": (2, 2), }
	GAME = {"True": Symbol.X.value, "False": Symbol.O.value}
	turn = choice([True, False])
	while True:
		grid = Grid()
		grid.display_grid()
		check = game_state(grid.matrix) 
		if check:
			return check

		guess: str = inputChoice(prompt=f"{GAME[str(turn)]}'s Move: ", choices=list(TABLE.keys())).lower()
		if grid.matrix[TABLE[guess][0]][TABLE[guess][1]] != "":
				continue
		grid.matrix[TABLE[guess][0]][TABLE[guess][1]] = GAME[str(turn)]

		grid.display_grid()
		turn ^= True


def game_state(matrix: list[list[str]]) -> int:
	""" Determines what state the game is in, Game over or Winner """
	check: list = list(map(lambda x: list(filter(lambda y: y != "", x)), matrix))
	if check_winner(matrix):
		return display_winner(check_winner(matrix))
	if len(check[0]) == 3 and len(check[1]) == 3 and len(check[2]) == 3:
		return display_winner("DRAW!!!")
	return 0

def check_winner(matrix: list[list[str]]) -> str:
	"""Checks if theres a winner

	Args:
		matrix (list[list[str]]): the matrix to eval

	Returns:
		Symbol: Winners symbol or nothing
	"""
	matrix: list[str] = [*matrix[0], *matrix[1], *matrix[2]]
	if matrix[1] == matrix[0] and matrix[2] == matrix[0] and matrix[0]:
		return matrix[0]
	if matrix[4] == matrix[3] and matrix[5] == matrix[3] and matrix[3]:
		return matrix[3]
	if matrix[7] == matrix[6] and matrix[8] == matrix[6] and matrix[6]:
		return matrix[6]

	if matrix[3] == matrix[0] and matrix[6] == matrix[0] and matrix[0]:
		return matrix[0]
	if matrix[4] == matrix[1] and matrix[7] == matrix[1] and matrix[1]:
		return matrix[1]
	if matrix[5] == matrix[2] and matrix[8] == matrix[2] and matrix[2]:
		return matrix[2]

	if matrix[4]  == matrix[0]and matrix[8] == matrix[0] and matrix[0]:
		return matrix[0]
	if matrix[4] == matrix[2] and matrix[6] == matrix[2] and matrix[2]:
		return matrix[2]
	return ""

def display_winner(winner: str) -> int:
	"""Prints the winner

	Args:
		winner (Symbol): Symbol for the winner

	Returns:
		int: always 1
	"""
	if winner != "DRAW":
		print(f"{winner}'s win 🎉")
		return 1
	print(f"{winner}")
	return 2