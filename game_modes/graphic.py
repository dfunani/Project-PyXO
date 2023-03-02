"""Graphics module
PyXO game in graphic mode.
Run on a graphics window generated using TK"""

from tkinter import *
from .terminal import Grid

class GameWindow(Tk):
    """Game Window Class
    maintaining the game window 
    when in graphics mode

    Args:
        tk (tkinter.tk): TK root window class from which we inherit
    """
    
    def __init__(self, title="PyXO"):
        """Constructor for the GameWindow Class
        """
        super().__init__()
        self.config(bg='black')
        self.title(title)
        self.maxsize(width=500, height=500)
        self.minsize(width=500, height=500)
        self._grid = Grid.empty

class GameBoard(Frame):
    """Abstraction of the game board

    Args:
        Frame (ttk.Frame): abstraction of the frame to use as the game board
    """
    
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.pack()

class GameButton(Button):
    """Game button abstracted to a class

    Args:
        Button (tkinter.ttk.Button): Base TK Button Class
    """
    
    def __init__(self, master):
        """Constructor for the button class
        """
        super().__init__()
        self.master = master
        self.config(text='Hello', fg='red', bg='red')
    
def main() -> int:
    root = GameWindow()
    root.display = GameBoard(root)
    root.display.pack()
    root.mainloop()