#!/bin/usr/python
"""PyXO.app
module containing the X and O game rendered using TKinter
"""

def game_mode(mode: int) -> int:
	"""game_mode
	determines which mode to run the game, Terminal or Graphic,
	and executes the game in the selected mode

	Args:
		mode (int): user defined or requested game mode
		0 - Terminal Mode
		1 - Graphic Mode

	Returns:
		int: Outcome of this function 0 - fail or 1 - success
	"""
	try:
		if mode == 0:
			return terminal()
		else:
			return graphic()
	except BaseException as e:
		print(e)
		return 0

def main(argv: list) -> int:
	"""main
	Program's main function from which the app is run
 
 	Args:
		argv (list[str]): command line args
		[-t] - Terminal
		[-g] - Graphic

	Returns:
		int: Outcome of this function 0 - fail or 1 - success
	"""
	try:
		if len(argv) == 1:
			return game_mode(0)
		elif len(argv) == 2 and argv[1].lower() == "-t" or argv[1].lower() == 'terminal':
			return game_mode(0)
		elif len(argv) == 2 and argv[1].lower() == "-g" or argv[1].lower() == 'graphic':
			return game_mode(1)
		else:
			raise SyntaxError()
	except SyntaxError:
		sys.exit("python3 app.py [-t] | [terminal] | [-g] | [graphic] ")
	except BaseException as e:
		print(str(e))
		return 0


if __name__ == '__main__':
    import sys
    from game_modes.graphic import main as graphic
    from game_modes.terminal import main as terminal
    try:
    	main(sys.argv)
    except BaseException as e:
        print(e)